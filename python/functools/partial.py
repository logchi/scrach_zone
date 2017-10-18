# coding=utf-8

import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print('called myfunc with:', (a, b))
    return

def show_details(name, f, is_partial=False):
    """show details of a called object."""
    print('%s:' % name)
    print('object:', f)
    try:
        print('__name__:', f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('__doc__', repr(f.__doc__))
    return

# show_details('myfunc', myfunc)
# myfunc('a', 3)
# print

# p1 = functools.partial(myfunc, b=4)
# show_details('partial with named default', p1, True)
# p1('passing a')
# p1('override b', b=5)
# print

# p2 = functools.partial(myfunc, 'default a', b=99)
# show_details('partial with defaults', p2, True)
# p2()
# p2(b='override b')
print

print('Insufficient arguments:')
# p1()

show_details('myfunc', myfunc)
p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print('Updating wrapper:')
print('assign:', functools.WRAPPER_ASSIGNMENTS)
print('update:', functools.WRAPPER_UPDATES)
print

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)