# coding=utf-8


s = '大师傅'
su = u'大师傅'
print(type(s))
print(type(su))
print(s == su)
print(len(s))
print(len(su))

# python2
'''
<type 'str'>
<type 'unicode'>
/Users/sukong/projects/own/scratch_zone/python/str/str.py:8: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  print(s == su)
False
9
3
'''

# python3
'''
<class 'str'>
<class 'str'>
True
3
3
'''