#!/usr/bin/env python
# coding: utf-8

# In[5]:


### Challenge Level:
# 31. Create a program that validates a password based on complexity rules (length, characters, etc.).
import re
x=""
pattern = r"[!@$%^&*()_+{}\[\]:;<>,.?~\\]"
pwrd = "AniveshhhhH"
for i in pwrd:
    if len(pwrd)>=8 and pwrd[0].isupper()==True and pwrd[-1].isupper()==True:
        if re.search(pattern,i):
            x="Valid"
        else:
            x="Not Valid"
  

# 32. Develop a program that performs matrix addition and subtraction based on user input
x,y=map(int,input().split())
l1=[]
for i in range(1,x+1):
    l2=[]
    for j in range(1,y+1):
        l2.append(j)
    l1.append(l2)
    
x,y=map(int,input().split())
l3=[]
for i in range(1,x+1):
    l4=[]
    for j in range(1,y+1):
        l4.append(j)
    l3.append(l4)


# In[6]:


l1,l3


# In[9]:


def mix(x, y, *b, **a):
    # Initialize sum
    total = 0

    # Sum the values in *b
    for i in b:
        total += i
        print("Sum:", total)

    # Print the keyword arguments in **a
    for key, value in a.items():
        print(key, value)

    # Print positional args
    print("Positional args are", x, y)

# Example usage
mix("An", "ab", 11111, 223, 44455, name="Anivesh", sal="100000000000")


# In[14]:


# lambda function
x=lambda : print("Hello World")
x()


# In[16]:


s=lambda a,b:a+b
s(1,2)


# In[18]:


m = lambda a,b:a*b
m(10,23)


# In[20]:


a =int(input("Enter number"))
b=int(input("second number"))
sqr = lambda a,b:(a**2,b**2)
sqr(a,b)


# In[32]:


ev = lambda a:True if a%2==0 else False
ev(13)


# In[39]:


g = lambda x,y : x if x>y else y
g(21,16)


# In[42]:


g = lambda x,y,z : x if x>y and x>z else z
g(21,1600,211)


# In[50]:


product =[
{"name":"product21","price":50},
    {"name":"product2","price":40},
    {"name":"product32","price":30},
    {"name":"product4","price":20}    
]


# In[53]:


sort = sorted(product,key=lambda x:x["name"],reverse=False)
for i in sort:
    print(i)


# In[77]:


vow =["a","e","i","o","u","A","E","I","O","U"]
cha="Anivesheioreoe"
d=lambda x:[i for i in cha if i in vow]
d(cha)


# In[80]:


d=lambda x:(" ".join(i for i in cha if i in vow))
d(cha)


# In[104]:


# 33. Write a program that calculates the greatest common divisor (GCD) of two numbers using the Euclidean 
# algorithm.
# a,b = map(int,(input().split(" ")))
a=40
b=90
l1=[]
for i in range(a,b+1):
    if a%i==0:
        l1.append(i)
l2=[]
for j in range(1,b+1):
    if b%j==0:
        l2.append(j)
l1,l2

# 34. Build a program that performs matrix multiplication using nested loops and conditional statements.

# 35. Create a program that simulates a basic text-based tic-tac-toe game against the computer.

# 36. Write a program that generates Fibonacci numbers up to a specified term using iterative methods.

# 37. Develop a program that calculates the nth term of the Fibonacci sequence using memoization.

# 38. Create a program that generates a calendar for a given month and year using conditional statements.

# 39. Build a program that simulates a basic text-based blackjack game against the computer.

# 40. Write a program that generates the prime factors of a given number using trial division.


# In[107]:


#  Write a Python program to check if a given number is positive or negative.
x=-12
y=["-ve" if x<0 else "+ve"]
y


# In[110]:


# 2. Create a program that determines if a person is eligible to vote based on their age.
x=17
y=["Eligible" if x>=18 else "No"]
y


# In[115]:


# 3. Develop a program to find the maximum of two numbers using if-else statements.
x=10
y=300
z=[x if x>y else y]
z



# In[120]:


# 4. Write a Python script to classify a given year as a leap year or not.
x=2011

if x%400==0 or ( x%100!=0 and x%4==0):
    print("Leap")
else:
    print("No Leap")


# In[124]:


# 5. Create a program that checks whether a character is a vowel or a consonant.
c="aeiouAEIOU"

x="d"
if x in c:
    print("Vow")
else:
    print("No")


# In[127]:


# 6. Implement a program to determine whether a given number is even or odd.
x=1
y=["even" if x%2==0 else "odd"]
y


# In[132]:


# 7. Write a Python function to calculate the absolute value of a number without using the `abs()` function.
def ab(n):
    if n==0:
        return "No 0 Plzzzz"
    elif n<0:
        n=-n
        return n
    else:
        return n
ab(-11
  )


# In[143]:


# 8. Develop a program that determines the largest of three given numbers using if-else statements.
x,y,z=110,2,10
g=[x if x>y and x>z else(y if y>z else z)]
g


# In[147]:


# 9. Create a program that checks if a given string is a palindrome.
x="JAHAJI"
x==x[::-1]


# In[156]:


# 10. Write a Python program to calculate the grade based on a student's score
# A=1,10
# B=11,20
# C=21,30
m = 21
x=["A" if m >=0 and m<11 else ("B" if m>=11 and m<21 else "C")]
x


# In[158]:


# Nested If-Else Statements:
# 11. Write a program to find the largest among three numbers using nested if-else statements.
x,y,z=110,2,10
g=[x if x>y and x>z else(y if y>z else z)]
g


# In[160]:


# 12. Implement a program to determine if a triangle is equilateral, isosceles, or scalene.
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
triangle_type(11,11,10)


# In[162]:


# 13. Develop a program that checks if a year is a leap year and also if it is a century year.
x=2011

if x%400==0 or ( x%100!=0 and x%4==0):
    print("Leap")
else:
    print("No Leap")



# In[167]:


# 14. Write a Python script to determine if a number is positive, negative, or zero.
x=100
if x<0:
    print("-ve")
elif x>0:
    print("+ve")
else:
    print("0")
# 15. Create a program to check if a person is a teenager (between 13 and 19 years old).
# 16. Develop a program that determines the type of angle based on its measure (acute, obtuse, or right).



# In[1]:


# 17. Write a Python program to calculate the roots of a quadratic equation.
import math
# Input coefficients a, b, and c from the user
a =10
b =20 
c =40
d=(b**2)-4*(a*c)
if d>0:
    r1=(-b+math.sqrt(d))//2*a
    r2=(-b-math.sqrt(d))//2*a
else:
    print("d is 0")

    

# 18. Implement a program to determine the day of the week based on a user-provided number (1 for Monday, 2 
# for Tuesday, etc.).

# 19. Create a program that determines if a year is a leap year and also if it is evenly divisible by 400.

# 20. Develop a program that checks if a given number is prime or not using nested if-else statements.


# In[8]:


# Implement a program to determine the day of the week based on a user-provided number (1 for Monday, 2 
# for Tuesday, etc.)
d={1:"M",2:"T",3:"W",4:"T",5:"F",6:"S"}
x=int(input("Enter Day.No"))
for key,val in d.items():
    if x==key:
        print(val)
    else:
        None
    


# In[11]:


# 19. Create a program that determines if a year is a leap year and also if it is evenly divisible by 400
x=2000

if x%400==0 or (x%100==0 and x%4==0):
    print("Yes")
else:
    print("No")


# In[38]:


# 20. Develop a program that checks if a given number is prime or not using nested if-else statements.
x=15
c=0
d=0
for i in range(2,x-1):
    if x%i==0:
        c=c+1
    else:
        d=d+1
if c>0:
    print("No")
else:
    print("yes")


# In[52]:


# Elif Statements:
# 21. Write a Python program to assign grades based on different ranges of scores using elif statements.

# 22. Implement a program to determine the type of a triangle based on its angles.

# 23. Develop a program to categorize a given person's BMI into underweight, normal, overweight, or obese using 
# elif statements.

# 24. Create a program that determines whether a given number is positive, negative, or zero using elif 
# statements.

# 25. Write a Python script to determine the type of a character (uppercase, lowercase, or special) using elif 
# statements.
x="T"
s="@#$%^&*"
if x in s:
    print("Special")
else:
    if x.isupper():
        print("Upper")
    elif x.islower():
        print("Lower")
# 26. Implement a program to calculate the discounted price based on different purchase amounts using elif 
# statements.

# 27. Develop a program to calculate the electricity bill based on different consumption slabs using elif 
# statements.

# 28. Create a program to determine the type of quadrilateral based on its angles and sides using elif 
# statements.

# 29. Write a Python script to determine the season based on a user-provided month using elif statements.

# 30. Implement a program to determine the type of a year (leap or common) and month (30 or 31 days) using 
# elif statements.


# In[53]:


"#" in s


# In[90]:


# Intermediate Level:
# 11. Write a program that calculates the roots of a quadratic equation .
a,b,c=11,200,20
import math
import numpy as np
d=b*b-4*a*c
if d>0:
    x1=-b+np.sqrt(d)/a
    x2=-b-np.sqrt(d)/a
    
print(x1,x2)
a,b,c
# 12. Create a program that determines the day of the week based on the day number (1-7).

# 13. Develop a program that calculates the factorial of a given number using recursion.
def fact(n):
    if n==0:
        return 1
    else: 
        return n*fact(n-1)
fact(4)
# 14. Write a program to find the largest among three numbers without using the `max()` function.
a,b,c=12,21,10
x=lambda a,b,c:a if a>b and a>c else (b if b>c else c )
r=x(21,10,43)
r

# 15. Create a program that simulates a basic ATM transaction menu.

# 16. Build a program that checks if a given string is a palindrome or not.

# 17. Write a program that calculates the average of a list of numbers, excluding the smallest and largest values.
x=[1,21,2,3,4,55,67,65,100]
x.remove(min(x))
np.mean(x)

# 18. Develop a program that converts a given temperature from Celsius to Fahrenheit.

# 19. Create a program that simulates a basic calculator for addition, subtraction, multiplication, and division.

# 20. Write a program that determines the roots of a cubic equation using the Cardano formula


# In[1]:


# Advanced Level:
# 21. Create a program that calculates the income tax based on the user's income and tax brackets.

# 22. Write a program that simulates a rock-paper-scissors game against the computer.
import random
l=["r","p","s"]
x=random.choice(l)
s=input("Enter the r,p,s")
if x==s:
    print("Draw")
elif x=="r" and s=="p" or (s=="r" and x=="p"):
    print("Papar")
elif (x=="s" and s=="p") or (s=="s" and x=="p"):
    print("scissor")
else:
    print("rock")



# In[46]:


# 23. Develop a program that generates a random password based on user preferences (length, complexity).
x=10
y=0
l=[]
s=""
for i in range(1,x+1):
    y=random.randint(1,i+1)
    l.append(y)
for i in l:
    s=s+str(i)
int(s)
   
# 24. Create a program that implements a simple text-based adventure game with branching scenarios.
def game():
    print("Where do you wanna go")
    i = input().lower()
    if i=="delhi":
        Delhi()
    elif i=="mumbai":
        Mumbai()
    else:
        print("Invalid Input")
def Delhi():
    print("Welcome to delhi, do wanna go India gate or CP")
    d=input().lower()
    if d=="India Gate":
        print("welcome to India Gate")
    else:
        print("Welcome to CP")
def Mumbai():
    print("Welcome to Mumbai, do wanna go Taj or Juhu")
    d=input().lower()
    if d=="taj":
        print("welcome to TAJ")
    else:
        print("Welcome to Juhu")
def main():
    game()
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()


# In[60]:


# 25. Build a program that solves a linear equation  for x, considering different cases.
def linear(a,b):
    if a==0:
        print("0 is the root")
        if b==0:
            print("Infinite Solution")
    else:
        x=-b/a
        print(x)
def main():
    linear(10,55)
if __name__ == "__main__":
    main()
    
# 26. Write a program that simulates a basic quiz game with multiple-choice questions and scoring.



# In[106]:


# 27. Develop a program that determines whether a given year is a prime number or not.
l=[]
def prime(n):
    for i in range(2,n):
        if i%2!=0:
            l.append(i)
        for j in l:
            if n%j==0:
                print("Not Prime")
                break
            else:
                print("Prime")
    print(l)
prime(12) 


# In[136]:


# 28. Create a program that sorts three numbers in ascending order using conditional statements.

def sort(a,b,c):
     if a > b:
        a, b = b, a
     if a > c:
        a, c = c, a
     if b > c:
        b, c = c, b
     return a, b, c
print()
sort(1200,11,13)
    



# In[138]:


# 29. Build a program that determines the roots of a quartic equation using numerical methods.

# 30.Write a program that calculates the BMI (Body Mass Index) and provides health recommendations based 
# on the user's input
def BMI(w,h):
    x=w/(h**2)
    return f"BMI is {x} "
BMI(65,17.2)


# In[179]:


# lChallenge Level:
# 31. Create a program that validates a password based on complexity rules (length, characters, etc.).

# 32. Develop a program that performs matrix addition and subtraction based on user input.
x=[[1,2],[3,4]]
y=[[2,3],[1,1]]
l=[[0,0],[0,0]]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        l[i][j]=x[i][j]+y[i][j]
l
        
        

# 33. Write a program that calculates the greatest common divisor (GCD) of two numbers using the Euclidean 
# algorithm.

# 34. Build a program that performs matrix multiplication using nested loops and conditional statements.

# 35. Create a program that simulates a basic text-based tic-tac-toe game against the computer.

# 36. Write a program that generates Fibonacci numbers up to a specified term using iterative methods.
l = [0, 1]

for i in range(1, 11):
    new_element = l[i] + l[i - 1]
    l.append(new_element)

print(l)
  
# 37. Develop a program that calculates the nth term of the Fibonacci sequence using memoization.
l = [0, 1]
n=int(input())
for i in range(1, n):
    new_element = l[i] + l[i - 1]
    l.append(new_element)

print(l[n])


# In[206]:


# 38. Create a program that generates a calendar for a given month and year using conditional statements.
import numpy as np
x=2000
m="D"
l=[]
d1={"J":31,"F":28,"M":31,"A":30,"M":31,"JU":30,"JL":31,"A":31,"S":30,"O":31,"N":30,"D":31}
d2={"J":31,"F":29,"M":31,"A":30,"M":31,"JU":30,"JL":31,"A":31,"S":30,"O":31,"N":30,"D":31}
if x%4==0 and x%400==0:
    print("Leap Year")
    for key,val in d2.items():
        if key==m:
            for i in range(1,val+1):
                print(i,end="\t")
            print()
               
else:
    print("Calender year")
    for key,val in d1.items():
        if key==m:
            for i in range(1,val+1):
                print(i,end="\t")

        
    
    
    
# 39. Build a program that simulates a basic text-based blackjack game against the computer.

# 40. Write a program that generates the prime factors of a given number using trial division.

