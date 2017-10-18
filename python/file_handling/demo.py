import os

os.system('touch /tmp/demo.txt')

infile = open(filename, 'r')   # default
infile = open(filename, 'rb')  # binary read [ byte stream ]
infile = open(filename, 'r+')  # both input and output
with open('/tmp/demo.txt') as f:
    f.read()
    f.read(N)
    f.readline()
    f.readlines()       # => [line string, ...]
    for line in f:      # => space saving, read on need


outfile = open(filename, 'w')   # write mode
outfile = open(filename, 'wb')   # binary write mode
with open('/tmp/demo.txt') as f:
    f.write(S)
    f.wirtelines(I)     # I is an iterable


with open('/tmp/demo.txt') as f:
    # file methods
    f.close()
    f.tell()    # return the file's current position
    f.seek(offset, whence=0)  # 移动游标偏移offset到新的位置，whence为0表示从文件起始起，
                              # 1表示从当前位置，2表示从尾端开始
    f.isatty()
    f.flush()
    f.truncate(size)
    file.fileno()

    # file attrbutes
    f.closed   # => True or False
    f.mode     # => 'r' ...
    f.name     # => '/tmp/demo.txt' ...

