---
date: 2023-11-18
title: "Unreal - Part 4: Basic Unreal C++"
---
## Unreal's Reflection System
- How does unreal editor seamlessly read and write your custom C++ classes? -- the reflection system!
- It gathers metadata about your class like variable names, types, and special attributes (using macros like UCLASS(), UPROPERTY(), UFUNCTION(), etc.)
- Uses Unreal Header Tool (UHT) to intergrate with C++ classes (the `#include *.generated.h`)
- Its like a god mode for unreal editor


## A minimal Unreal class implemented in C++
- Inherit `UObject` when Non-physical, and `AActor` when have a collision or mesh (exist in 3d physical world)
- The header file
```cpp
// UMyItem.h
#pragma once // Ensure the header is only included once during compilation
#include "CoreMinimal.h" // Essential Unreal Engine types and macros
#include "UObject/Object.h" // Base class for all UObject classes
#include "MyItem.generated.h" // For Unreal Header Tool (UHT) generated code

/**
 * Simple inventory item class.
 */
UCLASS(Blueprintable) // Class can be used to create Blueprints
// EXAMPLEGAME_API: UHT keyword indicating project this class belongs to is ExampleGame
class EXAMPLEGAME_API UMyItem : public UObject {
    GENERATED_BODY() // Macro to support Unreal's reflection system

private:
    // Private variable for item count
    int Count;

public:
    // Constructor declaration
    UMyItem();

    // EditAnywhere: can be edited by unreal editor
    // BlueprintReadWrite: can be read and write by a blueprint
    // Category="Item": what is this? 
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Item")
    FString Name;

    // Getter and setter for Count
    // getter is pure function, indicated by const keyword
    UFUNCTION(BlueprintCallable, Category="Item")
    int GetCount() const; // Make const if it doesn't modify the object

    UFUNCTION(BlueprintCallable, Category="Item")
    bool SetCount(int NewCount);
};
```
- The cpp file
```cpp
// UMyItem.cpp
#include "UMyItem.h"

// Constructor definition
// Count(0): C++ init short hand, init Count to 0
UMyItem::UMyItem() : Count(0) {/* Other Init stuff here */}

// GetCount function definition
int UMyItem::GetCount() const {
    return Count;
}

// SetCount function definition
bool UMyItem::SetCount(int NewCount) {
    if (NewCount >= 0) {
        Count = NewCount;
        return true;
    }
    return false;
}
```
- what is the `Category` keyword:
- For better viewing in unreal editor:
- ![category keyword](images/unreal_cpp_category_keyword.png)