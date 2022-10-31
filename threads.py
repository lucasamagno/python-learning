import threading
import sys
import math
import random
import time

def execute_thread(i):
    # time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1, 5)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

for i in range(1, 10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print("Acting Thread:", threading.active_count())
    print("Thread Objects:", threading.enumerate())


