---
date: 2023-11-18
title: "Unreal - Part 2: Environment Setup"
---
### Install VS2022 Community edition
- Download exe from official website, install. You will get a **Visual Studio Installer**
- In the installer **workloads** tab, select:
  - .Net desktop development
  - Desktop development with C++
  - Universal Windows Platform development
  - Game development with C++
    - In the optional dropdown, select Windows 11 SDK, latest
    - Unreal Engine installer
    - IDE support for Unreal Engine
  - click install
### Install Unreal Engine
- download Epic Game launcher
- Inside launcher install unreal engine latest version

### Intergrate VS with Unreal
- In Epic games, marketplace, search for **Visual Studio Intergration Tool**, install to Unreal engine
- Launch the engine and create a project.
- Once unreal editor is open, go to **edit - plugins**
- Search for Visual studio Intergration tool (just installed) and make sure it is ticked
- ![Check Ticked](images/vs_unreal_intergration_tool_addon.png)
- In VS, [install the UnrealVS Extension](https://docs.unrealengine.com/5.3/en-US/using-the-unrealvs-extension-for-unreal-engine-cplusplus-projects/)
- [Some tweaks on VS for ease of use](https://docs.unrealengine.com/5.3/en-US/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine/)

### How to Use
- After all is setup, you should be able to:
  - build the game from unreal engine
  - When **Only** VS is open, build the game from VS (Unreal Live Coding prevent build)
  - Unreal context should be recognized and there should be no build error.