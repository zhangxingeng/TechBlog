---
title: "Isomorphic_string"
date: 2023-04-06T18:46:53-04:00
draft: true
---
- [details](https://leetcode.com/problems/isomorphic-strings)
### 1st Attempt (Skip This Part)
- My first thought would be to make a map that "translates" or "decrypts" first string into second string.
- But this idea does not ensure string 2 can be "translated" into string 1. 
- To solve this we can do map both strings, and make sure the map the map are the same size? 
- m1: {a:b, a:c, d:c}, m2= {c:a, c:d, b:a} same size but mapping is not unique (in m1 a map to 2 letters, and in m2 c map to 2 letters)
- So the only way would be make sure both map are the same by traverse
- Its obvious that big O wont be good.

- The next idea wo

### Approach
- The next thought would be: we can think of each loop in for loop as a state, all we need to do is to make sure that state is correct, let the future state to concern about themselves.
- What we could do is, use a big for loop to traverse all states, then handle each state seperately.
- The intuition would be to save current letter first then check if map is correct
 ```cpp
 // this is wrong code dont use
 for(int i = 0; i<len; ++i){
    m1[s[i]] = i;
    m2[t[i]] = i;
    if(m1[s[i]] != m2[t[i]]){
        return false;
    }
 }
 ```
- But think "foo" and "bar": for the first two loop m1 = {f:0, o:1} m2={b:0, a:1} everything is ok
- But for the third loop, since we are assigning value first then compare, we are overwritting m1: {o:1} ->{o:2} and create m2: {r: 2}, which is obviously incorrect
- Basically we are ignoring the fact that o is already in the system while r is first-timer, and overwritten them with the latest record
- What we should do instead, is to check these letters history first:
- still for "foo" and "bar" at 3rd loop: s1: {"o":1}, {r: not_exist} history shows that o is mapped to a letter at position 1 while r was never mapped before, thus return false.
  ```cpp
  for(int i = 0; i<len; ++i){
      if(m1[s[i]] != m2[t[i]]){
          return false;
      }else{
          m1[s[i]] = i+1; // explained below
          m2[t[i]] = i+1;
      }
  }
  ```
- You could notice we added 1 to the index, the reason can be seen with a simple example
- "aa" and "ab": if we save index i directly, for the 1st loop we will have: {a:0}, {a:0} for both maps
- Then for the 2nd loop we will have {a:0}, {b: not_exist}. here not_exist is represented as m2.end(). or '\0'.
- We know that '\0' == 0 which means for the 2nd loop if we compare 'a' and 'b', we will get ` 0 == m.end()`. Obviously not good, so we need to avoid 0 as a record entirely due to the nature of how C++ mark end with '\0'. nothing personal, zero. 

### Code
```
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int len = s.length();
        if(len != (int)t.length()){return false;}
        map<char, int> m1, m2;
        for(int i = 0; i<len; ++i){
            if(m1[s[i]] != m2[t[i]]){
                return false;
            }else{ // rememeber the updated position only (at current state, previous states are checked valid)
                m1[s[i]] = i+1; // since 0 == '\0', when m1['a'] = 0 and m2['b'] does not exist (returns m2.end()=='\0') should return false but return true thus add 1 to all index to avoid 0
                m2[t[i]] = i+1;
            }
        }
        return true;
    }
};
```

