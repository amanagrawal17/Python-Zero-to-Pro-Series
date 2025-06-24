"Python Program to Print All Odd Numbers in a Range:"

def odd_num(lower, upper):
    for i in range(lower, upper):
        if i % 2 != 0:
            print (i)
            
            
odd_num(1,15)