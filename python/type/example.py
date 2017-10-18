type(1)

import types
print(dir(types))
print('There are totally %s types im Python' % len(dir(types)))

print(type('abc'))
print(type('abc') == str)