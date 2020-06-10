## 1185. Day of the Week
- Today `today = datetime.datetime.today()`

- One specific time `date = datetime.datetime(year, month, day)`

- Get weekday `today.weekday()`


## 231. Power of Two
- Bitwise operation: &, |, ^, ~, <<, >>
- The difference between `not` and `~`: `not` is a logic negative and `~` is a bitwise negative.

    Here is the situation: `not n`, if n is any number other than 0, it will be False, and if n is 0, then it will be True.
    
    `~ n`, it will reverse every bit of n, including the bit representing the sign. So only `~-1` will be 0, others will be differnent numbers. 
    
    So, if in this problem, I should use `not` other than `~`.

## 2. Add Two Numbers
- Ternary conditional operator(三目运算符）

    `a if condition else b`: a is returned when condition is true, else b is returned.
- Division in Python
    `/` is the exact division, `//` is the downward division, `%` is the modulus.
    
    `round` can round off, round down and round up: `math.floor, math.ceil`
