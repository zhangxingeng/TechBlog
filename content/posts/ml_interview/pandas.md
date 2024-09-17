---
title: "Notes on pandas selections"
date: 2024-04-01
---

- `table[]`, `table.loc[]` and `table.iloc[]`
- `iloc`
  - `iloc` is for indices of rows (the number thing before first column)
  - `table.iloc[:, [0, 2]]` select column 1 and 3 of all rows. 
  - Notice you can do **both row and column** selection just like `iloc`
- `loc`
  - `loc` is the general solution when it comes to sub-tables. Syntax`table[<row_id | row_cond>, <column_names>]`
  - Notice how you can select row **and** column at the same time whereas `table[]`
  - `df.loc[df['A'] > 2, ['B', 'C']]`
- `[]`
  - just typical simple **column** selection like a filter, cant select columns.
  - `table[['col1', 'col2']]` select column 1 and 2 of all rows.