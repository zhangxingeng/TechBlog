---
date: 2024-01-21
title: "Unreal - Part 6: Unreal Folder Structure"
---
### Intro
I have been trying to build a simple unreal game lately for fun, but I encountered some crashes and I am not sure why. During this process I encounterd a term called "module", which isolates unreal classes into modules and helps with code management. there are quite some configurations with files other than C++ files, which makes me realize I dont really know much about all the files in an unreal project. so heres my note on unreal project folder structures and what does each file do
[Reference](https://docs.unrealengine.com/5.3/en-US/unreal-engine-directory-structure/)

## The **Unreal Engine** Folder
### `Engine`
- all source code, contents, etc that makes up the unreal engine
### `GenerateProjectFiles.bat`


## The **Project** Folder
### `Derived Data Cache`
- derived data files generated on-load for referenced content (to reduce load time)
### `Intermediate`
- temporary files generated during building the engine or game (like shaders)
### `Saved`
- Autosaves, configurations and logs, etc
### `Config`
- contains`.ini` files related to the **project** and **editor** itself.
- can be edited interactively in Unreal editor settings
### `Content`
- the content folder we see in unreal editor asset management
### **`Source`**
- Source code of the game (organized by module)
- each module contains:
  - `Public` module header file (inter-module interface)
  - `Private` module source cpp file (source code)