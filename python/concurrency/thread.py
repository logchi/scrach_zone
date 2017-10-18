# coding=utf-8
import time
from threading import Thread

def countdown(n):
    while n > 0:
        print('T-minus:', n)
        n -= 1
        time.sleep(2)

t = Thread(target=countdown, args=(10,))
'''
The interpreter remains running until all threads terminate.
For long-running threads or background tasks that run forever,
you should consider making the thread daemonic.
Daemonic threads can’t be joined. However,
they are destroyed automatically when the main thread terminates.
'''
# t = Thread(target=countdown, args=(10,), daemon=True)
t.start()

if t.is_alive():
    print('the thread is still alive')
else:
    print('the thread is completed')

time.sleep(7)
# t.join() # request to join with a thread, which waits for it to terminate



