#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[3]:


#1

x="Anivesh"
x[::-1]


# In[6]:


#2
x="Anivesh"
if x==x[::-1]:
    print("yes")
else:
    print("No")


# In[9]:


#3 and #4
x.upper(),x.lower()


# In[11]:


#5
def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define the list of vowel characters
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

user_input = input("Enter a string: ")
result = count_vowels(user_input)
print("Number of vowels:", result)


# In[13]:


#q6
def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define the list of vowel characters
    vowel_count = 0

    for char in input_string:
        if char not in vowels:
            vowel_count += 1

    return vowel_count

user_input = input("Enter a string: ")
result = count_vowels(user_input)
print("Number of vowels:", result)


# In[22]:


#q7
x="Anivesh"
x.index(x[-1])


# In[24]:


#Q8
x= "   How    are   You  "
x.replace(" ","")


# In[30]:


#q9
search ="on"
Word =" My book is on the table"
search in Word


# In[37]:


#q10
x="My name is Anivesh"
x.replace("Anivesh","Arijit")


# In[196]:


# 11. Count the occurrences of a word in a string.
x="My name is Arijit Singh Arijit is best"
x.count("Arijit")
# 12. Find the first occurrence of a word in a string.
x="My name is Arijit Singh Arijit is best"
x.find("Arijit")
# 13. Find the last occurrence of a word in a string.
x="My name is Arijit Singh Arijit is best"
x.rfind("M")

# 14. Split a string into a list of words.
x  = "anni ffsfs ds sfs fsf "
y = x.split(" ")
y
# 15. Join a list of words into a string.
" ".join(y)
# TOPIC: String Based Assignment Problem
# 16. Convert a string where words are separated by spaces to one where words
# are separated by underscores.
para = "India is the best country in the world"
para =para.replace(" ","_")
para
# 17. Check if a string starts with a specific word or phrase.
para.startswith("I")
# 18. Check if a string ends with a specific word or phrase.
para.endswith("I")
# 19. Convert a string to title case (e.g., "hello world" to "Hello World").
para.title()
# 20. Find the longest word in a string.
l=para.split("_")
x=""
for i in l:
    
    if len(i)>len(x):
        x=i
x


# In[207]:


# 21. Find the shortest word in a string.
text = "Hahah what a from the considenn ce ithe room of the ogtyhanfnf"
s = list(text.split(" "))
d={}
x=""
for i in s:
    if len(i)>len(x):
        x=i
print(f"{x}",len(i))


# In[209]:


# 22. Reverse the order of words in a string.
text[::-1]


# In[215]:


# 23. Check if a string is alphanumeric.
text ="Anivesis1"
text.isalnum()


# In[230]:


# 24. Extract all digits from a string.
text ="anivesh 1223 d dsa34342"
x=[]
pattern ="^\d+$"
for i in text:
    if re.match(pattern,i):
        x.append(i)
x      


# In[233]:


# 25. Extract all alphabets from a string.
text ="anivesh 1223 d dsa34342"
x=[]
pattern =r"^[a-zA-Z]+$"
for i in text:
    if re.match(pattern,i):
        x.append(i)
x


# In[239]:


# 26. Count the number of uppercase letters in a string.
text ="anivesQQQQh 1223 d AAdsBBa34JJ342"
t =[]
for i in text:
    if i.isupper():
        t.append(i)
list(set(t))
        
# 27. Count the number of lowercase letters in a string.
text ="anivesQQQQh 1223 d AAdsBBa34JJ342"
t =[]
for i in text:
    if i.islower():
        t.append(i)
list(set(t))


# In[243]:


# 28. Swap the case of each character in a string.
text ="anivesQQQQh 1223 d AAdsBBa34JJ342"
text.swapcase()


# In[250]:


# 29. Remove a specific word from a string.
text
text.replace("aniv","")


# In[251]:


# 30. Check if a string is a valid email address

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Test cases
print(is_valid_email("example@example.com"))  # True
print(is_valid_email("invalid.email"))       # False


# In[47]:


# 31. Extract the username from an email address string.
name = "anivesh@gmail.com"
name.split("@")[0]


# In[50]:


# 32. Extract the domain name from an email address string.
name = "anivesh@gmail.com"
name.split("@")[1]


# In[60]:


# 33. Replace multiple spaces in a string with a single space.
para = "my name is akon  but    peaople  call   me  singer"
import re
para = re.sub(r'\s+',' ',para)
para


# In[91]:


# 34. Check if a string is a valid URL.
mail  = "1ani@gmail.com"
# mail[len(mail)-4:]
# mail.find("@")
# mail.startswith
pattern = r"^[a-zA-Z]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
print(re.match(pattern,mail))



# In[104]:


# 35. Extract the protocol (http or https) from a URL string.
url ="https://learn.pwskills.com/lesson/13th-Aug'23-:-Introduction-to-Data-Science/64d8bec2786814535e1d392b/course/Full-Stack-Data-Science-Pro/64a264076977ccc0a0e20c13"
re.search(r"https://",url)


# In[136]:


# 36. Find the frequency of each character in a string.
name = "My name is Aniveshhhh"
u = list(set(name))
# Initialize an empty dictionary to store the character frequencies
char_frequency = {}
for char in name:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
# for i in name:
#     print(f"{i} is",name.count(i))


# In[156]:


# 37. Remove all punctuation from a string.
text = "My %#name\$! is @."
pattern = r"[^\w\s]"
re.sub(pattern,"",text)


# In[167]:


# 38. Check if a string contains only digits.
text ="12344554"
# pattern = r"[^\d]"
pattern = r"^\d+$"
# re.sub(pattern,"",text)
if re.match(pattern, text):
    print("Num")
else:
    print("Char")


# In[194]:


# 39. Check if a string contains only alphabets.
pattern = r"^[a-zA-Z ]+$"
text ="Anivesh is good"
if re.match(pattern,text):
    print("True")
else:
    print("False")



# In[252]:


# 40. Convert a string to a list of characters
text ="Anivesh is "
list(text)


# In[266]:


# 41. Check if two strings are anagrams.
x="sasha"
y="aassh"
for i in x:
    if i in y:
        print("YEs")
    else:
        print("no")


# In[267]:


# 42. Encode a string using a Caesar cipher.
x=""
text ="This is secret Password"
for i in text:
    if i.isalpha():
        ascii_offset  = 65 if i.isupper() else 97
# 43. Decode a Caesar cipher encoded string.
# 44. Find the most frequent word in a string.


# In[271]:


# 45. Find all unique words in a string.
l =list(text)
set(l)


# In[285]:


# 46. Count the number of syllables in a string.
text = "Embarking on an interstellar journey, we unlock the universe's mysteries, from distant galaxies to black holes, igniting human curiosity. Our technological advancements and unyielding spirit fuel this exploration, revealing cosmic marvels and fostering global collaboration. As we delve deeper, we uncover insights into our own existence, fostering unity and humility. The boundless expanse beckons us to question, dream, and discover, propelling humanity toward a brighter cosmic future"
import pyphen
# !pip install pyphen
dic =pyphen.Pyphen(lang="en")
word =text.split(" ")
syllables = dic(word)


# In[311]:


# 47. Check if a string contains any special characters.
text ="Anivesh as ff"
pattern = re.compile('[!@#$%^&*()_+{}\[\]:;<>,.?~]')
for i in list(text.split(" ")):
    if pattern.search(i):
        print("Yes")
    else:
        print("No")


# In[338]:


# 48. Remove the nth word from a string.
text ="one that will removed is remove"
text =text.split(" ")
text[0]=""
text


# In[1]:


# 49. Insert a word at the nth position in a string.
text ="one that will removed is remove"
text =text.split(" ")
text[0]="two"
text


# In[11]:


# 50. Convert a CSV string to a list of lists.
x ="ani,mni,sunnu,dunnu,lunnu"
import csv
from io import StringIO
y=StringIO(x)
csv_reader = csv.reader(y)
list =[row for row in csv_reader]
list


# In[16]:


# List Based Practice Problem :
# 1. Create a list with integers from 1 to 10.
import numpy as np
np.linspace(1,10,10)


# In[44]:


# 2. Find the length of a list without using the `len()` function.
x=[1,2,3,4,5,6,4,5,6,100,12,34,21,23]
x.index(x[-1])
# n=0
# for i in x:
#     n=n+1
# n


# In[56]:


# 3. Append an element to the end of a list.
x=[1,2,3,4,5,6,4,5,6,100,12,34,21,23]
x.append("1")


# In[66]:


# 4. Insert an element at a specific index in a list.
x=[1,2,3,4,5,6,4,5,6,100,12,34,21,23]
x.insert(1,"An")
x


# In[70]:


# 5. Remove an element from a list by its value.
x.remove(1)
x


# In[71]:


# 6. Remove an element from a list by its index.
x.remove(x[-1])
x


# In[72]:


# 7. Check if an element exists in a list.
"An" in x


# In[73]:


# 8. Find the index of the first occurrence of an element in a list.
x.index("An")


# In[86]:


# 9. Count the occurrences of an element in a list.
x=[1,1,22,33,44,"a","a","b",1]
d={}
for i in x:
    d[i]=x.count(i)
d


# In[87]:


# 10. Reverse the order of elements in a list
x[::-1]


# In[92]:


# 11. Sort a list in ascending order.
x=[1,2,2,1,2,333,443,1]
x.sort(reverse=False)
x


# In[112]:


# 12. Sort a list in descending order.
x=[1,2,2,1,2,333,443,1]
x.sort(reverse=True)
x


# In[114]:


# 13. Create a list of even numbers from 1 to 20.
[x for x in range(0,21) if x%2==0]


# In[116]:


# 14. Create a list of odd numbers from 1 to 20.
[x for x in range(0,21) if x%2!=0]


# In[120]:


# 15. Find the sum of all elements in a list.
x=[1,2,3,4,5]
np.sum(x)



# In[123]:


# 16. Find the maximum value in a list.
x
np.max(x)


# In[125]:


# 17. Find the minimum value in a list.
np.min(x)


# In[127]:


# 18. Create a list of squares of numbers from 1 to 10.
[x*x for x in range(1,11)]


# In[137]:


# 19. Create a list of random numbers.
# 20. Remove duplicates from a list.
x=[1,1,1,2,3,4,5,56,6,6,54]
set(x)


# In[151]:


# 21. Find the common elements between two lists.
x=[1,1,1,2,3,4,5,56,6,6,54]
y =[1,2,3,4,5,6,4,56]
l=[]
for i in x:
    if i in y:
        l.append(i)
print(set(l))        


# In[163]:


# 22. Find the difference between two lists.
x=[1,1,1,2,3,4,5,56,6,6,54]
y =[1,2,3,4,5,6,4,56]
l=[]
for i in x:
    if i not in y:
        l.append(i)
print(set(l)) 


# In[165]:


# 23. Merge two lists.
x+y


# In[167]:


# 24. Multiply all elements in a list by 2.
x*2


# In[11]:


# 25. Filter out all even numbers from a list.
# 26. Convert a list of strings to a list of integers.
x=[[1,2,3,4],[1,2,3,4],1,2,3,4,55,66]

# 27. Convert a list of integers to a list of strings.
x=[1,2,3,4]
str(x)
# 28. Flatten a nested list.
x=[1,2,3,[11,12,1,3,[111,33,444]]]
y=str(x)
y=y.replace("[","")
y.replace("]","")


# In[25]:


# 29. Create a list of the first 10 Fibonacci numbers.
x=[0,1]
y=[]
temp =0
for i in range(2,10):
    temp=x[i-1]+x[i-2]
    x.append(temp)
x


# In[31]:


# 30. Check if a list is sorted.
x=[2,3,4,3,222,23,4]
for i in range(len(x)-1):
    if x[i]<x[i+1]:
        print("Yes")
    else:
        print("No")


# In[36]:


# 31. Rotate a list to the left by `n` positions.
x=[1,2,3,4,5,6,7,8,9,10]
y=x[:5]
z=x[5:]
y[::-1]+z
# 32. Rotate a list to the right by `n` positions.


# In[54]:


# 33. Create a list of prime numbers up to 50.
for num in range(2,51):
    if num >1:
        for j in range(2,num-1):
            if num%j==0:
                break
            else:
                continue


# 34. Split a list into chunks of size `n`.


# In[72]:


# 35. Find the second largest number in a list.
x=[1,2,99,4,5,100]
import numpy as np
x.remove(np.max(x))
np.max(x)


# In[74]:


# 36. Replace every element in a list with its square.
x=[1,2,3,4]
np.square(x)


# In[78]:


# 37. Convert a list to a dictionary where list elements become keys and their
# indices become values.
x=[1,2,3,4,56,7]
d={}
for i in x:
    d[i]=x.index(i)
d


# In[81]:


# 38. Shuffle the elements of a list randomly.
x=[1,2,3,4,56,7,22,22,11,3,100,4,4]
import random
random.shuffle(x)
x


# In[86]:


# 39. Create a list of the first 10 factorial numbers.
l =[]
for i in range(2,500):
    if 50%i==0:
        l.append(i)
l


# In[89]:


# 40. Check if two lists have at least one element in common.
x=[1,2,3,4,5]
y=[2,33,44,33,5]
set(x).intersection(set(y))


# In[92]:


# 41. Remove all elements from a list.
x.clear()
x


# In[94]:


# 42. Replace negative numbers in a list with 0.
x=[1,-2,4,5,-6]
x=[0 for i in x if i<0]
x


# In[96]:


# 43. Convert a string into a list of words.
x="My name is Anivesh"
x.split(" ")


# In[99]:


# 44. Convert a list of words into a string.
l=['My', 'name', 'is', 'Anivesh']
' '.join(l)


# In[108]:


# 45. Create a list of the first `n` powers of 2
x=[1,2,3,4,5]
l=[]
for i in range(1,5):
    l.append(i**x[i])
l


# In[112]:


# 46. Find the longest string in a list of strings.
x=["Anivesh","is","Goooooood","Boy"]
for i in x:
    print(len(i))
# 47. Find the shortest string in a list of strings.


# In[118]:


# 48. Create a list of the first `n` triangular numbers.
l=[]
for i in range(1,50):
    n=i*(i+1)//2
    l.append(n)



# In[119]:


# 49. Check if a list contains another list as a subsequence.


# In[122]:


# 50. Swap two elements in a list by their indices.
# done already above
# 1. Create a tuple with integers from 1 to 5.
t=(1,2,3,4,5)
t


# In[124]:


# 2. Access the third element of a tuple.
t=(1,2,3,4,5)
t[2]


# In[137]:


# 3. Find the length of a tuple without using the `len()` function.
t=(1,2,3,4,5)
t.index(t[-1])


# In[141]:


# 4. Count the occurrences of an element in a tuple
t=(1,2,3,4,5,6,7,7,7,8,8,9)
t.count(7)


# In[143]:


# 5. Find the index of the first occurrence of an element in a tuple.
t=(1,2,3,4,5,6,7,7,7,8,8,9)
t.index(1)


# In[146]:


# 6. Check if an element exists in a tuple.


# In[151]:


t=(1,2,3,4,5,6,7,7,7,8,8,9)
t=list(t)
print(t)


# In[153]:


# 8. Convert a list to a tuple.
x=[1,2,3,4]
tuple(x)


# In[157]:


# 9. Unpack the elements of a tuple into variables.
t=(1,2,3)
x1,x2,x3=t
x1


# In[159]:


# 10. Create a tuple of even numbers from 1 to 10.
x= tuple(x for x in range(1,10) if x%2!=0)
x


# In[173]:


for i in range():
    for j in range(i+1):
        print(j,end="")
    print()


# In[196]:


for i in range(5,0,-1):
    print("*"*i)
for i in range(6):
    print("*"*i)
    


# In[214]:


x= "education is the key to sucess"
l= x.split(" ")
str(l[::-1])


# In[219]:


x=[1,2,3,4,5,7,8]
x[0]=x[0]+x[2]
x[2] = x[0]-x[2]
x[0]= x[0]-x[2]
x


# In[1]:


a=10
b=12
a,b=b,a
a,b


# In[13]:


# 11. Create a tuple of odd numbers from 1 to 10.
x= tuple(i for i in range(1,11) if i%2!=0)
x
# 12. Concatenate two tuples.
x=()
y=(6,6,8)
x+y
# 13. Repeat a tuple three times.
3*x
# 14. Check if a tuple is empty.
x=""
if x=="":
    print("es")
else:
    print("No")


# In[15]:


# 15. Create a nested tuple.
x=(1,2,3,4,(1,2,3,4))
x


# In[20]:


# 16. Access the first element of a nested tuple.
x=(1,2,3,4,(1,2,3,4))
x[4][0]


# In[25]:


# 17. Create a tuple with a single element.
x=(1,)
type(x)


# In[27]:


# 18. Compare two tuples.
x==y


# In[38]:


# 19. Delete a tuple.
x=(1,2,3,4,5)
del x



# In[40]:


# 20. Slice a tuple.
x=(1,2,3,4,5,6)
x[3:]


# In[45]:


# 21. Find the maximum value in a tuple.
max(x)
# 22. Find the minimum value in a tuple.
min(x)
# 23. Convert a string to a tuple of characters.
x = "Anivesh is my name"
tuple(x)


# In[49]:


# 24. Convert a tuple of characters to a string.
"".join(x)


# In[52]:


# 25. Create a tuple from multiple data types.
x=(1,2,3,"Ani",True,"1")
x


# In[54]:


# 26. Check if two tuples are identical.
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (3, 2, 1)

print(tuple1 == tuple2)  # Output: True (tuples are identical)
print(tuple1 == tuple3)  # Output: False (tuples are not identical)


# In[61]:


# 27. Sort the elements of a tuple.
t =(22,3,4,1,3)
tuple(sorted(list(t)))


# In[68]:


# 28. Convert a tuple of integers to a tuple of strings.
t =(1,2,3,4,5,6,7)
t=tuple(str(i) for i in t)
t


# In[71]:


# 29. Convert a tuple of strings to a tuple of integers.
t=tuple(int(i) for i in t)
t


# In[73]:


# 30. Merge two tuples.
t+x


# In[89]:


# 31. Flatten a nested tuple.
t=(1,2,3,4,(22,33,44,(44,5,5)))
x=[]
for i in t:
x.extend(i)
tuple(x)


# In[92]:


# 32. Create a tuple of the first 5 prime numbers.
x=[]
for num in range(1,20):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                x.append(num)
set(x)
            


# In[94]:


# 33. Check if a tuple is a palindrome.
x=(1,2,1,2,1)
x==x[::-1]


# In[98]:


# 34. Create a tuple of squares of numbers from 1 to 5.
import numpy as np
np.square(x)


# In[101]:


x=(1,2,3,4,5,6,7,8,9,10)
x=tuple(i for i in x if i%2!=0)
x


# In[110]:


# 37. Create a tuple of random numbers.
import random
t= tuple(random.randint(1,1000) for _ in range(7))
t
# 38. Check if a tuple is sorted.
sorted(list(t))


# In[117]:


# 39. Rotate a tuple to the left by `n` positions.
x=(1,2,3,4,5,6,11,22,33,55)
x[2:]+x[:2]


# In[122]:


# 40. Rotate a tuple to the right by `n` positions.
x[:len(x)-2]+x[len(x)-2:]


# In[143]:


# 41. Create a tuple of the first 5 Fibonacci numbers.
x=[0,1]
l=[]
temp=0
for i in range(2,10):
    temp =x[i-1]+x[i-2]
    x.append(temp)
tuple(x)

# 42. Create a tuple from user input.
# 43. Swap two elements in a tuple.
# 44. Reverse the elements of a tuple.
# 45. Create a tuple of the first `n` powers of 2.
# 46. Find the longest string in a tuple of strings.
# 47. Find the shortest string in a tuple of strings.
# 48. Create a tuple of the first `n` triangular numbers.
# 49. Check if a tuple contains another tuple as a subsequence.
# 50. Create a tuple of alternating 1s and 0s of length `n`.


# In[ ]:


## 42. Create a tuple from user input.
x = tuple(map(int, input().split()))
x


# In[1]:


# 43. Swap two elements in a tuple.
# 44. Reverse the elements of a tuple.
# 45. Create a tuple of the first `n` powers of 2.
t =(1,2,3,4,5,6,7)
x=[]
for i in t:
    print(2**i)


# In[5]:


# 46. Find the longest string in a tuple of strings.
t =("wwwwwwwww","aa","freddffssdffaaaa","e43e")
max(t)


# In[9]:


# 47. Find the shortest string in a tuple of strings.
min(t)
# 48. Create a tuple of the first `n` triangular numbers.


# In[15]:


# 49. Check if a tuple contains another tuple as a subsequence.

# 50. Create a tuple of alternating 1s and 0s of length `n`
t=tuple()
for i in range(11):
    t=t+(i,)


# In[21]:


# 1. Create a set with integers from 1 to 5.
s=set()
type(s)
s={1,2,3,4,5}
s
# 2. Add an element to a set.
s.add("Anivesh")
s


# In[24]:


# 3. Remove an element from a set.
s.remove(1)
s



# In[33]:


# 4. Check if an element exists in a set.
1 in s
# 5. Find the length of a set without using the `len()` function.
c=0
s={1,2,3,4,5,6,7,8}
for _ in s:
    c=c+1
c


# In[35]:


# 6. Clear all elements from a set.
s.clear()
# 7. Create a set of even numbers from 1 to 10.
# 8. Create a set of odd numbers from 1 to 10.


# In[38]:


# 9. Find the union of two sets.
s={1,2,3,4,56}
t={22,23,44}
s.union(t)


# In[42]:


# 10. Find the intersection of two sets.
s={1,22,3,4,56}
t={22,23,44}
s.intersection(t)


# In[44]:


# 11. Find the difference between two sets.
s-t


# In[46]:


# 12. Check if a set is a subset of another set.
# 13. Check if a set is a superset of another set.
# 14. Create a set from a list.
l=[1,2,3,4]
set(l)


# In[47]:


# 15. Convert a set to a list
l=[1,2,3,4]
list(set(l))


# In[50]:


# 16. Remove a random element from a set.
s.pop()


# In[56]:


# 17. Pop an element from a set.
s ={1,2,3,4,5}
s.remove(5)


# In[60]:


# 18. Check if two sets have no elements in common.
# 19. Find the symmetric difference between two sets.
# 20. Update a set with elements from another set.
s={1,2,3,4,5,6}
t={1,1,2,2,3,3,4,4,4,4,4444,44}
s.update(t)
s



# In[63]:


# 50. Merge multiple sets into one.

s={1,2,3,4,5,6}
t={1,1,2,2,3,3,4,4,4,4,4444,44}
s.union(t)

