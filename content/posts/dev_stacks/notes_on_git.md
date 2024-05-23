---
date: 2024-03-26
title: "Understading git Ultimate Guide"
---


# Understading git Ultimate Guide
### general idea
- The entire concept of git is based on remote copies and a local copy 
- notice how **remote can have many copies, but local only one**
- each copy in the remote is called a **branch**, and all of them as a collective is called a **repository**
- each repository have a unique url (we call it `repo_url` in the future)

### what is a `commit`
- `commit` is when your code is fitted to a local `base_branch` but remote `base_branch` does not know yet

### what is "origin"?
  - git refer to the `repo_url` by alias (we call it `url_alias` in the future), it is called the "origin", "upstream" or whatever you named it
  - git keeps track of a default `repo_url` for each local copy (a default value for `git fetch`)
  - you can hook a `repo_url` to a `url_alias` using command `git remote add origin <url>`

### what is a `branch`?
- If we use a tree as an analogy, a `branch` should really be called a leaf (time itself is the branch)
- a `branch` is a snapshot (an old copy), all `branch`es becomes a timeline keeping record the "development" history.
- `branch`es are read-only
- unlike real life where you cant have multiple timelines, a repository can have multiple timelines

### what is `fetch`:
- there is the files in different `branch`es and there is the record of all those files in all those `branch`es
- the record are the update information, you need to get them before you know what files need to update
- `git fetch` is to get those update information from the remote (what repo_url points to)

### what is `git pull`?
- `git pull <url_alias> <branch_name>` = `git fetch ` + `git merge`
- `git pull` `--rebase` = `git fetch` + `git rebase`

### what is `merge` and `rebase`?
Scenario: 
- a `branch` is really a piece of a branch in a tree analogy where fork creates new branches.
- You start work on a `feature_branch` (a branch you forked) forked from a `base_branch` (the base point where your branch is forked from) point in the `main_branch` (the latest branch).
- (fully understand these three important nodes in the development tree before proceeding)
- Meanwhile, the `main_branch` receives updates; and you and others have made multiple commits on the `feature_branch` 
- Now a simple solution is to `merge` `feature_branch` to `main_branch`. which would work usually.
However your to a point where you start to think you should move each commit at a time instead of just smash two very different versions together and spend days trying to fix all the conflicts. Also you found out that some of the commits are made my your collegues and you dont have their permission to merge their changes. one solution is to `rebase` your `feature_branch` to `main_branch` and then `merge` it to `main_branch`
- this way you wont see a branch is split at an earlier time, then merged back at a later time, since all the old commits are now moved to the latest point -- `main_branch`. (this is called a linear history)
- basically, its always a good idea to `rebase` before `merge` if you are not sure if your branch is up-to-date.

### what is `stash`?
- git have only one local copy in a way that you can only have one **Active** copy. You can always `stash` things you dont want to handle and deal with it later using
- `stash` only stash changes, not all files
- to apply old stash to current `local_branch`
  - get stash list `git stash list` 
  - `git stash apply stash@{n}` (n is index)
  - once the change in stash merges with current `local_branch`, `git stash drop stash@{n}`