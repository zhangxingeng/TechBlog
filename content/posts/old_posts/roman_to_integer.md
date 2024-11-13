---
title: "roman_to_integer"
date: 2023-04-04T12:01:17-04:00
draft: true
---

### Related
- [Original problem](https://leetcode.com/problems/roman-to-integer/)
- 

### My idea
- Group I=1, II=2, III=3, IV=4
- Group V=5, VI=6, VII=7, VIII=8, IX = 9
- Group X=10, XX=20, XXX=30, XL = 40
- Group L=50, LX=60, LXX=70, LXXX=80, XC=90
- Group C=100, CC=200,CCC=300, CD=400
- Group D=500, DC=600, DCC=700, DCCC=800, CM=900
- Group M=1000, MM=2000, MMM =3000
- MAX= MMM-CM-XC-IX
- pattern: from right to left:
  ---
  - Last Letter I (type 1)
    - multiple I
    - V multiple I
  - Last Letter V (type 2)
    - IV, V
  ---
  - Last letter X (type 1)
    - IX
    - multiple X
    - L multiple X
  - Last Letter L (type 2)
    - XL, L
  ---
  - Last letter C (type 1)
    - XC
    - multiple C
    - D multiple C
  - Last Letter D (type 2)
    - CD, D
  - Last Letter M (type 2)
    - CM
    - multiple M
### Better Solution
- Notice How IV=V-I, VI = V+I
- All the letters follow this rule
- Thus we should consider a window two char at a time:
  - if (left < right, eg. IV): right - left (5-1)
  - if(left > right, eg. VI): right +left(5+1)
  - if(left == right, eg. II): right + left(1+1)
- We can slide the window from right to left and add or reduce base on this simple rule
- [Source](/static/cpp/roman_to_integer.cpp)
