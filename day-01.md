# Day 01

(July 30, 2024)

Today I've acquired this knowledge

* Comment
* Data Types

## Comment

```python
# Single line comment

"""
Multiple
line
comment
"""
```

## Data types

### Numbers

There are 2 kind of numbers in Python: integer, float

```python
# integer
tax = 20

# float
buy_price = 1.68

# you can declare multiple variables on a single line, separated by commas
sell_price, sold_amount = 1.99, 2123

co = buy_price * sold_amount
revenue = sold_amount * sell_price
profit_before_tax = (sell_price - buy_price) * sold_amount
profit_after_tax = profit_before_tax - (profit_before_tax * tax / 100)

print(str.format("CO: ${0:,.2f}", co))
print(str.format("Revenue: ${0:,.2f}", revenue))
print(str.format("Profit before tax: ${0:,.2f}", profit_before_tax))
print(str.format("Profit after tax: ${0:,.2f}", profit_after_tax))

# CO: $3,566.64
# Revenue: $4,224.77
# Profit before tax: $658.13
# Profit after tax: $526.50

latitude = 20.577180620745487
longitude = 106.04136437153396
print(f"Geopoint is {latitude}, {longitude}")
# Geopoint is 20.577180620745487, 106.04136437153396

# classic division / always return a float
print(6 / 2) # 3.0
print(9 / 5) # 1.8

# floor division // discards the fractional part
print(6 // 3) # 2
print(6 // 4) # 1

# % operator returns the remainder of the division
print(6 % 3) # 0
print(6 % 4) # 2

# use ** to calculate the powers
print(4 ** 4) # 256
print( 2 ** 7) # 128

```

### String

```python
name = "Tuan"
# character in position 0
print(name[0]) # T
# last charactor
print(name[-1]) # n
# second last charactor
print(name[-2]) # a
# charactor from position 0 (included) to 2 (excluded)
print(name[0:2]) # Tu
# charactor from position 1 (included) to 3 (excluded)
print(name[1:3]) # ua
# charactor from beginning to 2 (excluded)
print(name[:2]) # Tu
# charactor from 2 (exclude 2) to the end
print(name[2:]) # an

# Python string cannot be changed, they are immutable, therefore assigning to an indexed position in the string result in an error
name[0] = "H" # error
# Traceback (most recent call last):
#   File "/home/runner/RockPaperScissors/main.py", line 2, in <module>
#     name[0] = "H"
# TypeError: 'str' object does not support item assignment

# concat string
greeting_one = "Hello " + name
greeting_two = str.format("Hello {0}", name)
concat_string = f"Hello {name}"
print(greeting_one)
print(greeting_two)
print(concat_string)
# Hello Tuan
# Hello Tuan
# Hello Tuan

# string methods
greeting_three = str.format("Hello {0}", name.upper())
print(greeting_three)
print(greeting_three.split(" "))

# Hello TUAN
# ['Hello', 'TUAN']

# you need to cast data to string before concat
age = 30
greeting_f_our = "Hello " + name + ", age: " + str(age)
# but you can use str.format to concat other data type into string
greeting_five = str.format("Hello {0}, age: {1}", name, age)

# split line
print("Multiple\nline\n\tstring")
# Multiple
# line
#     string

```

### Boolean

It have 2 value: True/False

```python
exceeded_quota = True
published = False

# negative with not
new_value = not exceeded_quota # False

# Boolean Operators
True & True # True
True and True # True
False & True # False
False and True # False

# True/False is 1 and 0 but with different keywords
True + True # 2
True + False # 1
True * 8 # 8
False - 5 # -5
True - 5 # -4

# comparision operators look at the numerical value of True and False
0 == False # True
1 == False # False
1 == True # True
0 == True # False
2 > True # True
2 >= True # True
2 != True # True

# None, 0, and empty strings/list/dics/tuples/sets all evaluate to False
# All other values are True
print(bool(None)) # False
print(bool(0)) # False
print(bool("")) # False
print(bool([])) # False
print(bool({})) # False
print(bool(())) # False
print(bool(set())) # False

# int
print(bool(5)) # True
# string
print(bool("tuan")) # True
# list
print(bool(["tuan", "nguyen"])) # True
# dics
print(bool({"foo": "bar"})) # True
# tuple
print(bool((1, 2, 3, 4, 5))) # True
# set
print(bool({120, 120, 10, 30})) # True

```

### Lists

```python
day_of_weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

```
