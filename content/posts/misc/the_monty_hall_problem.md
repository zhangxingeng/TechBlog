---
date: 2024-05-13
title: "In Depth Explanation of The Monty Hall Problem With python experiment Code" 
---
### Problem
- Given three doors with one car and two goats behind them, you choose one door.
- The host then opens one of the other two doors to reveal a goat.
- You are then given the option to switch doors or stick with your original choice.
- What should you do to maximize your chances of winning the car?

### My Thought Process
- After host opens a door, the prbability still wont change so switching really wont make a difference.
- However, the trick is revealed when you stand in the shoe of the host.
- imagine you are the host, some player picked a door
  - assume the player picked the car, lucky him, the host just randomly pick a door thats not picked by the player
  - however, if the player picked a goat, now the host can only open one door since the other one is the car, and the host cant pick the player's door
  - Now the door the host didnt pick contains more information -- its must contain the car (assume player picked the goat first)
  - Obviously if you pick the door the host didnt pick, you will have a higher chance of winning the car.

### Math
- For easy understanding, lets say player picked door 1, and the host opened door 2
- Lets define the event of door 1 containing a car as $C$
- We could also define the event of the player switch and got the car as $S$
- We could easily get the probability of the player not switching and getting the car as $P(C) = \frac{1}{3}$
- We know the bayes theorem:
    $$
    P(A|B) \cdot P(B) = P(B|A) \cdot P(A)
    $$
- We also know the law of total probability
    $$
    P(B) = P(B|A) \cdot P(A) + P(B| \neg A) \cdot P(\neg A)
    $$
- Using the law of total probability, we can compute the probability of the player switched and got the car as:
    $$
    P(S) = P(S|C)\cdot P(C) + P(S| \neg C)\cdot P( \neg C)
    $$
- $P(C) = \frac{1}{3}$, $P(\neg C) = \frac{2}{3}$
- $P(S|C) = 0$, since if the player picked the car, switching will make him lose
- $P(S| \neg C) = 1$, since if the player picked the goat, switching will make him win
- Now we can compute P(S) as:
    $$
    P(S) = 0 \cdot \frac{1}{3} + 1 \cdot \frac{2}{3} = \frac{2}{3}
    $$
- This means a increased chance of winning. If confused go back to how we stand in the shoe of the host and see how his action is constrained by the fact that he cant open the player's door, and he cant open the door with the car.

### Experiment
- In case you need solid proof, here's a simple python code to simulate the game and see the result:

```python
import random

num_experiments = 10000
stay_win_count = 0
switch_win_count = 0
doors = ['goat', 'goat', 'car']

for _ in range(num_experiments):
    random.shuffle(doors)
    player_choice = random.randint(0, 2)

    # The host's turn: he can't open the players door and cant open the car door
    host_door_rule = lambda i: i != player_choice and doors[i] == 'goat'
    host_door_options = [i for i in range(3) if host_door_rule(i)]  # doors indices the host can pick from
    if len(host_door_options) == 1:  # host dont have a choice, must pick the goat
        rand_goat_door = host_door_options[0]
    else:  # `if len(host_door_options) == 2` # randomly pick one of the two goat doors
        rand_goat_door = random.choice(host_door_options)

    # gather stat after switch
    switched_door = next(i for i in range(3) if i != player_choice and i != rand_goat_door)

    # check if player wins and keep record
    if doors[player_choice] == 'car':  # initial choice gives a car
        stay_win_count += 1
    if doors[switched_door] == 'car':  # switched choice gives a car
        switch_win_count += 1

print(f"Probability of winning by staying: {stay_win_count / num_experiments}")
print(f"Probability of winning by switching: {switch_win_count / num_experiments}")

# Output I got:
# Probability of winning by staying: 0.3331
# Probability of winning by switching: 0.6669

```