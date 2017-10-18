import os
from glob import glob

def removeFiles(lst_of_path):
    if type(lst_of_path) is list:
        for path in lst_of_path:
            if type(path) is str:
                os.remove(path)
            else:
                 print('the argument must be a list of path!')
    else:
        print('the argument must be a list of path!')

removeFiles(glob('answerFile*'))
removeFiles(glob('quizFile*.txt'))


