---
date: 2023-11-18
title: "Unreal - Part 3: Basic Unreal Knowledge"
---
## Important Components of a Game
### Subclass vs Inheritance
- Subclass is extension of a given class
- inheritance is a hierarchical relationship
### Level
- A container that holds game assets
- A scene or map where gameplay takes place
- Class: `ULevel` subclass of `UObject`
- Each level will have a World settings, it will be loaded into the world (`UWorld`) when current level is active
### GameMode
- Define the rules and structure of a game
- class `AGameMode` is a subclass of `AGameModeBase` which inherits from `AActor`
### `UWorld`
- As name suggests, it is the world a game resides in, each game have one.Levels are activated within the world
- Its like the OS and levels are like processes (except only one level is allowed at any time)
- More of a background process, generally programmers don't interact with it.

### PlayerController
- The User-Game interface, handles input to game actions
- Player Controller "possesses" pawns.
- `APlayerController` is a subclass of `AController`
- There is also a AI controller`AAIController` to use AI to control pawns

### Widgets
- designed with UMG UI Designer
- Used for Menus, HUDs, Inventories, dialogues and other UI elements
- Widgets can be attached to actors other than the player to show in 3d space (like health bar of NPC)

### Blueprint and CPP classes
- Blueprints are compiled Just-In-Time for rapid development, its compiled into a bytecode less efficient than C++.
- Usually implement core system using C++ and interface those system with the world using blueprint