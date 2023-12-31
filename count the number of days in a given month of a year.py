#Method Discussed :

'''Method 1: Using if-else ladder'''
'''Method 2 : Using Array'''

----------------------------------------------------------------'''Method 1: Using if-else ladder'''----------------------------------------------------------------
#Check if the given month is February. 
#If True Check if the year is a year leap or not.
#If year is a leap year Print 29 Days, Else Print 28 Days.
#If Condition in Step 3 is False Check the month. 
#Print the number of days assigned to specific Month.


'''Method 1 : Code in Python'''

month = 12
year=2012
    
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29");

elif(month==2) :
    print("Number of days is 28");

elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("Number of days is 31");

else :
    print("Number of days is 30");
    
Output
Number of days is 31



----------------------------------------------------------------'''Method 2 : Using Array'''----------------------------------------------------------------

#In this method instead of using if-else-if ladder or switch case, we use array.

arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month = 12
year=2012
    
if(month==2 and ((year%400==0) or ((year%100!=0) and (year%4==0)))) :
    print("Number of days is ", arr[month-1]+1)
    
else :
    print("Number of days is ", arr[month-1]);
    
Output
Number of days is 31
