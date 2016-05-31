# https://developers.google.com/edu/python/lists
colors = ['red', 'blue', 'green']

print colors[0]         # red
print colors[2]         # green
print len(colors)       # 3

# Assignment with an = on lists does not make a copy. Instead,
# assignment makes the two variables point to the one list in memory.
b = colors              ## Does not copy the list
print ''

# FOR and IN

# Python's *for* and *in* constructs are extremely useful,
# and the first use of them we'll see is with lists.
# The *for* construct -- for var in list -- is an easy way to look at each element in a
# list (or other collection). Do not add or remove from the list during iteration.

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num

print sum               # 30

list = ['larry', 'curly', 'move']
if 'curly' in list:
    print 'yay'

print ''

# Range
# The range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) returns a, a+1,
# ... b-1 -- up to but not including the last number. The combination of the for-loop and the range()
# function allow you to build a traditional numeric for loop:
for i in range(10):
    print i

print ''

# List
list = ['larry', 'curly', 'move']
list.append('shemp')            # append elem at end
list.insert(0, 'xxx')           # insert elem at index 0
list.extend(['yyy', 'zzz'])     # add list of elements at end
print list                      # ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print list.index('curly')       # 2

list.remove('curly')            # search and remove that element
list.pop(1)                     # removes and returns 'larry'
print list                      # ['xxx', 'moe', 'shemp', 'yyy', 'zzz']