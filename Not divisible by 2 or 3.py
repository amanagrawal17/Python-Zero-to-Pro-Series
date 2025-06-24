"Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3"

def divi(L, U):
    for i in range(L,U):
        if(i%2!=0 and i%3!=0):
            print(i)

divi(1, 20)
            
