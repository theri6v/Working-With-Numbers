Here, in this section we will discuss the program for decimal to octal conversion in python. 
Decimal numbers are the standard representation for representing integer or non-integer values. Decimal numbers are with base 10 and can represent numbers from 0-9. 
Whereas in Octal representation of numbers, numbers from 0-7 are represented as octal numbers are with base 8.

#Decimal to octal conversion in python
#Methods Discussed:-
#Using an array to store the comparable octal value
#Using int variable to store comparable octal value
---------------------------------------------------------------------------------------------'''Method 1:'''---------------------------------------------------------------------------------------------
#Take the decimal number from the user and store it in variable say decimal.
#Create an array say octal to store the octal representation of the given decimal number.
#Run a loop until decimal is not equal to 0 i.e., (decimal !=0)
#Inside the loop insert the remainder that achieved by dividing decimal from 8 i.e., (decimal%8)
#Coming out from the loop print the octal array in reverse order.


    
#Python program to convert decimal to octal number
#Python Code

decimal = 148
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8
for i in reversed(octal):
    print(i, end="")
    
Output
224

---------------------------------------------------------------------------------------------'''Method 2:'''---------------------------------------------------------------------------------------------


#Initialize ocatalNum to 0 and countVal to 1 and the decimal number as n
#Find the remainder when decimal number divided by 8
#Update octal number by octalNum + (remainder * countval)
#Increase countval by countval*10
#Divide decimal number by 8
#Repeat from the second step until the decimal number is zero

#Python Code

decimal = 33
octal = 0
count = 1

while decimal > 0:
    r = decimal % 8
    octal += r * count
    count *= 10
    decimal = decimal // 8

print(octal)

Output
41
