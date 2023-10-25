#Number of Digits in an integer in python program to find the length of the Integer entered by the user. The number of digits present in the Integer is the length of the Integer. 
#Every Character or Integer or any other variable or constant either given by the user or predefined has some length.

#number of digits in an integer in python
Method Discussed :

/'''Method 1: Using loop'''
/'''Method 2: Using formulae'''

Let’s discuss above two methods in brief,

-------------------------------------------------------------------------------------------'''Method 1: Using loop'''-------------------------------------------------------------------------------------------
Let’s see how the code works:

#The input will be stored in an int type variable say n.
#do while loop is started
#Divide n by 10 and store result in n itself
                                           # n //=10;

E#very time n is divided by 10 increment digit by 1
                                           # digit++;.

#Do this until num is not equal to 0
                                            #while(n!=0);

#digit is printed which is the number of digits in num.

'''Method 1: Using loop'''

def countDigit(n):
    digit = 0
    while n != 0:
        n //= 10
        digit += 1
    return digit
 
 
# Driver Code
n = 78673
print("Number of digits : % d" % (countDigit(n)))
Output
No. of digits = 5
-------------------------------------------------------------------------------------------'''Method 2: Using formulae'''-------------------------------------------------------------------------------------------
In this method we will use simple log10(logarithm of base 10) to count the number of digits of positive numbers (logarithm is not defined for negative numbers).
Digit count of

Digits = upper bound of log10(N). 
        
Method 2: Using formulae
      
import math

# Driver Code
n = 78673
digit = math.floor(math.log10(n)+1)
print("Number of digits : ", digit)
Output
No. of digits = 5
