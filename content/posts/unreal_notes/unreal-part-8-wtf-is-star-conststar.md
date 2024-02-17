---
date: 2024-01-22
title: "Unreal - Part 8: WTF is `*const*`?
---
### const pointer vs pointed to is const
- const pointer to a int: `int* const ptr`
- point to a const int: `const int* ptr`

### stacking consts with pointers
- non-const pointer to non-const object: `ULocation*`
- non-const pointer to a const object: `const ULocation*`
- const pointer to a const object: `const ULocation* const`
- pointer to above: `const ULocation* const*`


### Conclusion
since variables have const in front and function have const at back, pointer is more like a function in case of const position