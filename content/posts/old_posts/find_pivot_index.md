---
title: "Find_pivot_index"
date: 2023-04-04T17:45:52-04:00
draft: false
---

- [Original problem](https://leetcode.com/problems/find-pivot-index/)
- First idea: use two marks to mark left step and right step
    - sum_l > sum_r: pointer_r move toward center, vice versa until pointer_r == pointer_l
    - Problem: not considering negative values.
- Solution: instead of predicting by moving toward the center, we can assume one pivot point (eg. front of array)
- Move assumed point right until it is pivot point or -1
- [Source](/static/cpp/find_pivot_index.cpp)

