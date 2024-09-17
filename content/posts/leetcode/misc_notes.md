---
date: 2023-11-17
title: "Random Python tips for interview coding"
---

- use `is not` for reference comparison and compare to `None`, use `!=` for value comparison
- stack and queue use `collections.deque` with functions: `append`, `appendleft`, `pop`, `popleft`
- sliding window always consider reuse the previous result
- Binary Tree:
  - Core concept: each sub-tree is another tree, use recursion to simplify the problem
- generators:
  - `yield` return the value and pause the action, but state is saved (next call will continue from the last `yield`)
  - `yield from` delegate one generator to another generator
- python list: `==` compare value, `is` compare reference
- When you need to keep something tracked in a dfs or bfs, just push it into the stack or queue along with the node