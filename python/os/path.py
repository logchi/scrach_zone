import os

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), ''))
print(os.path.join(os.path.dirname(os.path.abspath(__file__))))

'''output
====
/Users/sukong/projects/own/scratch_zone/python/os/path.py
/Users/sukong/projects/own/scratch_zone/python/os
/Users/sukong/projects/own/scratch_zone/python/os/templates
/Users/sukong/projects/own/scratch_zone/python/os/
/Users/sukong/projects/own/scratch_zone/python/os
'''
path = '/tmp/hehe/demo.txt'

os.path.abspath(path)
os.path.basename(path)
os.path.commonprefix([path, ...])
os.path.dirname(path)
os.path.exists(path)
os.path.expanduser(path)
os.path.expandvars(path)
os.path.getatime(path)
os.path.getsize(path)
os.path.isabs(path)
os.path.isfile(path)
os.path.isdir(path)
os.path.islink(path)
os.path.ismount(path)
os.path.join(path1, path2, ...)
os.path.normcase(path)
os.path.realpath(path)
os.path.samefile(path1, path2)
os.path.sameopenfile(fp1, fp2)
os.path.samestat(stat1, stat2)
os.path.split(path)
os.path.splitdrive(path)
os.path.splitext(path)
os.path.walk()  # python 2 only, 3 use os.walk()
