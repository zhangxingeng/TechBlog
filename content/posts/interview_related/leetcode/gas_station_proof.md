---
date: 2023-11-17
title: "Gas station Problem Proof"
---

### Problem [LeetCode Gas Station](https://leetcode.com/problems/gas-station/description/)
-The difficult thing about this is not the algorithm, its the mathmatical proof of this algorithm
- The algorithm is:
```python
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    curr_gas = 0
    start_station = 0

    for i in range(len(gas)):
        curr_gas += gas[i] - cost[i]

        if curr_gas <0:
            start_station = i+1
            curr_gas = 0
    return start_station
```

### Assumption
$\Delta_{0}^{k}$ is the smallest piece of route for any start to any end （without reaching a complete loop）

### Prove: start from k+1 we always have gas left
- we want to prove that if total gas is > total cost then there will be at least one solution where can gas tank remain non-negative throughout the journey.
- We will use induction to prove this.
- We call gas - cost as delta
- Assume we have n+1 stations from staion 0 to station n.
- since the circuit is a circle we can set the staring point anywhere, for simplicity's sake we just say the starting point 0 and ending point k is the smallest cumulative sum.
- We can easily prove that since loop 1 circuit gives positive gas leftover, then the smallest cumulative sum cannot go beyond 1 loop (since each loop gives more gas) Thus the smallest cumulative delta within the 1st round is true for any rounds.

- since $\Delta_{0}^{k}$ is the smallest (only consider 1st round, or only consider k < n), then $\Delta_{0}^{k+1} \geq \Delta_{0}^{k}$
- Which means $\Delta_{k+1}\geq0$
- Similarly, $\Delta_{k+1} + \Delta_{k+2}\geq0$, ... , $\Delta_{k+1} + \Delta_{k+m}\geq0$ for $m < n$, where a loop is not formed yet
    - Notice $\Delta_{k+2}$, ... , $\Delta_{k+m}$ could still be $\leq0$
    - The statement only says **CUMULATED** value from $k+1$ to $k+m$ $\geq0$
- Now lets consider when $m >= n$: We define loop sum C = $\Delta_{0}^{n}\geq 0$, 
  $$
  \Delta_{k+1}^{k + m} = \lfloor \frac{k+m}{n} \rfloor \cdot \Delta_{k+1}^{(k+n)\%n} + \Delta_{k+1}^{(k+m)\%n} = \lfloor \frac{k+m}{n} \rfloor \cdot C + \Delta_{k+1}^{(k+m)\%n}
  $$
  Since $\lfloor \frac{k+m}{n} \rfloor \cdot C \geq 0$ and $\Delta_{k+1}^{(k+m)\%n} \geq 0$ (since the $\%$ ensures this part of the route is less than a circuit so previous rule applies)
- Thus if start from k+1 we can just loop on forever (given C >= 0 of course)

### How the algorithm optimize for performance
- this proof is all good and stuff but in the actual algorithm we simply traverse the loop from idex 0 onwards and if k causes cumulacumulative sum < 0 then we start from k+1 and do the whole thing again.
- How do we link this algorithm with the given proof?
#### Difference between algorithm and Proof
- First thing we need to realize is: when we write algorithm we dont really need to do exactly as the mathmatically proof -- the condition is more relaxed: we can just start testing the water: if we can just go loop from the begining there is no need to find the min array (which is required for the math proof to work)
#### How the algorithm find the min array
- There are some features of a min subarray we could exploit:
    1. the end of a subarray k is always negative, otherwise k+1 would give a more negaive subarray
    2. We dont really need the begining of the min array, just the end of it.
    3. **If we drive from j to k successfully, then as long as we can reach j, we can reach k** (because we started from j within minimum gas possible, ie 0, if we can reach j it means we have gas >= 0 always true)
- This means we could just rule out points we can't start from
- We can just find a random starting point and drive! if at k-1 we still have positive gas and at k we have negative gas it means k is really negative!
- So we just **assume** k is the end of the min-array (see rule 1 in this section) and thus k+1 **could** be the solution
- with this trial and error we can find k+1 within 1 loop