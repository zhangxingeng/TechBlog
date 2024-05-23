---
date: 2024-05-23
title: "Solve the Queens Problem in LinkedIn"
---


### Game Rules
Your goal is to have exactly one queen  in each row, column, and color region.
Tap once to place X and tap twice for queen placement . Use X to mark where queen cannot be placed.
Two queen  cannot touch each other, not even diagonally.
You know about this game? if yes write me a python code that provides where the queen should be placed by using brutal force. assume the table is 9x9 and use 1,2,3,4,5 to represent colors
Attached is an image of the game table and passing condition queen locations (the blck queen crown icon is where the queen can be placed)

### Source Code
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
```

```python
def plot_board(color_regions, sol_pos_list, n):
    """Plot the board with queens using Matplotlib.

    Args:
        color_regions (np.array): 2D array with color codes for each region.
        sol_pos_list (list of tuples): Positions of queens, as (row, col) tuples.
        n (int): Dimension of the board (n x n).
    """
    _, ax = plt.subplots()
    cmap = ListedColormap(['#ADD8E6', '#90EE90', '#FFFFE0', '#FFA07A', '#E6E6FA', '#FFDAB9', '#FFB6C1', '#D2B48C', '#D3D3D3'])
    _ = ax.matshow(color_regions, cmap=cmap, interpolation='nearest')
    ax.set_xticks(np.arange(-.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-.5, n, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.set_xticks([])
    ax.set_yticks([])
    if sol_pos_list:
        for row, col in sol_pos_list:
            ax.text(col, row, 'Q', fontsize=12, ha='center', va='center', color='black')
    # ax.axis('off')
    plt.show()
```


```python
class QueenSolver:
    def __init__(self, color_regions):
        self.color_regions = color_regions
        self.n = color_regions.shape[0]
        self.sorted_colors = self._sort_colors_by_size()
        self.color_positions = self._precompute_positions()
        self.queens_positions = []
        self.stack = []

    def _sort_colors_by_size(self):
        """Sort colors by the number of cells in each region."""
        color_sizes = {color: np.sum(self.color_regions == color) for color in np.unique(self.color_regions)}
        return sorted(color_sizes, key=color_sizes.get)

    def _precompute_positions(self):
        """Precompute and store positions for each color."""
        positions_dict = {}
        for row in range(self.n):
            for col in range(self.n):
                color = self.color_regions[row][col]
                if color not in positions_dict:
                    positions_dict[color] = []
                positions_dict[color].append((row, col))
        return positions_dict

    def solve(self):
        """Solve the queen placement problem iteratively."""
        if not self._place_queen(0):
            return None
        return self.queens_positions

    def _place_queen(self, current_index):
        """Recursively try to place queens for each color."""
        if current_index == len(self.sorted_colors):
            return True  # All queens placed

        color = self.sorted_colors[current_index]
        for row, col in self.color_positions[color]:
            if self._is_valid(row, col):
                self.queens_positions.append((row, col))
                if self._place_queen(current_index + 1):
                    return True
                self.queens_positions.pop()

        return False

    def _is_valid(self, row, col):
        """Check if placing a queen at (row, col) does not result in an immediate attack."""
        for r, c in self.queens_positions:
            if r == row or c == col or abs(row - r) == 1 and 1 == abs(col - c):
                return False
        return True
```


```python
color_regions = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 2, 8, 1, 1],
    [1, 1, 2, 8, 2, 8, 1, 1],
    [3, 3, 8, 8, 8, 8, 6, 6],
    [3, 4, 4, 8, 8, 7, 7, 6],
    [3, 3, 4, 8, 8, 8, 7, 6],
    [5, 4, 4, 5, 8, 7, 7, 6],
    [5, 5, 5, 5, 8, 8, 6, 6]
])

solver = QueenSolver(color_regions)
solution_positions = solver.solve()
if solution_positions:
    print("Solution found:", solution_positions)
    plot_board(color_regions, solution_positions, solver.n)
else:
    print("No solution found.")
```
### Output
Solution found: [(1, 2), (4, 0), (6, 1), (5, 6), (7, 3), (3, 7), (2, 5), (0, 4)]
![](/images/linkedin_queens.png)
<!-- ![](../images/linkedin_queens2.png) -->