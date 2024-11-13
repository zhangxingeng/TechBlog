---
title: "Is_subsequence"
date: 2023-04-06T21:10:08-04:00
draft: true
---
[details](https://leetcode.com/problems/is-subsequence)

- traverse parent check if match with child
- if not parent move forward
- if yes both move forward
  - keep checking, if no longer matching, parent go back to right after first match while child go to top
  - 