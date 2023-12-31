#Here, in this page we will discuss program to find Prime number between 1 to100 in python .
#A prime number is an positive integer that has no divisors except one and itself or can only be exactly divided by the integers 1 and itself without leaving a remainder.

#Prime number between 1 to 100

Methods Discussed

'''Method 1 :Basic checking prime by only checking first n'''
'''Method 2: Basic checking prime by only checking first n/2 divisors'''
'''Method 3: Checking prime by only checking first √n divisors'''
'''Method 4: Checking prime by only checking first √n divisors, but also skipping even iterations.'''

#Method used to check prime
#Here we use the usual method to check prime. If given number is prime then we print it else we move ahead to the next number and check if that is prime and keep going till 100
#Find Prime Number between 1 to 100 in Python

-------------------------------------------------------------------------'''Method 1 :Basic checking prime by only checking first n'''--------------------------------------------------------------------------

#Python Code

def checkPrime(num):

    #  0, 1 and negative numbers are not prime
    if num < 2:
        return 0
    else:

        # no need to run loop till num-1 as for any number x the numbers in
        # the range(num/2 + 1, num) won't be divisible anyway
        # Example 36 won't be divisible by anything b/w 19-35

        x = num // 2
        for j in range(2, x + 1):
            if num % j == 0:
                return 0

    # the number would be prime if we reach here
    return 1


a, b = 1, 100
for i in range(a, b + 1):
    if checkPrime(i):
        print(i, end=" ")
Output
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

--------------------------------------------------------------------------'''Method 2: Basic checking prime by only checking first n/2 divisors'''--------------------------------------------------------------------------


#Run a loop in the iteration of (i) b/w 1 and 100 bounds.
#For each, i check if its prime or not using function checkPrime(i)
#If i is prime print it else move to the next iteration
#Here we use the usual method to check prime. We however check the divisibility only till num/2. 

#As the range(num/2 + 1, num) won't be divisible anyways. Example 36 won't be divisible by anything b/w 19-35
    
#Python Code

def checkPrime(num):

    #  0, 1 and negative numbers are not prime
    if num < 2:
        return 0
    else:

        # no need to run loop till num-1 as for any number x the numbers in
        # the range(num/2 + 1, num) won't be divisible anyway
        # Example 36 won't be divisible by anything b/w 19-35
        x = num // 2
        for j in range(2, x + 1):
            if num % j == 0:
                return 0

    # the number would be prime if we reach here
    return 1


for i in range(1, 100 + 1):
    if checkPrime(i):
        print(i, end=" ")
Output
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


#Count possible decoding of a given digit sequence
#Find the prime numbers between 1 to 100
#Calculate the number of digits in an integer
#Convert digit/number to words
#Counting number of days in a given month of a year


--------------------------------------------------------------------------'''Method 3: Checking prime by only checking first √n divisors'''--------------------------------------------------------------------------

#The outer logic remains the same. Only the method to check prime changes to make code more optimized. Has better time complexity of O(√N)
#Run a loop in the iteration of (i) b/w 1 and 100 bounds.
#For each, i check if its prime or not using function checkPrime(i)
#If i is prime print it else move to next iteration
Method used to check prime
#A number n is not a prime if it can be factored into two factors a & b:
#n = a * b 

#Now a and b can't be both greater than the square root of n, since then the product a * b would be greater than sqrt(n) * sqrt(n) = n. 
#So in any factorization of n, at least one of the factors must be smaller than the square root of n, and if we can't find any factors less than or equal to the square root, n must be a prime. 
#So we only need to run loop till sqrt(n) and not n or n/2


#Python Code

from math import sqrt


def checkPrime(num):
    #  0, 1 and negative numbers are not prime
    if num < 2:
        return 0
    else:

        # A number n is not a prime, if it can be factored into two factors a & b:
        # n = a * b

        """Now a and b can't be both greater than the square root of n, since
        then the product a * b would be greater than sqrt(n) * sqrt(n) = n.
        So in any factorization of n, at least one of the factors must be
        smaller than the square root of n, and if we can't find any factors
        less than or equal to the square root, n must be a prime."""

        for j in range(2, int(sqrt(num))):
            if num % j == 0:
                return 0

    # the number would be prime if we reach here
    return 1


a, b = 1, 100
for i in range(a, b + 1):
    if checkPrime(i):
        print(i, end=" ")


Output
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
--------------------------------------------------------------------------'''Method 4: Checking prime by only checking first √n divisors, but also skipping even iterations.'''--------------------------------------------------------------------------

#The outer logic remains the same. Only the method to check prime changes to make code more optimized. Has same time complexity of O(√N).
#But makes around half lesser checks
#Run a loop in the iteration of (i) b/w 1 to 100 bounds.
#For each, i check if its prime or not using function checkPrime(i)
#If i is prime print it else move to next iteration

#We can simply check all divisors between [2, √num]
#2 is the only even prime number
#We can skip all even iterations in the loop


#Python Code

from math import sqrt


def checkPrime(n):
    # 0 and 1 are not prime numbers
    # negative numbers are not prime
    if n <= 1:
        return 0
    # special case as 2 is the only even number that is prime
    elif n == 2:
        return 1

    # Check if n is a multiple of 2 thus all these won't be prime
    elif n % 2 == 0:
        return 0

    # If not, then just check the odds
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return 0
    return 1


a, b = 1, 100
for i in range(a, b + 1):
    if checkPrime(i):
        print(i, end=" ")

# This method is obviously faster as makes around half lesser comparison due skipping even iterations in the loop

Output
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
