# https://developers.google.com/edu/python/regular-expressions
import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)

if match:
    print 'found', match.group() # 'found word:cat'
else:
    print 'did not find'