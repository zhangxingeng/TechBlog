---
title: "Notes on ml statistics"
date: 2024-04-01
---

- binomial distribution & normal/beta distribution
- First Normal distribution is a special case of the Beta distribution when a=b

- central limit theorem: 
  - **regardless** of distributions, if
    - 1. the distribution have a **finite** mean and variance; 
    - 2. trail results from that distribution are **independent**;
  - then if we look at the distribution of **the sum of the results**; 
    - (not the result themselves which is already known) will:
    - We see that it always approximate a normal distribution.
  - This explains why symmetric binomial distribution always resembles a bell curve (): 
    - because: 
      - 1. the bernoulli trials are independent;
      - 2. the mean and variance (of bernoulli) is finite.
- Check out this video for more https://youtu.be/FdnMWdICdRs?si=zESXyxRktP3h2FsW
