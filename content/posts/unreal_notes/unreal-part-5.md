---
date: 2023-11-18
title: "Unreal - Part 5: More C++"
---
## C++ pass by reference
- Good Old C: pass a pointer:
  - could be null pointer and cause memory problem
- C++: Pass by reference:
  - reference is an alias for the original variable (compiler level reference, instead of Memory level reference)
  - This means the intergrity of the original variable is checked by the compiler to make sure it exists before entrust that part of the RAM with a pointer (notice how compiler creates the pointer now, instead of programmer directly access the memory)

## pass by reference
- in unreal if you do the following:
    ```cpp
    bool UMyItem::SetCount(int& NewCount){}
    ```
  You will get an output pin NewCount instead of input pin
- this is because unreal considers all reference parameters as the output of this function (design choice)
- The solution is to use `UPARAM(ref)` keyword
    ```cpp
    bool UMyItem::SetCount(UPARAM(ref)int& NewCount)
    ```
- Now blueprint would consider it as input pin as pass by ref type
- Notice Unreal's reflection system cannot check reference integrity like CPP compiler does, so its really the same as a pointer
- Potential NULL reference could occur and Unreal cannot tell you (remember, you are intergrating C++ with some ByteCode when you expose your C++ code to blueprint.)
- Conclusion: Just pass by value or pass by pointer!
