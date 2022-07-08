#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading

pencil = threading.Lock()

garlic_count = 0
garlic_count
def shopper_mut():
    global garlic_count
    for i in range(100000000):
        pencil.acquire()
        pencil.acquire()
        garlic_count += 1
        pencil.release()
        pencil.release()
    

barron = threading.Thread(target=shopper_mut)
olivia = threading.Thread(target=shopper_mut)
barron.start()
olivia.start()
barron.is_alive()
olivia.is_alive()
barron.join()
olivia.join()
print('We should buy', garlic_count, 'garlic.')
