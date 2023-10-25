#program to check whether a number be expressed as a sum of two prime number in python. Prime number is a number which only have two divisors 
#i.e. a number which can not be divided by any other number other than 1 or itself is a prime number.

#Number be expressed as a sum of two prime numbers in python
#There are many theories which express numbers as a sum of two primes like Goldbach’s Conjecture which states that any even number greater than 2 can be expressed as a sum of two primes.
#Prime number is a number which only have two divisors i.e. a number which can not be divided by any other number other than 1 or itself is a prime number.

#Here we will check for all the numbers if they can be expressed as sum of two primes or not.

Algorithm

#Take number as input in n
#Initialize a variable flag as 0
#Iterate using for loop from value of i between (2, n/2)
#For each iteration Call a function sum_of_two_primes for value of i is it returns 1
#Call same function for value n-i and if it is also 1 then print i and n-i as answer increment the flag to 1
#If flag is 0 print not possible
#Create function sum_of_two_prime where check if passed number is prime return true else false
#number be expressed as a sum of two prime numbers


'''Python code'''

# take input
Number = int(input('Enter the Number : '))
# initialize an array
arr = []
# find prime numbers
for i in range(2, Number):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    # append prime numbers to array
    if flag == 0:
        arr.append(i)
# possible combinations
flag = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        # if condition is True Print numbers
        if arr[i] + arr[j] == Number:
            flag = 1
            print(str(arr[i]) + " and " + str(arr[j]) + ' are prime numbers when added gives ' + str(Number))
            break
if flag == 0:
    print('No Prime numbers can give sum of ' + str(Number))


Output
Insert the num: 15
15 can be expressed as the sum of 2 and 13
