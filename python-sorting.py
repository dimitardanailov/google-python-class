# https://developers.google.com/edu/python/sorting

numbers = [5, 1, 4, 3]
print sorted(numbers) ## [1, 3, 4, 5]
print numbers ## [5, 1, 3, 3]

strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs) ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print sorted(strs, reverse=True) ## ['zz', 'aa', 'CC', 'BB']

# Custom Sorting with key=
strs = ['ccc', 'aaaa', 'b', 'bb']
print sorted(strs, key=len) ## ['d', 'bb', 'ccc', 'aaaa']

# Custom function

## Say we have a list of strings we want to sort
## by the last letter of the string.
strs = ['xc', 'zb', 'yd', 'wa']

## Write a little function that takes
## a string, and returns its last letter.
## This will be the key function
## (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-1]

## Now pass key=MyFn to sorted() to sort by last letter
print sorted(strs, key=MyFn) ## ['wa', 'zb', 'xc', 'yd']

# Tuples
tuple = (1, 2, 'hi')
print len(tuple)      ## 3
print tuple[2]        ## hi
# tuple[2] = 'bye'    ## NO, tuples cannot be changed
tuple = (1, 2, 'bye') ## this works

(x, y, z) = (42, 13, "hike")
print z               ## hike

## List Comprehensions
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums] ## 1, 4, 9, 16
print squares

strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs] ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
print shouting

## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2] ## [2, 1]
print small

## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'bannana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s] ## ['APPLE', 'BANNANA']
print afruits