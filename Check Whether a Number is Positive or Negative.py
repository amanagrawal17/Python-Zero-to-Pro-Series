'''Python Program to Check Whether a Number is Positive or Negative'''

def check_pos_neg(n):
    if(n > 0):
        print("Number is positive")
    else :
        print ("Number is negative")    
    
    
n  = int(input("Enter number: "))
check_pos_neg(n)