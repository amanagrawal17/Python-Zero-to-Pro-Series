'''Python Program to Check if a Number is a Palindrome'''

def is_palindrome(n):
    num_str = str(n)
    return num_str == num_str[::-1]
   
 
n = int(input("Enter a number:"))
 
if is_palindrome(n):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")