Here, in this page we will discuss program for addition of two fractions in python. For this purpose we need to ask the user to enter two fractional values where each fraction must consist a Numerator and a Denominator.

Addition of two fractions in python
Concept
 For understanding this in a better way lets suppose an example :

 Suppose, First fraction consist of 1 as numerator and 3 as denominator, and Second fraction consist of 3 as numerator and 9 as denominator.

 (1 / 3) + (3 / 9) = (6 / 9) = (2 / 3)

Find LCM of 3 and 9 and the result will be 9.
Multiply 3 in first fraction : (3 / 9) + (3 / 9)
Add both fractions and then the result will be : (6 / 9)
Now simplify it by finding the HCF of 6 and 9 and the result will be 3.
So divide 6 and 9 by 3 and then the result will be : (2 / 3)
This will be your simplified answer for the given problem.
Algorithm
Initialize variables of numerator and denominator
Take user input of two fraction
Find numerator using this condition (n1*d2) +(d1*n2 ) where n1,n2 are numerator and d1 and d2 are denominator
Find denominator using this condition (d1*d2) for lcm
Calculate GCD of a this new numerator and denominator
Display a two value of this condition x / gcd, y/gcd
Addition of two fractions
Related Pages
Permutations in which n people can occupy r seats in a classroom
 
Maximum number of handshakes
 
Replace all 0’s with 1 in a given integer

Can a number be expressed as a sum of two prime numbers

Count possible decoding of a given digit sequence

Python code
Run
def findGCD(n1, n2):
    gcd = 0
    for i in range(1, int(min(n1, n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd


# input first fraction
num1, den1 = map(int, list(input("Enter numerator and denominator of first number : ").split(" ")))

# input first fraction
num2, den2 = map(int, list(input("Enter numerator and denominator of second number: ").split(" ")))

lcm = (den1 * den2) // findGCD(den1, den2)

sum = (num1 * lcm // den1) + (num2 * lcm // den2)

num3 = sum // findGCD(sum, lcm)

lcm = lcm // findGCD(sum, lcm)

print(num1, "/", den1, " + ", num2, "/", den2, " = ", num3, "/", lcm)
Output
Enter numerator and denominator of first number : 14 10
Enter numerator and denominator of second number: 24 3
14 / 10 + 24 / 3 = 47 / 5
