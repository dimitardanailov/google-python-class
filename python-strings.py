# https://developers.google.com/edu/python/strings#devsite_header_1

s = 'h1'
print s[1]                  ## i
print len(s)                ## 2
print s + ' there'          ## hi there
print ''

simple = "Hello"
print simple[1:4]            #ell - chars starting at index 1 and extending up to but not including index 4
print simple[1:]             #ello - omitting either index defaults to the start or end of the string
print s[:]                   #Hello - omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
print s[1:100]               #ello - an index that is too big is truncated down to the string length

# The standard zero-based index numbers give easy access to chars
# near the start of the string. As an alternative, Python uses negative numbers to give easy access to the chars at the
# end of the string: s[-1] is the last char 'o', s[-2] is 'l' the next-to-last char, and so on.
# Negative index numbers count back from the end of the string:

print simple[-1]            # is 'o' -- last char (1st from the end)
print simple[-4]            # is 'e' -- 4th from the end
print simple[:-3]           # is 'He' -- going up to but not including the last 3 chars.
print simple[-3:]           # is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.
print ''

#### String % ####

# Python has a printf()-like facility to put together a string.
# The % operator takes a printf-type format string on the left (%d int, %s string, %f/%g floating point),
# and the matching values in a tuple on the right (a tuple is made of values separated by commas,
# typically grouped inside parenthesis):

# % operator
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print text
