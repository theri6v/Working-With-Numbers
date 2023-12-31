#On this page we will learn how to create a python program for Hexadecimal to Decimal Conversion.
#Hexadecimal has numbers in the range of [0, 15] and to achieve so it also uses some characters of alphabets.
#Python program to convert hexadecimal to decimal

Hexadecimal Working :

#As discussed in hexadecimal numbers range from 0 to 15 so 0 to 9 are represented same as integer values but after 9 alphabets are used as shown below :

#A = 10
#B = 11
#C = 12
#D = 13
#E = 14
#F = 15

#How To Convert From Hexadecimal to Decimal Manually?
#For a user input num. This requires you to know ASCII values, please check the ASCII table here 
#To convert a hexadecimal to a decimal manually, you must start by multiplying the hex number by 16. 
#Then, you raise it to a power of 0 and increase that power by 1 each time according to the hexadecimal number equivalent.
#We start from the right of the hexadecimal number and go to the left when applying the powers. Each time you multiply a number by 16, the power of 16 increases.

#When converting a C9 hexadecimal to a decimal your work should look something like this:

Example :

9 = 9 * (16 ^ 0) = 9
C = 12 * (16 ^ 1) = 192
Then, we add the results.

192 + 9 = 201 
Hexadecimal	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F
Decimal	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15


#Python Code

def convert(hex):
    l = len(hex)
    decimal = 0
    pos = 0
    for i in range(l - 1, -1, -1):

        # if given index value is a digit (0 - 9)
        if '0' <= hex[i] <= '9':

            # if hex[i] is in range '0' - '9'
            # can convert string value to its integer value
            # by passing it to int() function
            digit = int(hex[i])
            decimal += digit * pow(16, pos)
            pos += 1

        # if given index is char in range [A, F]
        elif 'A' <= hex[i] <= 'F':

            # if hex[i] is in range 'A' - 'F'
            # can convert sting value to its int value
            # by subtracting 55(Refer Ascii table) as
            # ASCII val A: 65 and A must result 10 as value
            # to get ASCII value in Python can use ord() function
            digit = ord(hex[i]) - 55
            decimal += digit * pow(16, pos)
            pos += 1
    return decimal


hex = "C9"

print("decimal value of", hex, "is", convert(hex))

Output
Decimal value of C9 is 201
