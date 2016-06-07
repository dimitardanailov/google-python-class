# https://developers.google.com/edu/python/dict-files#dict-hash-table

## Can build up a dict by starting with the empty dict {}
## and storing key / value pairs into the dict like this:
## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
print dict          ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

# Simple lookup, returns 'alpha'
print dict['a']     ## alpha

# Put new key / value into dict
dict['a'] = 6
print dict          ## {'a': 6, 'o': 'omega', 'g': 'gamma'}
print 'a' in dict   ## True

if 'z' in dict: print dict['z'] ## Avoid KeyError

## By default, iterating over a dict iterates over its keys
## Note that the keys are in a random order
for key in dict: print key ## prints a g o

## Exactly the same as above
for key in dict.keys(): print key

## Get the .keys list:
print dict.keys() ## ['a', 'o', 'g']

## Common case --loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print key, dict[key]

## .items() is the dict expressed as (key, value) tuples
print dict.items() ## [('a', 6), ('o', 'omega'), ('g', 'gamma')]

## This loops syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print k, ' > ', v
## a  >  6
## o  >  omega
## g  >  gamma

## Dic formatting
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
# %d for int, %s for string
s = 'I want %(count)d copies of %(word)s' % hash
print s # I want 42 copies of garfield

## Del
var = 6
del var # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print list      ## ['b']

dict = { 'a': 1, 'b': 2, 'c': 3}
del dict['b']   ## Delete 'b' entry
print dict      ## {'a': 1, 'c': 3}