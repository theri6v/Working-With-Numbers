#On this page we will learn the concept of decimal to hexadecimal conversion in Python.
#We will also learn to Decimal to Hexadecimal Conversion in Python Programing language.
#Python Program to convert Decimal to Hexadecimal
---------------------------------------------------------------------------------------------'''Method 1'''---------------------------------------------------------------------------------------------
#To know how to solve this you must first have knowledge of ASCII Table.

#The program works in two cases

#If the current remainder left >= 10
#Must be replaced by (A – F)
#Else if current remainder < 10
#Must be replaced by (0- 9)
#Decimal to Hexadecimal conversion in Python
#Quadrants in which a given coordinate lies

#Python Code

def convert(num):
    hexa = []

    while num != 0:

        rem = num % 16

        if rem < 10:
            hexa.append(chr(rem + 48))
        else:
            hexa.append(chr(rem + 55))
        num = num // 16

    hexa.reverse()
    return ''.join(hexa)


decimal = 2545
print("Hexadecimal :", convert(decimal))
Output
Hexadecimal : 9F1
