#!/usr/bin/env python3
""" Several users reading a calendar, but only a few users updating it """

import threading
from readerwriterlock import rwlock
rwlock.
import time
counter=0
counter
marker = rwlock.RWLockFair()

def calendar_reader(id_number):
    global counter
    read_marker=marker.gen_rlock()
    read_marker.acquire()
    for i in range(10):
        time.sleep(1)
        print(counter)
        print(read_marker.c_rw_lock.v_read_count)
    read_marker.release()


def calendar_writer(id_number):
    global counter
    write_marker = marker.gen_wlock()
    write_marker.acquire()
    counter = 10
    name = 'Writer-' + str(counter)
    write_marker.release()

# create ten reader threads
for i in range(10):
    threading.Thread(target=calendar_reader, args=(i,)).start()

# ...but only two writer threads
for i in range(2):
    threading.Thread(target=calendar_writer, args=(i,)).start()

