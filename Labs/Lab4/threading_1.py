import threading # import the threading module
 
def print_cube(num):
    # function to print cube of given num
    print("Cube: {}".format(num * num * num))
 
def print_square(num):
    # function to print square of given num
    print("Square: {}".format(num * num))
 
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
    
    t1.start() # starting thread 1
    t2.start() # starting thread 2
 
    t1.join() # wait until thread 1 is completely executed
    t2.join() # wait until thread 2 is completely executed
 
    print("Done!") # both threads completely executed