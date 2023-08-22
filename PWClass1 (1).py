#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Declare two variables, `x` and `y`, and assign them integer values. Swap the
# values of these variables without using any temporary variable.
# 2. Create a program that calculates the area of a rectangle. Take the length and
# width as inputs from the user and store them in variables. Calculate and
# display the area.
# 3. Write a Python program that converts temperatures from Celsius to
# Fahrenheit. Take the temperature in Celsius as input, store it in a variable,
# convert it to Fahrenheit, and display the result.

# 1. Write a Python program that takes a string as input and prints the length of
# the string.
# 2. Create a program that takes a sentence from the user and counts the number
# of vowels (a, e, i, o, u) in the string.
# 3. Given a string, reverse the order of characters using string slicing and print
# the reversed string.
# 4. Write a program that takes a string as input and checks if it is a palindrome
# (reads the same forwards and backwards).
# 5. Create a program that takes a string as input and removes all the spaces from
# it. Print the modified string without spaces.


# In[26]:


#Q1
x = 12
y = 99
x = x+y
y = x-y
x=x-y
x,y


# In[3]:


#q2
def area():
    x=int(input())
    y=int(input())
    z=x*y
    return print(f"Area is {z}")
area()


# In[4]:


#q3
def temp(celcius):
    fah =celcius*(9/5)+32
    return fah
temp(-41)


# In[5]:


#q1
x = input()
print(len(x))


# In[7]:


#q2
vowel ="aeiou"
x= input()
c=0
for i in vowel:
    if i in x:
        c=c+1
print(c)


# In[16]:


#q3
a =list(input())
b=a[::-1]
b


# In[21]:


x=input()
if x==x[::-1]:
    print("Pallindrom")
else:
    print("Not Pallindrom")


# In[25]:


x=input()
x.replace(" ","")

