# Python Datatypes and Operators

- String
- Numbers: Integer, Float, Long
- Boolean (True or False)

## Arithmetic and Comparison Operators

### Arithmetic
```python
+, -, *, /, % # (modulus - it gives the remainder)
```

### Comparison

- `<` | (`<=`) Less than (or equal to)
- `>` | (`>=`) Greater than (or equal to)
- `==` Equal to
- `!=` Not equal to
---
## Strings and Casting

### Single and Double Quotes
There is no best practice for which quotes to use  

```python
single_quotes = 'Single quotes \'wow\'' # need to escape the ' symbol
double_quotes = "Double quotes 'wow'"
```
Output:
```
Single quotes 'wow'
Double quotes 'wow'
```
---
### Sting Slicing
Indexing in Python starts from 0
```
H e l l o _ w o r l d  !
0 1 2 3 4 5 6 7 8 9 10 11
```

Python supports reverse indexing. It begins from -1
```
 H   e   l   l   o   _   w   o   r   l   d   !
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
```  
---
### Concatenation and Casting

```python
first_name = "Cringe"
last_name = "Katalyst"
age = 27

print(first_name + ' ' + last_name)
print(first_name, last_name) # prints the same as above, but works differently
```
Output:
```
Cringe Katalyst
Cringe Katalyst
```
---

```python
print(first_name + ' ' + last_name + ' ' + str(age)) # will throw an error without str(age)
print(first_name, last_name, age) # works without casting as each item is treated as its own object
```
Output:
```
Cringe Katalyst 27
Cringe Katalyst 27
```
---
### f strings - Used for formatting text
```python
print(f"{first_name} {last_name} is {age} years of age.")
```
Output:
```
Cringe Katalyst is 27 years of age.
```