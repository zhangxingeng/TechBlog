---
date: 2024-01-22
title: "Unreal - Part 7: When to use Pointer and when to use reference"
---
Before I even explain anything lets dive into the example:
```cpp
  ULocation* GetLocationByName(const FString& LocationName) const;  // Changed return type
  const TArray<ULocation*>& GetLocationsList() const;  // Changed return type
```
- Here are two functions, one is returning a pointer `*`, the other reference `&`
- Firstly Pointers are not managed while reference are
- In other words, what you point to are just memory while the reference will be kept alive until you finished using
- We use `*` when the code is trying to get an element, so nullptr means no element found
- But when you try to create something then `&` is more apporiate, because create something guarantees something, nullptr does not make sense

