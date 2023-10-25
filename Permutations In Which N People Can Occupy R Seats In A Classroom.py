#program for Permutations In Which N People Can Occupy R Seats in python .In this python program, we will be defining the number of ways in which N number of students can occupy R number of seats. 
#Take an example Ten friends enter the classroom late and all the seats are occupied by toppers of the college and now only Six seats are available so 
#in how many ways are those Ten friends will occupy Six seats although 4 students have to leave the classroom. We will use math library for factorial function in building of this program.


#Way 2 Of Asking Question
#Write code to find all possible permutations in which n people can occupy r seats in a theater
#Problem Statement :
#In a classroom some of the seats are already occupied by students and only a few seats are available in the classroom. The available seats are assumed as r and n number of students are looking for the seat. We need to find in how many different permutations n number of students can sit on r number of chairs.

#Algorithm
#Input number of students in n
#Input number of seats in r
#Use permutation formula { factorial(n) / factorial(n-r) }

#Print Output
#Permutation in which n people can occupy in python

#Quadrants in which a given coordinate lies
#Maximum number of handshakes
#Addition of two fractions
#Replace all 0’s with 1 in a given integer


#Python code

# Permutations in which n people can occupy r seats
# function for factorial
def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact


# main program
# user input
n = int(input("Enter number of people: "))
r = int(input("Enter number of seats: "))

# finding all possible arrangements of n people on r seats
# by using formula of permutation
p = factorial(n) // factorial(n - r)

# printing output
print("Total possible arrangements:", p)

Output
Enter number of people: 10
Enter number of seats: 6
Total possible arrangements: 151200
