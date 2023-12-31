#Here, in this page we will discuss the program for Decimal to binary conversion in python. A decimal number is a standard representation of integers or non-integers, 
#decimal numbers are also called as numbers with base 10. Whereas in binary number system numbers are with base 10 and shows representation by 0 and 1.

#Decimal to binary conversion

Methods discussed
'''Method 1: Binary Bits stored in Array'''
'''Method 2: Using mathematical operations to generate binary equivalent'''
---------------------------------------------------------------------------------------------'''Method 1: Binary Bits stored in Array'''---------------------------------------------------------------------------------------------

#Initialize a empty array as binaryArray
#while input number is greater then 0
#Append 1 if unit digit of num is odd else append 0
#Assign half the value of num to num
#Print all the values of  binary array

#Python Code

def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2)
        num = num//2
    for j in binaryArray:
        print(j, end="")


decimal_num = 21
convertBinary(decimal_num)
Output
Binary of 21 is : 10101



---------------------------------------------------------------------------------------------'''Method 2: Using mathematical operations to generate binary equivalent'''---------------------------------------------------------------------------------------------

#Initialize variables binary, i, rem and assign 0, 1, 0 respectively
#While input number is greater then zero run he loop
#rem equals to divisibility of input by 2
#num equals to half of num
#Add rem * i to binary
#Multiply i by 10
#return binary  


#Python Code

def convertBinary(num):
    binary = 0
    i, rem = 1, 0
    while num != 0:
        rem = num % 2
        num = num // 2
        binary += rem * i
        i *= 10
    return binary


decimal_num = 21
print("Binary of", decimal_num, "is : ", end="")
print(convertBinary(decimal_num))

Output
Binary of 21 is : 10101
