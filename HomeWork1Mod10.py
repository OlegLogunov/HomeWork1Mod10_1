from time import sleep
from threading import Thread

albet = ("abcdefghij")

def cycle():
    for i in range(10):
        print(i + 1)
        sleep(1)

def alphabet():
    for j in albet:
        print(j)
        sleep(1)

thread = Thread(target = cycle)
thread.start()

thread1 = Thread(target = alphabet)
thread1.start()
thread.join()
