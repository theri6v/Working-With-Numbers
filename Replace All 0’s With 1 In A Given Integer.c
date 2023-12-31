//how to Replace All 0’s With 1 In A Given Integer using Python.
//The concept is simple, find the digits of the integer. Compare each digit with 0 if the digit is equal to 0 then replace it with 1. Construct the new integer with the replaced digits.
//Replace all 0's with 1 in given integer

Implementation

//We will convert the integer into string.
//Then we will convert it into list and then we will traverse through the list.
//Wherever we find a ‘0’ we will replace with ‘1’.
//Question can come like Way 1

//Write a code to change all zero's as one's (0s as 1s) in a given number? ex: 120014 needs to be printed as 121114
//Question can come like Way 2

//implement a c program to replace all 0's with 1 in a given integer as an input, all the 0's in the number has to be replaced with 1.

Algorithm

//Take Input in num and initialize a variable num with with value 0
//If num is equals to zero then update the value of num2 to 1
//Iterate using a while loop until num is greater then 0
//For each iteration initialize a variable rem and store unit digit of num
//If rem equals to 0 then set rem to 1
//Set num to num divide by 10 & num2 equals to num2*10+rem
//Reverse and print num2
//Replace all 0's with 1


----------------------------------------------------------------------------------'''Method 1'''----------------------------------------------------------------------------------

num = int(input("Enter number : "))
num2 = 0

if num == 0:
    num2 = 1

while num > 0:
    rem = num % 10
    if rem == 0:
        rem = 1
    num = num//10
    num2 = num2 * 10 + rem

num = 0
while num2 > 0:
    r = num2 % 10
    num = num * 10 + r
    num2 //= 10

print("Converted number is:", num)


----------------------------------------------------------------------------------'''Method 2'''----------------------------------------------------------------------------------

#taking Input
n=int(input('Enter number: '))
#converting into string
n=str(n) 
#then into the list
n=list(n)
r="" #empty string for addind it the item of list
for i in range(len(n)):
    #if we find '0' we will replace it with '1'
    if(n[i]=='0'):
        n[i]='1'
    r=r + n[i]  #creating the new integer 
del n    
print("Converted number is :",int(r))
Method 3
Run
n=int(input("Enter number: "))
s=str(n)
l=[]
for i in s:
    if(i=='0'):
        l.append('1')
    else:
        l.append(i)
ns=""
for i in l:
    ns+=i
print("Converted number is:", int(ns))
Method 4
Run
#take inputs
Val = int(input('Enter number:'))
#change type to string
Val = str(Val)
Replaced = Val.replace('0','1')
print("Converted number is:" + Replaced)

    
Output
Enter number: 12090
Converted number is: 12191
