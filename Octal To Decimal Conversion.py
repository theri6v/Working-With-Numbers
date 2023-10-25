#the program for octal to decimal conversion in python . Octal numbers are also called numbers with base 8 and hold values from 0 – 7. 
#Whereas in Decimal numbers are with base 10 is Standard number system for denoting integers and non-integers. 

#Algorithm for converting octal to decimal nmber

#Methods discussed:
#Algorithmic way (Octal to Decimal)
#Inbuilt Method (Octal to Decimal)

----------------------------------------------------------------------------------'''Method 1 : Algorithmic Way'''----------------------------------------------------------------------------------
#Algorithm :

#Initialize two variable decimal value and base 0, 1 respectively
#Iterate using while loop until num is greater then 0
#For each iteration het the unit place digit and multiply it with base and add it to decimal value
#divide num by 10 and multiply base with 8
#Python ptogram for converting octal to decimal number

#Python Code :

def OctalToDecimal(num):
    decimal_value = 0
    base = 1

    while num:
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value


octal = 512
print("The decimal value of",octal, " is",OctalToDecimal(octal))
Output :
The decimal value of 512 is 330


----------------------------------------------------------------------------------'''Method 2 : Inbuilt Method'''----------------------------------------------------------------------------------
#By using inbuilt function int in Python we can convert any number with any base to decimal.
    
#Python Code

octal_num = 512

decimal_value = int(str(octal_num), 8)

print("The decimal value of {} is {}".format(octal_num, decimal_value))

Output
The decimal value of 512 is 330
