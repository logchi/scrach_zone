# class partial:
#     """New function with partial application of the given arguments
#     and keywords.
#     """

#     __slots__ = "func", "args", "keywords", "__dict__", "__weakref__"

#     def __new__(*args, **keywords):
#         if not args:
#             raise TypeError("descriptor '__new__' of partial needs an argument")
#         if len(args) < 2:
#             raise TypeError("type 'partial' takes at least one argument")
#         cls, func, *args = args
#         if not callable(func):
#             raise TypeError("the first argument must be callable")
#         args = tuple(args)
#
class A:
    def a():
        return '123'

a = A()
a.a = '456'
print(a.a())