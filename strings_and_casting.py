# strings and casting


# There is no best practice for which quotes to use 
# greeting = "Hello world!"

# single_quotes = 'Single quotes \'wow\'' # need to escape the ' symbol
# double_quotes = "Double quotes 'wow'"

# print(single_quotes)
# print(double_quotes)

# Sting Slicing
# Indexing in Python starts from 0
# H e l l o   w o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

#print(len(greeting))
# there's a method called len() which can be used to find
# the number if characters in a string

# print(greeting[0:5]) # outputs 'Hello', starting from 0 upto 4
# print(greeting[6:11])

# Python supports reverse indexing. It begins from -1
# H e l l o   w o r l d !
# 
# print(greeting[-1])

#white_space = "Lot's of space at the end                                  "
# strip() removes white spaces
#print(len(white_space))
#white_space = white_space.strip()
#print(len(white_space))

# count(substring) returns the number of times a substring appears in a string
# count is case sensitive
# example_text = "some Text with a lot of text in it"
# print(example_text.count("text"))
# print(example_text.upper())
# print(example_text.lower())
# print(example_text.capitalize())

# print(example_text.replace(" ", "_"))

# Concatenation and Casting
first_name = "Cringe"
last_name = "Katalyst"
age = 27

#print(first_name + ' ' + last_name)
#print(first_name, last_name) # prints the same as above, but works differently

#print(first_name + ' ' + last_name + ' ' + str(age)) # will throw an error without str(age)
#print(first_name, last_name, age) # works without casting as each item is treated as its own object

# f strings - Used for formatting text
print(f"{first_name} {last_name} is {age} years of age.")