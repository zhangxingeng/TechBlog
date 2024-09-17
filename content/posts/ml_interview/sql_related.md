---
title: "Notes on sql commands"
date: 2024-04-01
---

- Auto increment: 
  - unique number for each row, 
  - defined at table creation, 
  - no need to specify when adding rows
    ```SQL
    CREATE TABLE Employees (
        EmployeeID int NOT NULL AUTO_INCREMENT,
        ...);
    ```

- Auto commit
  - default mode, each SQL statement is treated as a transaction
  - auto rollback if failed as if nothing happened
  - if you use `BEGIN TRANSACTION` in query, sql server would suspend auto commit and wait till a `COMMIT` or `ROLLBACK` is issued
  - before `COMMIT` is issued, changes made wont be seen by others, also the data being changed maybe be locked to prevent inconsistency
  - log is flushed to disk after commit
  - data is lasy written to disk independent to commits


### Commands
- `like` find similar strings (`%` is any number of chars (0-inf), while `_` is 1 char exactly)
- `[First Name]` if your field name has spaces, use square brackets to avoid parsing errors
- `'someString'` use tick for string values
- 
- `update <table>` for updating existing rows
- `alter <table>` for changing table structure like adding columns
- 
- `add <attr>`: add new attribute
- `Set <attr>` to the change existing attribute
- 
- `--` one line comment `/**/` multi-line comment
- `add foreign key (ProductID) references Products(ID)` add foreign key to table
- `ORDER BY col1, col2 ASC|DESC` order by multiple columns from left to right
- `LIMIT n` select top n 
- Aggregate functions like `SUM`, `COUNT`, `AVG`, `MIN(col_name)`, `MAX`
- `WHERE col_name IN ('s1', 's2')` select rows where col_name is in the list
- `between` for range, `>`, `<`, `>=`, `<=` for comparison

- `CREATE TABLE foo (b BINARY(16)  DEFAULT (UUID_TO_BIN(UUID())));` create default PK using UUID
-
  ```sql
  --inner join
  SELECT ...
  FROM table_left
  INNER JOIN table_right
  ON table_left.column_name = table_right.column_name;
  ```
- 
  ```sql
  -- How to use alias for the same table to join with self
  SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
  FROM Customers AS A, Customers AS B
  WHERE A.CustomerID <> B.CustomerID
  AND A.City = B.City
  ORDER BY A.City;
  ```


### Compare with pandas
- `contains()` use regex to find strings, more powerful than `like` in sql