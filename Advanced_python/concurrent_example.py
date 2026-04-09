import threading
import time

def square(num):
    print(f"Square: {num*num}")
    time.sleep(1)

def cube(num):
    print(f"Cube: {num*num*num}")
    time.sleep(3)

t1 = threading.Thread(target=square, args=(4,))
t2 = threading.Thread(target=cube, args=(4,))

t1.start()
t2.start()
t1.join()
t2.join()

print("Done!")

#-------------------------------------------------------------------
# importing the multiprocessing module
import multiprocessing
import os

def worker1():
    # printing process id
    print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
    # printing process id
    print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
    # printing main program process id
    print("ID of main process: {}".format(os.getpid()))

    # creating processes
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    # starting processes
    p1.start()
    p2.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until processes are finished
    p1.join()
    p2.join()

    # both processes finished
    print("Both processes finished execution!")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))

#-------------------------------------------------------------------------------

