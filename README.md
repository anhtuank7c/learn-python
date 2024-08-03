# Learn Python

I use this repo to track all the lessons I learned about python

## Reference documents

* https://www.w3schools.com/python/default.asp
* https://learnxinyminutes.com/docs/python/
* https://docs.python.org/3/tutorial/index.html
* https://www.youtube.com/watch?v=eWRfhZUzrAc&t=386s

## Online playground tools

* https://programiz.pro/ide/python
* https://replit.com

## Main content

### Comment

```python
# Single line comment

"""
Multiple
line
comment
"""
```

### Data types

#### Numbers

There are 2 kind of numbers in Python: integer, float

```python
# integer
# -2, -1, 0, 1, 2, 3, 4, 5
tax = 20

# you can use underscore to make readable number
salary = 100_000_000_000 # 1000000000
print(f"{salary: _}") # 100_000_000_000
print(f"{salary: ,}") # 100,000,000,000

# float
# -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25
buy_price = 1.68

# you can use underscore to make readable number
income = 88_000_000.123_456 # 88000000.123456
print(f"{income: _.2f}") # 88_000_000.12
print(f"{income: ,.6f}") # 88,000,000.123456

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
print(f'4 ** 4 = {4 ** 4}') # 4 ** 4 = 256
print(f'{4 ** 4 = }') # 4 ** 4 = 256

print(2 ** 7) # 128
print(f'2 ** 7 = {2 ** 7}') # 2 ** 7 = 128
print(f'{2 ** 7 = }') # 2 ** 7 = 128

# casting data using `int(), float()` methods
int("123") # <class 'int'>
float("123.123") # <class 'float'>

# check type
type(12) # <class 'int'>
type(3.14) # <class 'float'>
```

#### String

```python
address = 'Halong Bay, Quang Ninh, Vietnam'
name = "Tuan"
# find lenght of a string
len(name) # 4

# string can be treated like a list characters
# character in position 0
print(name[0]) # T
# last character
print(name[-1]) # n
# second last character
print(name[-2]) # a
# character from position 0 (included) to 2 (excluded)
print(name[0:2]) # Tu
# character from position 1 (included) to 3 (excluded)
print(name[1:3]) # ua
# character from beginning to 2 (excluded)
print(name[:2]) # Tu
# character from 2 (exclude 2) to the end
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

# pad string
name = 'TUAN'
print(f'{name:_<10}') # TUAN______
print(f'{name:_>10}') # ______TUAN
print(f'{name:_^10}') # ___TUAN___

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

# casting data using `str()` method
str(123) # <class 'str'>
str(123.123) # <class 'str'>
str("123") # <class 'str'>

# check type
type("Hello world") # <class 'str'>
```

#### Boolean

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

# equality is ==
1 == True # True
1 == 1 # True
0 == True # False

# inequality is !=
1 != True # False
1 != False # True
1 != 0 # True

# More comparision
1 < 10 # True
1 > 10 # False
1 <= 10 # True
1 >= 10 # False

# Seeing whether a value is in a range
1 < 2 and 2 < 3 # True
2 < 3 and 3 < 2 # False
# Chaining make this look nicer
1 < 2 < 3 # True
2 < 3 < 2 # False

# is vs ==
# is check if 2 variables refer to the same object
# == check if the objects pointed to the same value
list_one = [1, 2, 3, 4]
list_two = list_one

list_two is list_one # True, list_one and list_two point to the same object
list_two == list_one # True, list_one and list_two are equal because they have the same value

list_three = [1, 2, 3, 4]

list_three is list_one # False, list_three is not point to the same object as list_one
list_three == list_one # True, list_three and list_one have the same value

# check type
type(True) # <class 'bool'>
```

#### None

None is an object

```python
None  # None

# Don't use the equality `==` to compare objects to None
# Use `is` instead. `is` check for equality of object identity

"etc" is None # False
None is None # True

# check type
type(None) # <class 'NoneType'>
```

#### Lists

List store sequences

```python
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_of_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# append element
days_of_week.append("Lazy")

append_result = days_of_month.append(31) # None
print(days_of_month) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# remove from the end with pop
pop_result = days_of_month.pop() # 31

print(days_of_month) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# access a list like you would any array
days_of_month[0] # 1

# look at the last element
days_of_month[-1] # 30

# looking out of bounds is an IndexError
days_of_month[50] # IndexError: list index out of range

# You can look at ranges with slice syntax.
# the start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
days_of_month[1:3] # return list from 1 (excluded) to 3 (included) => [2, 3]
days_of_month[28:] # return list from 28 (excluded) to the end => [29, 30]
days_of_month[:3] # return list from beginning to index 3 (excluded) => [1, 2, 3]
days_of_month[::3] # return list selecting elements with a step size of 3 => [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
days_of_month[::-1] # return list in reverse order => [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# make one layer deep copy using slices
days_of_month_copy = days_of_month[:]

# remove arbitrary elements from a list with `del`
del days_of_month[0] # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# remove first occurrence of a value, raise ValueError if absent
list_with_duplicate_value = [1, 2, 3, 4, 5, 4, 3, 8]
list_with_duplicate_value.remove(4) # [1, 2, 3, 5, 4, 3, 8]
list_with_duplicate_value.remove(100) # ValueError: list.remove(x): x not in list

# insert an element at a specific index
list_with_duplicate_value.insert(2, 100) # [1, 2, 100, 3, 4, 5, 4, 3, 8]

# get the index of the first item found matching the argument, raise ValueError if absent
list_item = ["Apple", "Banana", "Peach", "Guava", "Avocado", "Peach"]
list_item.index("Peach") # 3
list_item.index("Peachy") # ValueError: 'Peachy' is not in list

# use `+` to add multiple list to make a new list, original list will not being modified
list_poultry = ["Chickens", "Ducks", "Turkeys", "Geese", "Quails", "Pheasants", "Pigeons", "Ostriches"]
list_cattle = ["Wagyu", "Kobe beef", "Ohmi beef", "Hanwoo beef", "Kurobuta Pork", "Olive Sanuki Wagyu"]
list_animal = list_poultry + list_cattle + list_poultry

# concatenate list with `extend`, the extender list will be modified
list_poultry.extend(list_cattle)
print(list_poultry)
# ['Chickens', 'Ducks', 'Turkeys', 'Geese', 'Quails', 'Pheasants', 'Pigeons', 'Ostriches', 'Wagyu', 'Kobe beef', 'Ohmi beef', 'Hanwoo beef', 'Kurobuta Pork', 'Olive Sanuki Wagyu']
print(list_cattle) # ["Wagyu", "Kobe beef", "Ohmi beef", "Hanwoo beef", "Kurobuta Pork", "Olive Sanuki Wagyu"]

# check for existence in a list with `in`
"Chickens" in list_poultry # True

# examine the length with `len()`
len(list_poultry) # 8

# You can put multiple data types into the same list without hassle
list_mixed = ["Mon", 2, "Tue", 3, "Wed", 4, "Thu", 5, "Fri", 6, "Sat", True, "Sun", False]

# unpack lists into variables
data = [["Blog", "Service"], ["Post 01", "Post 02"], ["Author 01", "Author 02"]]
categories, posts, authors = data
print(categories) # ['Blog', 'Service']
print(posts) # ['Post 01', 'Post 02']
print(authors) # ["Author 01", "Author 02"]

# extended unpacking (or spreading)
*rest, authors = data
print(rest) # [['Blog', 'Service'], ['Post 01', 'Post 02']]
print(authors) # ['Author 01', 'Author 02']

categories, *rest = data
print(categories) # ['Blog', 'Service']
print(rest) # [['Post 01', 'Post 02'], ['Author 01', 'Author 02']]

categories, *rest, authors = data
print(categories) # ['Blog', 'Service']
print(rest) # [['Post 01', 'Post 02']]
print(authors) # ['Author 01', 'Author 02']

# check type
type(list_mixed) # <class 'list'>
```

#### Tuple

Tuple is like lists but are immutable

```python
user_info = ("Tuan", 35, "Halong Bay, Quang Ninh, Vietnam", True)
user_info[0] # Tuan
user_info[0] = "Quan" # TypeError: 'tuple' object does not support item assignment

# check type
# tuple of needs a comma if have elements
type(("Tuan", )) # <class 'tuple'>
type(("Tuan", True)) # <class 'tuple'>

# empty tuple don't need comma
type(()) # <class 'tuple'>

# without comma, it will never consider as tuple
type(("Tuan")) # <class 'str'>
type((1)) # <class 'int'>
type((3.14)) # <class 'float'>
type((True)) # <class 'bool'>

# you can do most of the list operations on tuples too
len(("Tuan", True)) # 2

book = ("Harry Porter", 2002, "Published")
author = ("JK Rowling", 1965, "Female", "England")
book_author = book + author # ('Harry Porter', 2002, 'Published', 'JK Rowling', 1965, 'Female', 'England')
book[:2] # ('Harry Porter', 2002)
book[:-1] # ('Harry Porter',)
book[::2] # ('Harry Porter', 'Published')
book[2:] # ('Published',)
book[1:2] # (2002,)
"England" in author # True

# You cannot extend a tuple
author.extend(book) # AttributeError: 'tuple' object has no attribute 'extend'

# Unpack tuples into variables
name, published_year, status = book

# extended unpacking
address = ((20.951826295025008, 107.01421196125972), "Halong Bay, Quang Ninh, Vietnam", 200000, "+84123456789")

geopoint, *rest, phone = address
print(geopoint) # (20.951826295025008, 107.01421196125972)
print(rest) # ['Halong Bay, Quang Ninh, Vietnam', 200000]
print(phone) # +84123456789

*rest, phone = address
print(rest) # [(20.951826295025008, 107.01421196125972), 'Halong Bay, Quang Ninh, Vietnam', 200000]
print(phone) # +84123456789

geopoint, *rest = address
print(geopoint) # (20.951826295025008, 107.01421196125972)
print(rest) # ['Halong Bay, Quang Ninh, Vietnam', 200000, '+84123456789']

# tuple are created by default if you leave out the parentheses
name, age = "Tuan", 35 # tuple Tuan, 35 is unpacked into variables name, age
print(name) # Tuan
print(age) # 35

# now look how easy it is to swap two values
age, name = name, age
print(name) # 35
print(age) # Tuan
```

#### Dictionary

Dictionary store mappings from keys to values

```python
empty_dict = {}
languages = {"en": "English", "vi": "Vietnamese"}

# keys for dictionaries have to be immutable types to ensure key can be converted to a constant hash value for quick look-ups.
# immutable types include ints, float, string, tuples
valid_dict = {100: "Very good", 90: "Good", 70: "Acceptable", 60: "Under average"}
valid_dict = {3.14: "Pi"}
valid_dict = {"cached": "total: 10, ranked 100"}
valid_dict = {("Tuan", 35): [10000, 3.141592654]}

invalid_dict = {[100, 200]: "salary"} # TypeError: unhashable type: 'list'
invalid_dict = {{"en": "English"}: "salary"} # TypeError: unhashable type: 'list'

# look up values with []
leaderboard = {1: ["Tuan", "Simon"], 2: ["Duong", "Chien"], 3: ["Truong"], 4: ["Son"], 5: ["Phuong"]}
print(leaderboard[1]) # ['Tuan', 'Simon']
print(leaderboard[3]) # ['Truong']

# get all keys as an iterable with "keys()". We need to wrap the call in list() to turn it into a list
# Note:
# - For python version < 3.7: dictionary key ordering is not guaranteed
# - For python version >= 3.7: dictionary items maintain the order at which they are inserted into the dictionary
values = list(leaderboard.values())
# [['Tuan', 'Simon'], ['Duong', 'Chien'], ['Truong'], ['Son'], ['Phuong']]

# check for existence of keys in a dictionary with `in`
languages = {
  "en": "English",
  "vi": "Vietnamese"
}
"en" in languages # True

# looking up for non-existing key is a KeyError
languages["de"] # KeyError: 'de'

# use `get()` method to avoid the KeyError
languages.get("vi") # Vietnamese
languages.get("de") # None

# `get()` method support default value when the value is missing
languages.get("de", "German") # German

# `setdefault()` inserts into a dictionary only if the given key is absent
languages.setdefault("de", "German")
languages.setdefault("en", "France")
# {'en': 'English', 'vi': 'Vietnamese', 'de': 'German'}

# adding to a dictionary 
languages.update({"zh": "Chinese"}) # {'en': 'English', 'vi': 'Vietnamese', 'de': 'German', 'zh': 'Chinese'}
languages.update({"en": "France"}) # {'en': 'France', 'vi': 'Vietnamese', 'de': 'German', 'zh': 'Chinese'}
languages["en"] = "English" # {'en': 'English', 'vi': 'Vietnamese', 'de': 'German', 'zh': 'Chinese'}

# remove keys from a dictionary with del, raise KeyError if key is absent
del languages["zh"]
del languages["absent_key"] # KeyError: 'absent_key'

# from python 3.5 you can also use the additional unpacking options
languages = {"en": "English", **{"zh": "Chinese"}} # {'en': 'English', 'zh': 'Chinese'}

# check type
print(type(languages)) # <class 'dict'>
```

#### Set

Set is an unordered collection of unique and immutable elements.

Set is commonly used for membership testing, eliminating duplicate entries, and performing mathematical set operation like `union`, `intersection`, and `difference`.

```python
# init an empty set
empty_set = set()

# init a set from a list
list_duplicated_values = [1, 1, 2, 2, 3, 3]
unique_values = set(list_duplicated_values) # {1, 2, 3}

# init a set with a bunch of values
some_set = {1, 1, 2, 3, 2, 5} # {1, 2, 3, 5}

days_of_week = {"Mon", "Tue"} # {'Tue', 'Mon'}

# Note elements of a set have to be immutable.
# Immutable types include ints, floats, strings, tuples, frozensets.
# other data types will raise error TypeError: unhashable type
new_set = {[1, 2]} # TypeError: unhashable type: 'list'
new_set = {{"foo": "bar"}} # TypeError: unhashable type: 'dict'

# tuple
new_set = {("Wed", "Tue")} # {('Wed', 'Tue')}
# string
new_set = {"Wed", "Tue"} # {'Wed', 'Tue'}
# int
new_set = {1, 2} # {1, 2}
# float
new_set = {3.14, 1,234} # {3.14, 234, 1}
# frozenset
new_set = {frozenset([1, 2, 3])} # {frozenset({1, 2, 3})}

mixed_set = {1, 2.2, "three", (4, 5), frozenset([6, 7])}

# add elements, duplicate entries will automatically eliminated
days_of_week.add("Wed") # {'Wed', 'Tue', 'Mon'}
days_of_week.add("Wed") # {'Wed', 'Tue', 'Mon'}

# remove elements using `remove()` or `discard()` methods.
# `remove()` will raise KeyError if remove an absent element
# `discard()` will never raise error
days_of_week.remove("Wed") #{'Tue', 'Mon'}
days_of_week.remove("Wed_asjdhas") # KeyError: 'Wed_asjdhas'

days_of_week.discard("Tue") #{'Mon'}
days_of_week.discard("Wed_asjdhas") # Nothing happen

# union is the way to merge 2 sets and also remove the duplicates
# use `union()` method or `|` operator
days_of_week_one = {"Mon", "Tue", "Web"}
days_of_week_two = {"Web", "Thu", "Fri", "Sat", "Sun"}
days_of_week = days_of_week_one.union(days_of_week_two) # {'Web', 'Sat', 'Mon', 'Sun', 'Fri', 'Tue', 'Thu'}

days_of_week = days_of_week_one | days_of_week_two # {'Web', 'Sat', 'Mon', 'Sun', 'Fri', 'Tue', 'Thu'}

# intersection is the way to find elements that found in both sets
# use `intersection()` or `&` operator
days_of_week_one = {"Mon", "Tue", "Web"}
days_of_week_two = {"Web", "Thu", "Fri", "Sat", "Sun"}

days_appeared_in_both_sets = days_of_week_one.intersection(days_of_week_two) # {'Web'}
days_appeared_in_both_sets = days_of_week_one & days_of_week_two # {'Web'}

# difference is the way to find elements that appear in the first set but not in the second
# use `difference()` method or `-` operator
days_of_week_one = {"Mon", "Tue", "Web"}
days_of_week_two = {"Web", "Thu", "Fri", "Sat", "Sun"}

days_difference_from_set_two = days_of_week_one.difference(days_of_week_two) # {'Tue', 'Mon'}
days_difference_from_set_two = days_of_week_one - days_of_week_two # {'Tue', 'Mon'}

# symmetric difference between two sets contains elements that are in either of the sets but not in both.
# use `symmetric_difference()` or `^` operator
days_of_week_one = {"Mon", "Tue", "Web"}
days_of_week_two = {"Web", "Thu", "Fri", "Sat", "Sun"}

symmetric_difference = days_of_week_one.symmetric_difference(days_of_week_two) # {'Fri', 'Mon', 'Sat', 'Tue', 'Thu', 'Sun'}
symmetric_difference = days_of_week_one ^ days_of_week_two # {'Fri', 'Mon', 'Sat', 'Tue', 'Thu', 'Sun'}

# a set is a subset of another if all elements of the first set are in the second
# use `issubset()` or `<=` operator
days_of_week = {2, 3, 4, 5, 6, 7, 8}
days_of_month = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}

days_of_week.issubset(days_of_month) # True
days_of_week <= days_of_month # True

# a set is a superset of another if it contains all elements of the second set.
# use `issuperset()` or `>=` operator
days_of_month.issuperset(days_of_week)
days_of_month >= days_of_week

# Make a one layer deep copy using the `copy()` method
days_of_week_copy = days_of_week.copy()

# remove all elements from a set using the `clear()` method
days_of_week.clear() # set()

# add multiple elements to a set using the `update()` method
days_of_week = {2, 3, 4, 5, 6, 7, 8}
days_of_week.update([1, 9, 10, 11]) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# check for existence in a set with `in`
2 in days_of_week # True

# a frozen set is an immutable version of a set.
# elements cannot be added or removed after creation.
# using `frozenset()` method
new_set = {"Mon", "Tue"}
new_frozenset = frozenset(new_set)

days_of_week = frozenset(["Mon", "Tue"])
days_of_week.clean() # AttributeError: 'frozenset' object has no attribute 'clean'
days_of_week.update(["Wed"]) # AttributeError: 'frozenset' object has no attribute 'update'
days_of_week.add("Wed") # AttributeError
days_of_week.remove("Wed") # AttributeError
```

### Variables

Variable in Python is a name that refers to a value. Python is dynamically typed which mean you don't need to declare the variable type explicitely.

```python
# variable identifier must follow these rules
# - must start with a letter [a-z A-Z] or an underscore `_`
# - can be followed by letter, digits (0-9) or underscore `_`
# - case-sensitive (e.g myVar and myvar are different variables)
# - cannot be a reversed keyword (e.g if, while, for)

########################
# implicit declaration
########################
# int
age = 35
# float
pi = 3.14
# string
name = "Tuan"
# boolean
sold_out = True
# tuple
person = ("Tuan", 35, "Male", "Halong Bay, Quang Ninh, Vietnam")
# list
stables = ["Gothenburg, Sweden", "Paris, France", "Hanoi, Vietnam"]
# dict
languages = {"en": "English", "vi": "Vietnam"}
# set
product_ids = {"sku_01", "sku_02", "sku_01", "sku_03"}

########################
# explicit declaration
########################
age: int = 35
pi: float = 3.14
name: str = "Tuan"
sold_out: bool = True

########################
# variable scope
# local scope: variable declared inside a function are local to that function
# enclosing scope: variable in the local scope of enclosing function (nonlocal)
# global scope: variable declared at the top level of a script or module, or declared global using `global` keyword
# built-in scope: variable preassigned in the built-in namespace (e.g., `len`, `range`)
########################
# global variable
age = 30

def outer_function():
  # enclosing variable
  age = 50

  def inner_function():
    # local variable
    age = 100

    # global variable
    global name
    name = "Tuan"

    print(f'{age = }') # 100

  inner_function()
  print(f'{age = }') # 50

outer_function()
print(f'{age = }') # 30
print(f'{name = }') # Tuan

# `global` keyword allows you to modify a global variable inside a function
today = "Monday"

def modify_global():
  global today
  today = "Tuesday"
  print(f'{today = }') # today = 'Tuesday'

modify_global()
print(f'{today = }') # today = 'Tuesday'

# `nonlocal` keyword allows you to modify a variable in the enclosing (non-global) scope
def outer_func():
  name = "Tuan"

  def inner_func():
    nonlocal name
    name = "Simon"
    print(f'{name = }') # name = 'Simon'

  inner_func()
  print(f'{name = }') # name = 'Simon'

outer_func()

########################
# dynamic typing and type checking
# Python is dynamically typed, meaning that variable types are determined at runtime, variables can change type
########################
x = 10
print(type(x)) # <class 'int'>

x = "Hello world"
print(type(x)) # <class 'str'>

# dynamic typing offers flexibility, it can easily lead to runtime errors if not managed carefully (like Javascript).
# to enhance type safety, you can use type hints and tools like `mypy` for static type checking.
# don't forget to install mypy extension for your IDE for static type checking: https://www.mypy-lang.org
# vscode extension https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker
# IntelliJ IDEA, PyCharm https://plugins.jetbrains.com/plugin/11086-mypy
def greeting(name: str) -> str:
  return f'Hello {name}'
print(greeting("Tuan")) # Hello Tuan
print(greeting(1123)) # Mypy raise thise: Argument 1 to "greeting" has incompatible type "int"; expected "str"

# recommended to use pipx over pip: https://pipx.pypa.io/stable
# `pip install mypy` or `pipx install mypy`
# and run: `mypy your_file.py`

from typing import Tuple, List, Dict, Set

Person = Tuple[str, int, str, str]
person: Person = ("Tuan", 35, "Male", "Halong Bay, Quang Ninh, Vietnam")
print(person)

names: List[str] = ["Tuan", "Simon", "Duong", "Son"]
print(names)

scores: Dict[str, int] = {"Tuan": 10, "Simon": 9, "Duong": 8, "Son": 7}
print(scores)

days_of_week: Set[str] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
print(days_of_week)

########################
# constant
# while Python doesn't have a built-in constant type
# by convention, constant are written in uppercase letters and are typically defined
# at the module level
########################
PI = 3.141592654
MAX_CONNECTIONS = 500
LOGS_LEVEL = "debug"
LOGS_SIZE = 5 * 1000 ** 2 #MB

# immutable types includes: int, float, str, tulple, frozenset
# mutable types inclide: list, dict, set

# declare multiple variables at once by adding commas
name, age, address = "Tuan", 35, "Halong Bay, Quang Ninh, Vietnam"
```

### Control Flow & Iterables

#### Conditional statements

Conditional statements allow you to execute different blocks of code based on certain conditions.

```python
# if
is_raining = True
if is_raining:
  print("It's raining")

# if-else
humidity = 88
if humidity > 80:
  print("Possibility to rain")
else:
  print("No chance to rain")

# if-elif-else
if humidity >= 90:
  print("Surely rain")
elif humidity >= 80:
  print("Possibility to rain")
else:
  print("No chance to rain")

# switch-case
# Python does not have a built-in switch-case statement like other languages.
# However you can archive similar functionality using different approaches.
# 1. use if-elif-else statement
# 2. use dict
# 3. use lambda function in dict
# 4. use match-case (python 3.10+)

# solution 1: if-elif-else
def switch_case(value):
  if value == 1:
    return "case 01"
  elif value == 2:
    return "case 02"
  else:
    return "default case"

switch_case(1)
switch_case(2)
switch_case("Hi")

# solution 2: dict
def case_1():
  return "case 01"
def case_2():
  return "case 02"
def case_default():
  return "default case"
switch = {
  1: case_1,
  2: case_2
}
def switch_case(value):
  return switch.get(value, case_default)()

switch_case(1)
switch_case(2)
switch_case("Hi")

# solution 3: use lambda function in dict
switch = {
  1: lambda: "case 01",
  2: lambda: "case 02",
}
def switch_case(value):
  return switch.get(value, lambda: "default case")()

switch_case(1)
switch_case(2)
switch_case("Hi")

# solution 4: match-case (python 3.10+)
def switch_case(value):
  match value:
    case 1:
      return "Case 1"
    case 2:
      return "Case 2"
    case 3 | 4:
      return "Case 3 and 4"
    case _:
      return "Default case"

print(switch_case(1))  # Case 1
print(switch_case(3))  # Case 3 and 4
print(switch_case(4))  # Case 3 and 4
print(switch_case(5))  # Default case

```

#### Loop statements

Loop statements allow you to repeat a block of code multiple times

```python
# for: Iterates over a sequence (such as a list, tuple, dictionary, set, or string) and executes a block of code for each item.
fruits = ["Apple", "Peach", "Pear", "Banana", "Kiwi"]
for fruit in fruits:
  print(fruit)

leaderboard = {1: "Tuan", 2: "Simon", 3: "Duong"}
for key in leaderboard.keys():
  print(f'{key}: {leaderboard[key]}')
# 1: Tuan
# 2: Simon
# 3: Duong

unique_numbers = {1, 2, 3, 4, 5, 1, 3, 5}
for value in unique_numbers:
  print(f'{value}')
# 1
# 2
# 3
# 4
# 5

# use `enumerate` method to create an iterator that produces tuples containing an index and the corresponding element
# from the iterable so you can access index and element
for index, value in enumerate(unique_numbers):
  print(f'{index}: {value}')
# 0: 1
# 1: 2
# 2: 3
# 3: 4
# 4: 5

# `range()` returns an iterable of numbers from 0 up to (but excluding) the given number
for i in range(4):
  print(i) # 0 1 2 3

for i in range(5, 10):
  print(i) # 5 6 7 8 9

for i in range(5, 10, 2):
  print(i) # 5 7 9

# loop over a list to retrieve both the index and the value of each list item
# use `enumerate` method
for index, value in enumerate(["dog", "cat", "mouse"]):
  print(f'{index}: {value}')
# 0: dog
# 1: cat
# 2: mouse

# while repeats a block of code as long as a specified condition is true.
count = 0
while count < 5: # continue if this condition still True
  print(count) # 0 1 2 3 4
  count += 1 # shorthand for count = count + 1

# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function is an iterable
languages = {"en": "English", "vi": "Vietnam"}
languages_iterator = languages.keys() # dict_keys(['en', 'vi'])

# we can loop over it
for langKey in languages_iterator:
  print(langKey)

# however we cannot address elements by index, will raise TypeError
languages_iterator["en"] # TypeError: 'dict_keys' object is not subscriptable

# an iterable is an object that knows how to create an iterable
languages_iterator = iter(languages)

# our iterable is an object that can remember the state as we traverse through
# it. We get the next object with `next()`
next(languages_iterator) # en
next(languages_iterator) # vi

# after the iterable has returned all of its data, it raises a StopIteration exception
next(languages_iterator) # StopIteration

# we can also loop over iterable, infact `for` does it implicitly
for lang in iter(languages):
  print(lang) # en, vi

# we can grab all the elements of an iterable or iterator by call of `list()`
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_iterator = iter(days_of_week)
list(days_iterator) # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
list(days_iterator) # [] because state is saved
```

#### Control Statements within Loops

```python
# break: exits the nearest enclosing loop immediately
for value in [1, 2, 3, 4]:
  if value == 3:
    break
  print(value) # 1, 2

count = 0
while True:
  count += 1
  print(count) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  if count == 10:
    break

# continue: skip the rest of the code inside the current loop iteration and proceeds to the next iteration
# does continue work with while???
for i in range(10):
  if i <= 5:
    print(i) # 0, 1, 2, 3, 4, 5
    continue
  break

# pass: does nothing and is used as a placeholder for future code
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
for i in range(10):
  pass # Todo

if paid_successfully:
  pass # Todo

while valid:
  pass # Todo

def paid(amount: int, currency: str) -> bool:
  pass # Todo
  return True
```

#### Functions

A function is a block of code which only runs when it is called

```python
def no_args_func():
  print("Hi")

# invoke function
no_args_func()

def args_func(name, age):
  print(f'{name}, {age}')

# invoke function with args
args_func("Tuan", 35)
# you can also send arguments with the key = value syntax to make it easier to follow
args_func(name = "Tuan", age = 35)

# if you want to passing only positional-only arguments place `, /` at the end of arguments list
# means need to use positional arguments only when invoking function
def args_func(name, age, /):
  print(f'{name}: {age}')

args_func("Tuan", 35) # Tuan: 35
args_func(name = "Tuan", age = 35) # TypeError: args_func() takes 0 positional arguments but 2 were given

# The opposite of positional arguments is keyword-only arguments
# place `* ,` before arguments
# means need to use keyword arguments only when invoking function
def args_func(*, name, age):
  print(f'{name}: {age}')

args_func("Tuan", 35) # TypeError: args_func() takes 0 positional arguments but 2 were given
args_func(name = "Tuan", age = 35) # Tuan: 35

# you can even make it more complex by combining positional-only with keyword-only arguments
# I don't prefer to make the complex thing but just a case you want to known
def args_func(name: str, /, age: int, *, address: str) -> None:
  print(f'{name}, {age}, {address}')

# positional-only `/` always in front of keyword-only `*` arguments
args_func('John', 30, address='New York') # Valid
args_func(name = 'John', age = 30, 'New York') # invalid `name` keyword which should have value only, and `address` which should be here

# defind a function explicitly
def args_func(name: str, age: int) -> str:
  return f'{name}, {age}'

args_func("Tuan", 35)
args_func(name = "Tuan", age = 35)

# you can also set default value for arguments by assign `= value`
# default argument must always go after non-default argument
def args_func(value: int, decimal: bool = True) -> str:
  return f'{value}, {decimal}'

# this function will raise error: SyntaxError: parameter without a default follows parameter with a default
def args_func(value: int = 100, decimal: bool) -> str:
  return f'{value}, {decimal}'

args_func(1011011)
args_func(1011011, True)
args_func(value = 1011011, decimal = True)

# use arbitrary keyword arguments `**args`
# if you don't know how many arguments that will be passed into your function
# add `**` before the parameter name in the function definition
def console_log(**logs):
  print(logs)

console_log(name="John", age=30, city="New York") # {'name': 'John', 'age': 30, 'city': 'New York'}
console_log(company = "SpaceX", avg_salary = 5000) # {'company': 'SpaceX', 'avg_salary': 5000}

# Arbitrary argument must comes after non-arbitrary argument
def console_log(level = 'debug', **logs) -> None:
  print(f'{level}: {logs}')

console_log(name="John", age=30, city="New York") # debug: {'name': 'John', 'age': 30, 'city': 'New York'}
console_log('warning',name="John", age=30, city="New York") # warning: {'name': 'John', 'age': 30, 'city': 'New York'}
console_log(level = 'error',name="John", age=30, city="New York") # error: {'name': 'John', 'age': 30, 'city': 'New York'}
console_log(company = "SpaceX", avg_salary = 5000) # debug: {'company': 'SpaceX', 'avg_salary': 5000}

def console_log(message: str, level = 'debug', **logs) -> None:
  print(f'{level}: {message} ({logs})')

console_log(message = "Something goes wrong", name="John", age=30, city="New York") # debug: Something goes wrong ({'name': 'John', 'age': 30, 'city': 'New York'})
console_log('warning',name="John", age=30, city="New York") # debug: warning ({'name': 'John', 'age': 30, 'city': 'New York'})
console_log(level = 'error', message = "Something goes wrong", name="John", age=30, city="New York") # error: Something goes wrong ({'name': 'John', 'age': 30, 'city': 'New York'})
console_log("Something goes wrong", company = "SpaceX", avg_salary = 5000) # debug: Something goes wrong ({'company': 'SpaceX', 'avg_salary': 5000})

# if you try to but arbitrary argument in front of non-arbitrary arguments
# it will raise SyntaxError: arguments cannot follow var-keyword argument
def console_log(**logs, level = 'debug'): # SyntaxError
  print(f'{level}: {logs}')

# as I mentioned from above, we use `pass` keyword for placeholder
def shipping(address: str) -> bool:
  pass # Todo
  return True

shipping("Halong Bay, Quang Ninh, Vietnam")
shipping(address = "Halong Bay, Quang Ninh, Vietnam")
```

#### Lambda/anonymous functions

An anonymous function in Python is a function without a name. It can be immediately invoked or stored in a variable.

Anonymous functions in Python are also known as lambda functions.

```python
# syntax
lambda parameter(s) : expression

price = 1.99

# note that lambda has no name, we assign lambda function to variable revenue
# so that we can easily invoke the function through the variable.
revenue = lambda quantity: quantity * price

revenue(10) # 19.9

# Lambda functions can take any number of arguments:
sum = lambda a, b: a + b
sum(2, 3)

# lamda function does not support type annotation
sum = lambda a: int, b: int: a + b # SyntaxError: invalid syntax
sum(2, 3)

# you can invoke lambda function directly like this
(lambda a,b : a + b)(2, 5) #7

# lambda function always return data without `return` keyword
# it will return None by default if you don't provide any data
print((lambda name : print(f'Hi {name}'))("Tuan")) # Hi Tuan, None

# when to use `lambda` over `function`?
# you want to use function just once, especially useful when working with `map, reduce, filter`
# you need a short function which never consider to reuse
# you don't want to write explicit function
numbers = [1, 3, 5, 7, 9]
double_result = map(lambda value: value + value, numbers)

print(list(double_result))
# [2, 6, 10, 14, 18]
```
