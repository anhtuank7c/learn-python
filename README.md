# Learn Python

I use this repo to track all the lessons I learned about python

## Reference documents

* https://www.geeksforgeeks.org/python-programming-language-tutorial
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

# trim whitespace from lead and tail
"    this is a string with spacing         ".strip() # this is a string with spacing

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

# sorting a list is a common behavior in real-life
salaries = [123.02, 3423.13, 34543, 945, 100, 8833.5]

salaries.sort()  # default ascending sort
print(salaries)  # [100, 123.02, 945, 3423.13, 8833.5, 34543]

salaries.sort(reverse=True)
print(salaries)  # [34543, 8833.5, 3423.13, 945, 123.02, 100]

names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]

names.sort()
print(names) # ['Adam', 'Corey', 'John', 'Rick', 'Steve', 'Thomas']

names.sort(reverse=True)
print(names) # ['Thomas', 'Steve', 'Rick', 'John', 'Corey', 'Adam']

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

# joining tuples using concatenation `+` operator
book_author = book + author # ('Harry Porter', 2002, 'Published', 'JK Rowling', 1965, 'Female', 'England')
# or `sum()` function
new_tuple_two = sum((book, author), ()) # ('Harry Porter', 2002, 'Published', 'JK Rowling', 1965, 'Female', 'England')

book[:2] # ('Harry Porter', 2002)
book[:-1] # ('Harry Porter',)
book[::2] # ('Harry Porter', 'Published')
book[2:] # ('Published',)
book[1:2] # (2002,)
"England" in author # True

# You cannot extend a tuple directly
author.extend(book) # AttributeError: 'tuple' object has no attribute 'extend'
# you need to cast to list and cast back to tuple after merged
author_list = list(author)
book_list = list(book)

author_list.extend(book_list)
new_tuple = tuple(author_list)
print(new_tuple) # ('JK Rowling', 1965, 'Female', 'England', 'Harry Porter', 2002, 'Published')

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

# keys for dictionaries have to be immutable types to ensure key can be 
# converted to a constant hash value for quick look-ups.
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

#### Enum (Enumeration)

Enum is a symbolic name for a set of values. Enum is immutable which means some case you might want to use Enum as Constants (Python have no Constant)

Enum are used to create readable names for a collection of related constants and make the code more readable and maintainable. Python's enum module provides the `Enum` class for creating enuimarations.

```python
# define an Enum TransactionState
from enum import Enum

class TransactionState(Enum):
  PENDING = 0
  PROCESSING = 1
  COMPLETED = 2
  FAILED = 3
  REFUNDED = 4

print(TransactionState.COMPLETED.name) # COMPLETED
print(TransactionState.COMPLETED.value) # 4

# using Enum in Conditional statement
if transaction_result == TransactionState.COMPLETED:
  print("Transaction completed")
elif transaction_result == TransactionState.PENDING:
  print("Transaction pending")
else:
  print("Transaction in other state")

# loop over Enum
for state in TransactionState:
  print(state)

class Theme(Enum):
  DARK = "dark"
  LIGHT = "light"

# auto assign value use `auto()` from enum module
from enum import Enum, auto

class Theme(Enum):
  DARK = auto()
  LIGHT = auto()

for theme in Theme:
  print(theme.value) # 1, 2

# output: will be auto-assigned starting from 1
# 1
# 2

# enum with method
from enum import Enum, auto

class Theme(Enum):
    DARK = auto()
    LIGHT = auto()

    def is_light(self):
        return self in {Theme.LIGHT}

print(Theme.LIGHT.is_light()) # True
print(Theme.DARK.is_light()) # False

# enum is immutable, which means you cannot reassign value to Enum
Theme.LIGHT.value = 123 # AttributeError: <enum 'Enum'> cannot set attribute 'value'
```

### Variables

Variable in Python is a name that refers to a value. Python is dynamically typed which mean you don't need to declare the variable type explicitly.

```python
# variable identifier must follow these rules
# - must start with a letter [a-z A-Z] or an underscore `_`
# - can be followed by letter, digits (0-9) or underscore `_`
# - case-sensitive (e.g myVar and myvar are different variables)
# - cannot be a reversed keyword (e.g if, while, for, break, continue, pass)

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
# int
age: int = 35
# float
pi: float = 3.14
# str
name: str = "Tuan"
# bool
sold_out: bool = True

# use `id()` function to find the variable address on memory
print(id(age)) # 4357660072
print(id(pi)) # 4342525072
print(id(name)) # 4344113520
print(id(sold_out)) # 4356703696

########################
# variable scope
# - local scope: variable declared inside a function are local to that function
# - enclosing scope: variable in the local scope of enclosing function (nonlocal)
# - global scope: variable declared at the top level of a
#   script or module, or declared global using `global` keyword
# - built-in scope: variable preassigned in the built-in namespace (e.g., `len`, `range`)
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
# Python is dynamically typed, meaning that variable types are 
# determined at runtime, variables can change type
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

# create custom iterator
# to create an object/class as an iterator, you have to implement
# the method `__iter__()` and `__next__()`
# `__iter__()` method acts similar, you can do operations but must always return the iterator object itself
# `__next__()` method also allows you to do operations, and must return the next item in the sequence
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 3:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

my_class = MyNumbers()
my_iterator = iter(my_class)

print(next(my_iterator)) # 1
print(next(my_iterator)) # 2
print(next(my_iterator)) # 3
print(next(my_iterator)) # raise StopIteration
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

# invalid `name` keyword which should have value only, and `address` which should be here
args_func(name = 'John', age = 30, 'New York')

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

# {'name': 'John', 'age': 30, 'city': 'New York'}
console_log(name="John", age=30, city="New York")

# {'company': 'SpaceX', 'avg_salary': 5000}
console_log(company = "SpaceX", avg_salary = 5000)

# Arbitrary argument must comes after non-arbitrary argument
def console_log(level = 'debug', **logs) -> None:
  print(f'{level}: {logs}')

# debug: {'name': 'John', 'age': 30, 'city': 'New York'}
console_log(name="John", age=30, city="New York")

# warning: {'name': 'John', 'age': 30, 'city': 'New York'}
console_log('warning',name="John", age=30, city="New York")

# error: {'name': 'John', 'age': 30, 'city': 'New York'}
console_log(level = 'error',name="John", age=30, city="New York")

# debug: {'company': 'SpaceX', 'avg_salary': 5000}
console_log(company = "SpaceX", avg_salary = 5000)

def console_log(message: str, level = 'debug', **logs) -> None:
  print(f'{level}: {message} ({logs})')

# debug: Something goes wrong ({'name': 'John', 'age': 30, 'city': 'New York'})
console_log(message = "Something goes wrong", name="John", age=30, city="New York")

# debug: warning ({'name': 'John', 'age': 30, 'city': 'New York'})
console_log('warning',name="John", age=30, city="New York")

# error: Something goes wrong ({'name': 'John', 'age': 30, 'city': 'New York'})
console_log(level = 'error', message = "Something goes wrong", name="John", age=30, city="New York")

# debug: Something goes wrong ({'company': 'SpaceX', 'avg_salary': 5000})
console_log("Something goes wrong", company = "SpaceX", avg_salary = 5000)

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

#### Decorators

Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of a function or class.

Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function without permanently modifying it. But before deep into decorators let us understand some concepts that will come in handy in learning the decorators.

**First Class Object**

In Python, functions are **[first class object](https://www.geeksforgeeks.org/first-class-functions-python/)** which means that functions in Python can be used or passed as arguments

Properties of first class functions:

- A function is an instance of the Object type
- You can store the function in a variable
- You can pass the function as a parameter to another function
- You can return the function from a function
- You can store them in data structures such as hash tables, lists ...

Consider the below examples for better understanding

Example 01: Treating the functions as objects

```python
def shout(text: str) -> str:
  return text.upper()

# we assign function shout to a variable. This will not invoke the function instead it
# takes the function object referenced by a shout abd creates a second name pointing to it `yell`
yell = shout

print(yell('Hello')) # HELLO
```

Example 02: Passing the function as an argument

```python
from typing import Callable

def shout(text: str) -> str:
  return text.upper()

def whisper(text: str) -> str:
  return text.lower()

def greet(func: Callable[[str], str]) -> None:
  # storing the function in a variable
  greeting = func('Hi, I am created by a function passed as an argument')
  print(greeting)

greet(shout) # HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT
greet(whisper) # hi, i am created by a function passed as an argument
```

In the above example, the greet function takes another function as a parameter (shout and whisper in this case). The function passed as an argument is then called inside the function greet.

Example 03: write your first decorator

```python
def logger(func):
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__}: {func.__code__.co_argcount}")
    func(*args, **kwargs)
  return wrapper

def another_func(x: int, y: int) -> int:
  return x + y

# we can pass func as a parameter as usual but it's doesn't convenient
another_func = logger(another_func)
another_func(1, 2) # Calling another_func: 2

# we can use decorator like this
# convenient and easy to read
@logger
def my_func(x: int, y: int) -> int:
  return x + y

my_func(1, 2) # Calling my_func: 2
```

Example 4: make decorator function return data

```python
from functools import wraps

def start_end_decorator(func):
  # wraps ensures docstring, function name, arguments list, etc. are all copied
  # to the wrapped function - instead of being replaced with wrapper's info
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('start')
    result = func(*args, **kwargs)
    print('end')
    return result
  return wrapper

@start_end_decorator
def hello(name: str):
  return f'Hello {name}'

print(hello("Tuan"))
```

**Chaining Decorator** means decorating a function with multiple decorators

```python
from functools import wraps

def logger(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('logger start')
    result = func(*args, **kwargs)
    print('logger end')
    return result
  return wrapper

def acl(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('check permission, valid, continue')
    result = func(*args, **kwargs)
    print('after check permission')
    return result
  return wrapper

@logger
@acl
def add_transaction(amount: float, reason: str):
  print(f'{amount =}, {reason =}')
  return "random_transaction_id"

add_transaction(120.123, "Test")

# logger start
# check permission, valid, continue
# amount =120.123, reason ='Test'
# after check permission
# logger end
```

**Decorator and classes**

Example 01: inject decorators function to class methods

```python
# tracking.py
from functools import wraps

def tracking(func):

  @wraps(func)
  def wrapper(self, *args, **kwargs):
    # call the original func
    result = func(self, *args, **kwargs)
    print(f'[{func.__name__}]: items in cart of "{self.user_id}": {len(self.items)}')
    return result
  return wrapper

# cart_item.py
class CartItem:
  def __init__(self, product_id: str, quantity: int) -> None:
    self.product_id = product_id
    self.quantity = quantity

# shopping_cart.py
from cart_item import CartItem
from typing import List
from utils.tracking import tracking

class ShoppingCart:
  def __init__(self, user_id: str) -> None:
    self.user_id = user_id
    self.items: List[CartItem] = []
  
  @tracking
  def add_item(self, item: CartItem) -> None:
    self.items.append(item)
    print(f'Added item {item.product_id} to cart of user {self.user_id}')

  @tracking
  def remove_item(self, item: CartItem) -> None:
    self.items.remove(item)
    print(f'Removed item {item.product_id} from cart of user {self.user_id}')

  @tracking
  def checkout(self):
    print(f'Checking out {len(self.items)}')
    self.items.clear()

# main.py
from cart_item import CartItem
from shopping_cart import ShoppingCart

cart = ShoppingCart("user_01")
cart_item_1 = CartItem("sku_01", 2)
cart_item_2 = CartItem("sku_02", 5)
cart.add_item(cart_item_1)
cart.add_item(cart_item_2)
cart.remove_item(cart_item_1)
cart.checkout()

# Added item sku_01 to cart of user user_01
# [add_item]: items in cart of "user_01": 1
# Added item sku_02 to cart of user user_01
# [add_item]: items in cart of "user_01": 2
# Removed item sku_01 from cart of user user_01
# [remove_item]: items in cart of "user_01": 1
# Checking out 1
# [checkout]: items in cart of "user_01": 0
```

Example 02: use decorator to manipulate function result

```python
# product.py
class Product:
  def __init__(self, id: str, name:str, price: float) -> None:
    self.id = id
    self.name = name
    self.price = price

# cart_item.py
class CartItem:
  def __init__(self, product_id: str, quantity: int) -> None:
    self.product_id = product_id
    self.quantity = quantity

# utils.py
from functools import wraps
from cart_item import CartItem
from product import Product
from typing import Callable, TypeVar

T = TypeVar("T", bound=Callable[[Product], Product])

# decorator function receive CartItem and return Product
def extract_product(func: T) -> Callable[[CartItem], Product]:
  @wraps(func)
  def wrapper(cart_item: CartItem, *args, **kwargs) -> Product:
    if not hasattr(cart_item, "product_id"):
      raise ValueError("cart_item must have product_id attribute")
    if not hasattr(cart_item, "quantity"):
      raise ValueError("cart_item must have quantity attribute")
    product = Product(cart_item.product_id, "fake_name", 0.0)
    return func(product, *args, **kwargs)
  return wrapper

# main.py
from cart_item import CartItem
from product import Product
from utils import extract_product

cart = ShoppingCart("user_01")
cart_item_1 = CartItem("sku_01", 2)
cart_item_2 = CartItem("sku_02", 5)

# return product object with decorator function
@extract_product
def process_checkout(product: Product):
  print(f"Checking out product {product.id}")

# passing cart_item object
process_checkout(cart_item_1) # Checking out product sku_01
process_checkout(cart_item_2) # Checking out product sku_02
```

#### Generators

Generators are defined using the `yield` keyword. When a generator function is called, it returns a generator object, but the function's code is not actually run until you iterate over the generator (e.g for loop).

Each time `yield` is encountered, the function's state is saved, and the yielded value is returned. The function can then be resumed from where it left off when the next value is requested.

```python
def simple_generator():
  print('first yield')
  yield 1
  print('second yield')
  yield 2
  print('third yield')
  yield 3

# using generator
gen = simple_generator()

print(f'received {next(gen)}')
print(f'received {next(gen)}')
print(f'received {next(gen)}')
print(f'received {next(gen)}')
```

Explain example from above:

1. first call `next(gen)`
  * print first yield
  * encountered `yield 1`, pausese and return 1 to the caller
  * the state of the generator is saved right after `yield 1`
2. second call `next(gen)`
  * the generator resume from where it pauseed, after `yield 1`
  * print second yield
  * encountered `yield 2`, pausese and return 2 to the caller
  * the state of the generator is saved right after `yield 2`
3. third call `next(gen)`
  * the generator resume from where it pauseed, after `yield 2`
  * print third yield
  * encountered `yield 3`, pausese and return 2 to the caller
  * the state of the generator is saved right after `yield 3`
4. fourth call `next(gen)`
  * there is nothing left in the generator so it will raise StopIteration exception

**Key points about yield**

* State preservation: Unlike a regular function call, when you call a generator, the state of the function is preserved between **yield** statements, allowing the function to continue where it left off.
* Lazy evaluation: The generator does not compute all its values at once. Instead, it generates each value on-the-fly when requested, which can save memory
* Return vs Yield: While return exist a function completely, yield pause the function, allow it to resume later

Generators are memory-efficient because they only load the data needed to process the next value in the iterable. This allows them to perform operations on otherwise prohibitively large value rangs.

Note: `range` replaces `xrange` in Python 3

```python
def fibonacci_generator(limit: int):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + 1

for number in fibonacci_generator(10):
  print(number)
```

Benefit of generators

* Memory Efficiency: Generators are memory-efficient since they produre items once at a time and do not store the entire sequence in memory
* Lazy Evaluation: Generators allow for lazy evalation, meaning values are computed as needed, which is useful when working with large datasets or infinite sequences.
* Simplified Code: Generators can simplify code by eliminating the need for complex iterator logic

```python
# reading large file with generator
def read_large_file(path: str):
  with open(path, 'r') as file:
    for line in file:
      yield line.strip()

for contact in read_large_file('contacts.txt'):
  print(contact)
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

#### Closures functions

A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Closures can capture an carry some variables from the outer function to the inner function.

This can be useful for creating function factories or function decorators.

How closures works?
1. Nested Function
  A function defined inside another function
2. Free variables
  Variables from the outer scope that the inner function can reference
3. Returning the Inner Function
  The outer function returns the inner function, which captures the state of the outer function's variables

```python
def outer_function(name: str):
  def inner_function():
    print(f'Hello {name}')
  return inner_function

# create a closure
closure = outer_function('Tuan')
closure()

# another example
def outer_function():
  count: int = 0
  def inner_function():
    nonlocal count
    count += 1
    print(count)
  return inner_function

# create a closure
closure = outer_function()
closure() # 1
closure() # 2
closure() # 3
```

Closures are useful for creating functions with some preset configurations.

```python
def make_multiplier(multiplier: int):
  def multiplier_func(input: int) -> int:
    return input * multiplier
  return multiplier_func

# create multiplier functions
double = make_multiplier(2)
triple = make_multiplier(3)
quad = make_multiplier(4)

print(double(5)) # 10
print(double(8)) # 16

print(triple(5)) # 15
print(triple(8)) # 24

print(quad(5)) # 20
print(quad(8)) # 32
```

Key points about closures

* State Retention: Closures retain the state of the variables in the outer function's scope
* Encapsulation: Closures can encapsulate functionality and data together
* Function Factories: Closures are ofent used to craete functions with specific behaviors preset

Avoiding common pitfalls

1. Mutable variable: be cautious with mutable variables in closures as they can lead to unexpected behaviors
2. Late binding: Python uses late binding for closures, meaning the values of variables are looked up when the inner function is called.
  This can cause issues if the variable values change after the closure is created. You can avoid this by using default arguments:

```python
def outer_func(numbers):
  return [lambda x, n = n: x + n for n in numbers]

closures = outer_func([1, 2, 3])
print([func(2) for func in closures]) # [3, 4, 5]
```

Real world examples of closures

```python
from enum import Enum

class LogLevel(Enum):
  DEBUG = "DEBUG"
  INFO = "INFO"
  ERROR = "ERROR"

def create_logger(level: LogLevel):
  def logger(message: str):
    print(f"[{level.value}] {message}")
  return logger

info_logger = create_logger(LogLevel.INFO)
error_logger = create_logger(LogLevel.ERROR)

info_logger('Something goes wrong') # [INFO] Something goes wrong
info_logger('Eiusmod mollit proident mollit laboris duis qui ut sint.') # [INFO] Eiusmod mollit proident mollit laboris duis qui ut sint.

error_logger('Something goes wrong') # [ERROR] Something goes wrong
```

Simple caching mechanism to store previously computed values

```python
def cache_func(func):
  cache = {}
  def wrapper(n):
    if n not in cache:
      cache[n] = func(n)
    return cache[n]
  return wrapper

@cache_func
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10)) # 55
print(fibonacci(23)) # 28657
```

### Modules

A Python module is a file containing Python code. It can define functions, classes and include runnable code.

Modules allow you to organize your code into manageable parts and reuse it across different programs.

#### Creating a module

Simply create a file with a `.py` extension.

```python
# transaction.py

# variable in modules
mock = {
  "tranId": "random_id",
  "amount": 0.0,
  "tax": 0.0,
  "address": "123 Sub St",
}

def add(amount: int, tax: float, address: str) -> str:
  return f'tranId: random_id, {amount =}, {tax =}, {address =}'

def update(transId: str, amount: int, tax: float, address: str) -> str:
  return f'updated. tranId: {transId}, {amount =}, {tax =}, {address =}'
```

#### Using a module

To use a module, import it into your script using the `import` statement

```python
import transaction

print(transaction.mock) # {'tranId': 'random_id', 'amount': 0.0, 'tax': 0.0, 'address': '123 Sub St'}
print(transaction.add(10, 20.0, "nowhere"))
print(transaction.update("011010", 10, 20.0, "nowhere"))
```

#### Importing specific items

You can import specific functions or classes from a module, separated by commas

```python
from transaction import add, update

print(add(10, 20.0, "nowhere"))
print(update("011010", 10, 20.0, "nowhere"))
```

You can also give an imported item an alias

```python
from transaction import update as modify

print(modify("011010", 10, 20.0, "nowhere"))
```

#### The `__name__` and `__main__`

In Python, the special variable `__name__` is used to determine if a module is being run as the main program or if it has been imported into another module

```python
# greeting.py

def greet(name: str) -> None:
  print(f'Hello {name}')

if __name__ == "__main__":
  greet("Main")

# When you execute greeting.py module, it will print Hello Main
# However if you import greeting.py from another script, the code inside the
# `if __name__ == "__main__":` block does not execute
```

#### Find you which functions and attributes are defined in a module

```python
# greeting.py
age = 10
def greet(name: str) -> None:
  print(f'Hello {name}')

if __name__ == "__main__":
  greet("Main")

# main.py
import greeting

dir(greeting)
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'age', 'greet']
```

#### Module priority

Python prefer local module over modules come from different places (included Python built-in modules)

If you have `math.py` module in the same place with your current script

It will be loaded instead of the built-in Python module

```python
# math.py

def add(a: int, b: int) -> int:
  return a + b

# main.py
import math # this is math.py because it have higher priority

print(math.add(1, 2))
```

#### Built-in modules

There are several built-in modules in Python, which you can import whenever you like, you can find them in here: https://docs.python.org/3/py-modindex.html

```python
import platform
import math
import io

print(platform.system())
print(math.sqrt(12))
print(io.open("contacts.txt").readline())
```

### Classes

Python is an Object Oriented Programming language.

Almost everything in Python is an object with its properties and methods.

A class is like an object constructor or a blueprint for creating objects.

#### Creating a class

To create a class, use `class` keyword

```python
# order.py
class Order:

  # A class attribute. It is shared by all instances of this class
  TAG: str = "ORDER"

  # basic initializer, this is called when this class is instantiated.
  # methods (or objects or attributes) like: __init__, __str__, __repr__ etc... are called
  # special methods (sometime called dunder methods)
  def __init__(self, id):
    # assign the argument to the instance's id attribute
    self.id = id
    # the leading underscore indicate the `status` property
    # is intended to be used internally
    # do not rely on this to be enforced: it's a hint to other devs
    self._status = 0
  
  # `__repr__` method is intended to provide a "representation" of the object
  # that is useful for debugging and development purposes. 
  def __repr__(self):
    return f'{self.id = }, {self.amount = }, {self.status = }'

  # `__str__` method, on the other hand, is intended to provide a "string" 
  # representation of the object that is more user-friendly and suitable
  # for display to end users
  def __str__(self):
    return f"Order {self.id}, amount: {self.amount}, status: {self.status}"

  # an instance method
  # all method take `self` as the first argument
  # `self` parameter is a reference to the current instance of the class, 
  # and is used to access variables that belongs to the class
  def place(self, amount:float, address: str) -> None:
    self.amount = amount
    print(f'Placed order {self.id}, {amount}, {address}')
  
  # a class method is shared among all instances
  # they are called with the calling class as the first argument
  @classmethod
  def get_id(cls):
    return cls.id

  # a static method is called without a class or instance reference
  @staticmethod
  def payment_method():
    return "Paypal"

  # property is just like a getter
  # it turns the method status() into a read-only attribute of the same name
  # there's no need to write trivial getters and setters in Python
  @property
  def status(self):
    return self._status

  # this allows the @property to be set
  # `status` is the @property that we define from above
  @status.setter
  def status(self, status):
    self._status = status

  # this allows the property to be deleted
  @status.deleter
  def status(self):
    del self._status
  
  # when a Python interpreter reads a source file it executes all its code.
  # this __name__ check makes sure this code block is only executed when
  # this module is the main program
  if __name__ == "__main__":
    print("Hello from main")

# main.py
from order import Order

first_order = Order("000001")

# access class attribute
first_order.TAG # ORDER

# modify class attribute
first_order.TAG = "USER"

# reassign value of object property
first_order.amount = 200.123

# get object property
print(first_order.amount)
# invoke property (getter)
print(first_order.status)
# assigning properter (setter)
first_order.status = 1

# delete property from object
del first_order.amount
del first_order.status

# delete object
del first_order

# invoke class method
first_order.place(10.0, "123 Main St") # Placed order 000001, 10.0, 123 Main St
first_order.get_id() # 000000

# invoke static method via instance
print(first_order.payment_method()) # Paypal

# invoke static method via class name
print(Order.payment_method()) # Paypal
```

#### Static attributes

Static attributes also known as **class attributes**, in Python **can be modified** because they are simply variables with the class object rather than with instances of the class.

In Python, variables do not have inherent immutability, their mutability is determinded by the type of the object they refer to. Static attributes and modifiable both through the class itself and through its instance

In Python, immutability is not enforced on **attributes** or **variables**. Instead, it's a characteristic of the data types:

* **Immutable types**: int, float, str, tuple etc...
* **Mutable types**: list, dict, set, etc...

When a static attribute refers to a mutable object, changes to the object will be reflected wherever the reference is accessed. If the static attribute itself is reassigned, it affects instance because they all refer to the same class attribute.

To ensure static attribute are immutable we have one possible way:

1. Convention: Use naming conventions to indicate that an attribute should not be modified (e.g STATIC_ATTRIBUTE, TAG, UPPERCASE_VARIABLE)

#### Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

**Parent class** is the class being inherited from, also called base class

**Child class** is the class that inherites from **Parent class**, also called derived class

```python
# Parent class
class Person:
  def __init__(self, *, first_name: str, last_name: str):
    self.first_name = first_name
    self.last_name = last_name
  
  def __str__(self):
    return f'{self.first_name} {self.last_name}'

  def say_my_name(self):
    print(f'Hi {self.first_name} {self.last_name}')

tuan = Person(first_name = "Tuan", last_name = "Nguyen")
tuan.say_my_name() # Hi Tuan Nguyen

# Child class
class Student(Person):
  def __init__(self, *, first_name: str, last_name: str, class_name: str):
    # call parent's `__init__` function to keep inheritance
    Person.__init__(self, first_name = first_name, last_name = last_name)
    # or use `super()` function which have the same result but look nicer
    super().__init__(first_name = first_name, last_name = last_name)

    # child class property
    self.class_name = class_name

  @property
  def name(self):
    return f'{self.first_name} {self.last_name}'

  @name.setter
  def name(self, name: str):
    arr = name.split(" ")
    first_name = arr[0] if len(arr) >= 1 else "default_fname"
    last_name = arr[1] if len(arr) >= 2 else "default_lname"
    self.first_name = first_name
    self.last_name = last_name

  def welcome(self):
    print(f'Welcome {self.name} to the class {self.class_name}')

  def __str__(self):
    return f'[{self.class_name}]: {self.first_name} {self.last_name}'

student_tuan = Student(first_name = "Anton", last_name = "Nguyen", class_name = "A3")
# invoke method from parent class
student_tuan.say_my_name() # Hi Anton Nguyen
student_tuan.welcome() # Welcome Anton Nguyen to the class A3
student_tuan.name = "Kim Phuong"
student_tuan.welcome() # Welcome Kim Phuong to the class A3
```

#### Access Modifiers

Python supports a form of access control for class properties and methods, although it does so in a more informal way compared to some other languages like Java or C++.

Python use naming conventions to indicate the intended level of access:

1. **Public**: Public attributes and methods are accessible from anywhere. By default, all attributes and methods are public.
   ```python
    class MyClass:
      def __init__(self):
        self.public_var = "I am public"
      def public_method(self):
        print("this is a public method")
    obj = MyClass()
    print(obj.public_var) # I am public
    obj.public_method() # this is a public method
   ```
2. **Protected**: Protected attributes and methods are indicated by a single underscore prefix `_`. These are intended to be accessible within the class and its subclasses but not from outside the class.
   ```python
    class MyClass:
      def __init__(self):
        self._protected_var = "I am protected"
      def _protected_method(self):
        print("this is a protected method")
    
    class SubClass(MyClass):
      def access_protected(self):
        print(self._protected_var) # I am protected
        self._protected_method() # this is a protected method
    
    obj = SubClass()
    obj.access_protected()
   ```
3. **Private**: Private attributes and methods are indicated by a double underscore prefix `__`. This triggers name mangling, where the attribute name is modified to include the class name, making it harder (but not impossible) to access from outside the class.
   ```python
   # example 01
    class MyClass:
      def __init__(self):
        self.__private_var = "I am private"
      def __private_method(self):
        print("this is a private method")

    class SubClass(MyClass):
      def access_protected(self):
        print(self.__private_var) # raise AttributeError
        self.__private_method() # raise AttributeError
    
    obj = SubClass()
    obj.access_protected()

    # example 02
    # Python doesn't block access to private data, it just leaves for the wisdom of the programmer, 
    # not to write any code that access it from outside the class. 
    # You can still access the private attributes/methods by Python's name mangling technique 
    # but will breaks the encapsulation principle so not recommend to do this in real-life
    class SubClass(MyClass):
      def access_protected(self):
        print(self._MyClass__private_var) # I am protected
        self._MyClass__private_method() # this is a protected method
    
    obj = SubClass()
    obj.access_protected()
   ```

#### Abstract class

An abstract class can be considered a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.

A class that contains one or more abstract methods is called an **abstract class**. An abstract method is a method that has a delcaration but does not have an implementation.

We use abstract class while we are designing large functional units or when we want to provide a common interface for different implementations of a component.

##### Abstract base classes

By defining an abstract base class, you can define a common **Application Program Interface** (**API**) for a set of subclasses.

By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining **Abstract Base Classes** (**ABC**) and that module name **ABC**.

* Example 01

  ```python
  from abc import ABC, abstractmethod

  class Polygon(ABC):
    # abstract method will be force to be implement in subclasses
    @abstractmethod
    def noofsides(self):
      pass

  class Triangle(Polygon):
    # must concrete implement abstract method
    def noofsides(self):
      print("I have 3 sides")

  class Pentagon(Polygon):
    # must concrete implement abstract method
    def noofsides(self):
      print("I have 5 sides")

  class Hexagon(Polygon):
    # must concrete implement abstract method
    def noofsides(self):
      print("I have 6 sides")

  triangle = Triangle()
  triangle.noofsides()

  pentagon = Pentagon()
  pentagon.noofsides()

  hexagon = Hexagon()
  hexagon.noofsides()
  ```

* Example 02

  ```python
  from abc import ABC, abstractmethod

  class Record(ABC):
    @abstractmethod
    def __str__(self) -> str:
      pass

    @abstractmethod
    def create(self) -> bool:
      pass

    @abstractmethod
    def update(self, *args) -> bool:
      pass

    @abstractmethod
    def delete(self) -> bool:
      pass

    @staticmethod
    @abstractmethod
    def TAG():
      pass

  class UserRecord(Record):
    def __init__(self, name: str, bod: str, avatar: str) -> None:
      self.name = name
      self.bod = bod
      self.avatar = avatar


    def __str__(self) -> str:
      return f"[{UserRecord.TAG()}]: {self.name} {self.bod} {self.avatar}"

    def create(self) -> bool:
      # execute sql command to create user
      return True

    def update(self, *args) -> bool:
      # execute sql command to update user
      return True

    def delete(self) -> bool:
      # execute sql command to delete user
      return True

    @staticmethod
    def TAG():
      return "USER"

  class ProductRecord(Record):
    def __init__(self, name: str, price: float, description: str) -> None:
      self.name = name
      self.price = price
      self.description = description

    def __str__(self) -> str:
      return f"[{ProductRecord.TAG()}] {self.name} {self.price} {self.description}"

    def create(self) -> bool:
      # execute sql command to create product
      return True

    def update(self, *args) -> bool:
      # execute sql command to update product
      return True

    def delete(self) -> bool:
      # execute sql command to delete product
      return True

    @staticmethod
    def TAG():
      return "PRODUCT"

  user_record = UserRecord("John", "1990-01-01", "https://example.com/avatar.jpg")
  print(user_record) # [USER]: John 1990-01-01 https://example.com/avatar.jpg
  user_record.create()
  user_record.update("Johny", "1991-01-01", "https://example.com/avatar2.jpg")
  user_record.delete()
  print(UserRecord.TAG()) # USER

  product_record = ProductRecord("iPhone", 1000, "A new phone")
  print(product_record) # [PRODUCT] iPhone 1000 A new phone
  product_record.create()
  product_record.delete()
  print(ProductRecord.TAG()) # PRODUCT
  ```

### Polymorphism

Polymorphism means **many forms**, and in programming it refers to methods/functions/operators with the same name that can be executed on many object or classes.

#### Function polymorphism

`len()` is one of many function polymorphism in Python that accept many kind of data

```python
# str
len("Tuan") # 4

# tuple
len(("apple", "banana", "cherry")) # 3

# list
len(["apple", "banana", "cherry"]) # 3

# dict
len({"foo": "bar"}) # 1
```

#### Class polymorphism

Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

```python
# polymorphism method `eat()` appear to all classes

class Dog:
  def __init__(self, name: str):
    self.name = name
  
  def eat(self):
    print('Dog is eating')

class Cat:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

  def eat(self):
    print('Cat is eating')

dog = Dog("Grant")
dog.eat() # Dog is eating

cat = Cat("Banana", 3)
cat.eat() # Cat is eating
```

#### Inheritance Class Polymorphism

Yes, we could do that

```python
class Animal:
  def __init__(self, name: str):
    self.name = name
  
  def eat(self):
    print('Animal is eating')

class Dog(Animal):
  def __init__(self, name: str, age: int):
    super().__init__(name)
    self.age = age

  def eat(self):
    print('Dog is eating')

class Cat(Animal):
  def __init__(self, name: str, age: int):
    super().__init__(name)
    self.age = age

  def eat(self):
    print('Cat is eating')

dog = Dog("Grant", 5)
dog.eat() # Dog is eating

cat = Cat("Banana", 3)
cat.eat() # Cat is eating
```

#### Data classes

[This module](https://docs.python.org/3/library/dataclasses.html) provides a decorator and functions for automatically adding generated special methods such ash `__init__` and `__repr()__` to user-defined classes.

```python
from dataclasses import dataclass, field

@dataclass
class InventoryItem:
  """Class for keeping track of an item in inventory"""
  name: str
  # if the default value of a field is specified by a call to `field()`, then the class attribute
  # for this field will be replaced by the specified `default` value.
  # if `default` is not provided, the the class attribute will be deleted
  unit_price: float = field(repr = False, default = 0.0)
  quantity_on_hand: int = 0
  source: str = field(repr = True, default = "global")

  @property
  def total_cost(self) -> float:
    return self.unit_price * self.quantity_on_hand

inventory_product_one = InventoryItem("Product name 01", 1.99, 1000)
print(inventory_product_one) # InventoryItem(name='Product name 01', quantity_on_hand=1000, source='global')
print(inventory_product_one.total_cost) # 1990.0
inventory_product_two = InventoryItem("Product name 01", 1.99, 1000)

if inventory_product_one == inventory_product_two: # True
  print("2 product are the same")
```

So we don't need to add an `__init__()` method like this

```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
  self.name = name
  self.unit_price = unit_price
  self.quantity_on_hand = quantity_on_hand
```

### Exception handling

Exception handling in Python is a mechanism that allows you to handle errors or exceptional situation in your code gracefully, instead of letting the entire program cash. Python provides a robust and flexible way to handle exceptions using the `try`, `except`, `else` and `finally` blocks.

#### Basic structure of exception handling

The basic structure looks like this

```python
try:
  result = 1 + non_exist_variable
except NameError as e:
  print(e)
else:
  print("successful operation")
finally:
  print("cleanup operation")
```

**Explanation**

1. try Block:
  * The code that yoy want to execute and that might raise an exception in placed inside the try block
2. except Block: 
  * If an excetion occurs in the `try` block, the code in the except block is executed. You can catch specific exceptions by specifying the exception type (e.g `except NameError`)
  * The `as e` part allows you to capture the exception object and access its message or other attributes
3. else Block:
  * The `else` block is optional and is executed only if no exception was raised in the `try` block
4. finally Block:
  * The `finally` block is also optional and is executed regardless of whether an exception occurded or not. This is typically used for cleanup operations like closing files or releasing resources, closing database connection.

#### Handling specific exception

**Here's an example where we handle different types of exception**

```python
def divide_number(a, b):
  try:
    result = a / b
  except ZeroDivisionError as e:
    print(f"Error: {e} - Division by zero is not allowed")
  except TypeError as e:
    print(f"Error: {e} - Only numbers are allowed")
  else:
    print(f"Result: {result}")
  finally:
    print("Execution of the divide_number function is completed")

divide_number(10, 0)
# Error: division by zero - Division by zero is not allowed
# Execution of the divide_number function is completed

divide_number(10, "a")
# Error: unsupported operand type(s) for /: 'int' and 'str' - Only numbers are allowed
# Execution of the divide_number function is completed

divide_number(10, 2)  
# Result: 5.0
# Execution of the divide_number function is completed
```

**Handle multiple exceptions**

```python
try:
  risky_operation()
except (ValueError, TypeError) as e:
  print(f"Error: {e}")
```

#### Raising exceptions

Sometime you might want to raise an exception manually using the `raise` keyword

```python
def check_age(age):
  if age < 0:
    raise ValueError("Age cannot be negative")
  return f"Age is {age}"

try:
  check_age(-1)
except ValueError as e:
  print(f"Exception '{e}'")

# Exception 'Age cannot be negative'
```

#### Custom exceptions

You can define your own exceptions by creating a new class that inherits from Python's built-in **Exception** class

```python
class InsufficientBalanceError(Exception):
  pass

def checkout(total: float, balance: float) -> bool:
  if balance < 0:
    raise InsufficientBalanceError("Negative balance is not allowed")
  if balance < total:
    raise InsufficientBalanceError("Your balance is not enough for checkout")
  return balance >= total

try:
  checkout(29.9, 10)
except InsufficientBalanceError as e:
  print(f'Error: {e}')

# Error: Your balance is not enough for checkout
```
