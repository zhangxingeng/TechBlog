Title: Algorithmic Trading Notes
Date: 06-02-2023 19:05:50
Modified: 06-02-2023 19:05:50
Authors: Xingeng Zhang
Category:
Tags:
Slug:
Summary:

## Terms
### SMA
- Simple Moving Average: $SMA = \frac{A_1 + A_2 + \cdots + A_n}{n}$
- n: total period number; $A_k$ data at period k
### EMA
- Exponential Moving Average: $\mathcal{f}(n) = m \cdot A_n + (1-m)\cdot f(n-1)$
- $m$ is the contribution weight for current data
- $1-m$ is the weight for historical data
- EMA can be tuned to be more/less sensitive to current data (by changing $m$)

### z-score
- ![](images/z_score_example.png)
- 

## Strategies
- MACD oscillator:
  - Moving average Convergence/Divergence.
  - $MACD = EMA(12 day) - EMA(26 day)$
  - MACD signal Line: $MACD_{signal} = EMA(9 day)$
  - Macd Histogram: $MACD_{histo} = MACD - MACD_{signal}$
  - Meaning: 
    - when MACD > 0: short term estimate larger than long term (new data is contributing to the growth) -- Its probabily a good time to buy
    - vice versa
  - ![](images/MACD_Example.png)

- 