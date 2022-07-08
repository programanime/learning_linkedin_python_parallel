#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading
import time

items_on_notepad = 0
pencil = threading.Lock()

def shopper1():
    pencil.acquire()
    time.sleep(15)
    print("ya lo voy a liberar")
    pencil.release()
def shopper2():
    while True:
        aval=pencil.acquire(blocking=False)
        if aval:
            print("i get the resource")
            pencil.release()
            return
        else:
            print("i do some other stuff here")
            time.sleep(1)

    
barron = threading.Thread(target=shopper1, name='Barron')
olivia = threading.Thread(target=shopper2, name='Olivia')
start_time = time.perf_counter()
elapsed_time = time.perf_counter() - start_time
start_time
barron.start()
olivia.start()
barron.join()
olivia.join()
elapsed_time = time.perf_counter() - start_time
elapsed_time 
print('Elapsed Time: {:.2f} seconds'.format(elapsed_time))
