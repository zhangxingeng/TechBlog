---
date: 2023-11-17
title: "Unreal - Part 1: the Big Picture"
---

## How Game Engine Runs
### Engine Prep
- **Plane Analogy**: Think game engine as a plane and its crew / flight attendant, while the game logics are the passengers.
- **Game/Engine Startup**: First Init Core System. Example: setup memeory management system; load all game related configurations (Settings of a game are stored in `ini` files); prep core subsystems like rendering engine, audio system, input system, etc. (check fuel, check food, pilot prep the plane)
- **Game Init**: After the engine is ready, the game-specific logic then begins. This includes load the init level, run the game-wise init functions (passengers boarded and settled)

### Level Prep
- **Load Game Level**: load all assets of a level like texture, mesh, sound, etc. Actors and Objects are also spawned (passangers boarding)
- ** BeginPlay Event **: Once all Objects are loaded, BeginPlay event (all actors have one) will be triggered (all passangers listen to safty and fasten seat belt) Notice BeginPlay event is like the constructor of an Object, it serve as a object state initializer.


- **The Game Loop**: a hugo loop, run until Level is destroyed. (Plane flying, flight attendant handles their needs and emergencies)
    - **Each Iteration is a \'Frame\'**: For each loop events are handled, including: input processing, Actor's Tick running, Physics simulation, Animations, sounds, rendering, etc. 
    - **Post-Processing**: after applying post-processing effects to rendered image, it will be drawn to the screen.
    - **Resource Mangement**: memory are recycled for unused assets before next iteration.

### Class Structures
<!-- - <iframe height='500' scrolling='yes' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%' src="https://app.creately.com/d/fZknuArLuyk/view"></iframe> -->
- ![Class Structure](images/unreal_class_structure.png)
- [View Interactive version](https://app.creately.com/d/fZknuArLuyk/view)
#### Root Structure
- `UObject`: base class for all objects in unreal. Garbage collection is implemented here
    - `AActor`: object placeable in the world (level). It contains - and nothing else. Which means it dont have a transform in the world - its componenet could have a transform. (when you place an 'actor' in the world, you are actually place the component, wrapped by Actor) Detail in [Actor Subclasses](#actor-subclasses)
    - `UActorComponent`: Base class for objects placed in AActor. (check previous). Notice this is a generic class for all components, no transform implemented at this level.
        - `USceneComponent`: actually appear in the world (have transform). for componenent that need to have transform information - like camera, or audio component.
            - `ULightComponentBase`: For lights
            - `UPrimitiveComponent`: Component with geometry. rendered. Collision tested
                - `UMeshComponent`: Any component with a renderable collection of triangles (mesh). Detail in [Mesh Component Subclasses](#mesh-component-subclasses)
                - `UShapeComponent`: represented by a simple geometrical shape (for collision shapes)
                  - `UBoxComponent`, `UCapsuleComponent`, `USphereComponent`: just shapes
    - `USubsystem`: elegant way to create managers (AI manager, Quest System, Audio Manager, etc) Instanced by engine. Share lifetime with its "logical parent". Example: `UWorld`'s manager: `UWorldSubsystem`. Only in C++.


#### Actor Subclasses
- `AActor`: generic (see previous section)
  - `AController`: non-physical actor (controls a `APawn`)
    - `APlayerController`: Human controlled
    - `AAIController`: AI controlled
  - `APawn`: have physical representation. possessed by `AController` (more generic, no complex movement logic)
    - `ACharacter`: specifically for humanoid that have a **character**. Have **built-in** support for animation with complex logics in different terrains. 
#### Mesh Component Subclasses
- `UMeshComponent`: generic mesh (see previous section)
  - `UStaticMeshComponent`: mesh that have no shape change during game
  - `USkinnedMeshComponent`: supports bone skinned mesh rendering
    - `USkeletalMeshComponent`: actual class used to create animated SkeletalMesh asset
  - `UWidgetComponent`: UI widget in 3D space.

