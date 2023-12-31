 will discuss binary-to-decimal conversion in Python. For this purpose, we need to take a binary integer number from user and convert that binary integer number to its decimal equivalent form and then print the converted number on to the screen. A Decimal number can be calculated by multiplying every digits of binary number with 2 to the power of the integers starts from 0 to n-1 where n refers as the total number of digits present in a binary number and finally add all of them.

Binary to decimal conversion

Working :
 A Decimal number can be calculated by multiplying every digits of binary number with 2 to the power of the integers

 starts from 0 to n-1 where n refers as the total number of digits present in a binary number and finally add all of them.

Methods Discussed :
Algorithmic way (Binary to Decimal)
Inbuilt Method (Binary to Decimal)

---------------------------------------------------------------------------------------------'''Method 1'''---------------------------------------------------------------------------------------------


Algorithm :
  
While num is greater then zero
Store the unit place value of num to a variable (rem)
Calculate rem with base and add it to answer
Completely divide Num by 10 and multiply base with 2
Time and Space Complexities
Time Complexity – O(N), where N is the count of the digits in the binary number
Space Complexity – O(1), Constant Space
   
Python Code :

num = 10
binary_val = num
decimal_val = 0
base = 1

while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print("Binary Number is {}\nDecimal Number is {}".format(binary_val, decimal_val))
Output :
Binary Number is 10
Decimal Number is 2
