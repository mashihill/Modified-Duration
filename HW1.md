Financial Computing HW1 
=======================

## Code explanation

**Function**: 
- `mdcv(y, c, w)`
**Inputs**: 
- `y` = interest rate,
- `c` = cash flow,
- `w` = as defined in class
**Outputs**:
- Modified duration
- Convexity


## How to run (examples):
```python
$ python 
>>> from HW1 import mdcv 
>>> mdcv(0.05, [1,2, 3,101], 0.5)
Modified duration = 3.2356006252
Convexity = 13.7299656004
>>> mdcv(0.08, [10, 10, 10, 10, 10 ,110], 1)
Modified duration = 4.4883792444
Convexity = 26.9005563975
>>>
```

Link: [Homework description](http://www.csie.ntu.edu.tw/~lyuu/finance1.html)

R03246004 陳彥安
