path = '/tmp/demo.txt'

os.chdir(path)
os.getcwd()
os.chmod(path, mode)  # chnages mode of file path to numeric mode
os.chown(path, uid, gid)
os.link(srcpath, dstpath)  # creates a hard link to file srcpath, named dstpath
os.listdir(path)
os.mkdir(path [, mode])
os.makedirs(path, [, mode])
os.readlink(path)
os.remove(path)
os.unlink(path)
os.removedirs(path)
os.rename(srcpath, dstpath)
os.renames(oldpath, newpath)
os.rmdir(path)
os.stat(path)
os.symlink(srcpath, dstpath)
os.utime(path, (atime, mtime))
os.acess(path, mode)