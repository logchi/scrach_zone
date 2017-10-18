'''
标准库之对象持久化

dbm (anydbm in python2)

pickle (and cPickle in python2)

shelve (based on dbm and pickle)
'''

import shelve
file = shelve.open(filename, flag='c', protocol=None, writeback=False)


import dbm
file = dbm.open(filename, flag='r', mode)


file[key] = value     # value is a string for dbm, an arbitrary object for shelve
value = file[key]
count = len(file)
index = file.keys()
for key in file:
    pass
found = key in file
del file[key]
file.close()


import pickle
p = pickle.Pickler(fileobject, protocol=None)  # makes a new pickler, for saving to an output file object
p.dump(object)  # writes an object to the pickler's file/straem
pickle.dump(object, fileobject, protocol=None)  # combination of previous two

U = pickle.Unpickler(fileobject, encoding="ASCII", errors="strict")  # makes Unpickler, for loading from input file object
object = U.load()  # reads object from the unpickler's file/stream
object = pickle.load(fileobject, encoding="ASCII", errors="strict")  # combination of previous two
object = pickle.load(string, encoding="ASCII", errors="strict")  # reads object from a string