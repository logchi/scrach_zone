# mcb.py [ multiclipboard ]

USAGE = '''usage: python mcb.py command argv ...
command save -> save the current contents of clipboard will be saved with the keyword demo
command get -> retrive the content of keyword demo and copy it to clipboard
command list -> copy a list of keywords to the clipboard

demo:
python mcb.py save foo
python mcb.py get foo
python mcb.py list
'''

from pyperclip import copy, paste
from sys import argv
import shelve

COMMNDS = ['save', 'get', 'list']
SAVE_FILE = 'mcb'

argv_count = len(argv)
f = shelve.open(SAVE_FILE)
if argv_count <= 1:
    print('Commnad Lost!')
    print(USAGE)
elif argv_count == 2:
    command = argv[1]
    if command == 'list':
        copy("The following are all saved keywords: \n" + '\n'.join(f.keys()))
    else:
        print('Wrong command! We support just these commands: %s %s %s' % tuple(COMMNDS))
elif argv_count == 3:
    command = argv[1]
    key = argv[2]
    if command == 'save':
        f[key] = paste()
    elif command == 'get':
        copy(f[key])
    else:
        print('Wrong command! We support just these commands: %s %s %s' % tuple(COMMNDS))
else:
    print('Arguments out of scope!')
    print(USAGE)

f.close()
