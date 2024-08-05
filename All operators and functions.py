#!/usr/bin/env python
# coding: utf-8

# In[8]:


a='Home'


# In[9]:


print((a+"" "")*3)


# In[10]:


print(a*3)


# In[11]:


print((a+""   "")*3)


# In[12]:


print((a+" " " ")*3)


# In[13]:


print(a+str(3)*2)


# In[14]:


print(a+a[3]*2)


# In[15]:


22 % 3


# In[16]:


3*1**3


# In[17]:


num1=10
num2=3


# In[18]:


a = num1 /5


# In[19]:


a


# In[20]:


a>=num2


# In[21]:


import math
b= math.floor(num2/2)


# In[22]:


b


# In[23]:


num1 % num2


# In[24]:


max((num1 *2) , (num2 *2))


# In[25]:


(num1 *2) >= (num2 *2)


# In[26]:


a, b = 10,10 
print(a>=b)   


# In[27]:


print(2 < 3 < 4 < 5)


# In[44]:


3<5 or 50/(5-(3+2))


# In[45]:


10>5 and 7>12 or not 18>3


# In[50]:


print("Match"*False) 


# In[49]:


print("Match"*True)  


# In[51]:


print(1==True) 


# In[52]:


print(0==False)


# In[53]:


print(10==10.0)


# In[56]:


x = int(input("Enter a number"))
x >= 6000 and x<=10000


# In[57]:


x = int(input("Enter a number"))
x % 7 or x.endswith("7") 


# In[60]:


x = int(input("Enter a number"))
x % 7 or str(x).endswith("7") 


# In[61]:


x = int(input("Enter a number"))
x % 7 or str(x).endswith("7") 


# In[65]:


x = int(input("Enter a number"))
x % 7 or str(x).endswith("7") 


# In[66]:


a=[5,6,7]
b=[5,6,7]


# In[68]:


a is b 


# In[71]:


a== b 


# In[72]:


print(5 & 6)


# In[73]:


print('' and "good work")


# In[74]:


print('1' and "good work")


# In[75]:


print('good' and "good work")


# In[76]:


print('0' and "good work")


# In[78]:


print("good work" and "good work")


# In[79]:


print("you are doing good" and "")


# In[80]:


print([] and "you are pythonic")


# In[81]:


print(True and False)


# In[82]:


print(1 and 0)


# In[83]:


print(5 or 6)


# In[84]:


print('' or "Cool")


# In[85]:


print("you are in right direction." or "Data scientist coming soon")


# In[86]:


print(True or False)


# In[91]:


print(1 or 0)


# # IF/ELSE STATEMENTS

# In[33]:


if True:
       print("Im right")
       print("bye")


# In[34]:


if False:
       print("Im right")
print("bye")


# In[36]:


x=3
r= x % 2

if r==0:
    print("Even")
print("bye")
    


# In[43]:


x=7  
r= x % 2

if r==0:
    print("Even")           ##Nested Intentation
    if x>5:
        print("Great")
else:
    print("odd")
    
print("bye")


# In[44]:


x=2  
r= x % 2

if r==0:
    print("Even")
    if x>5:
        print("Great")
else:
    print("odd")
    
print("bye")


# In[64]:


x=5

if x==1:
    print("one")
    
elif x==2:
    print("Two")
    
elif x==3:
    print("Three")
    
else:
    print("Wromg Input")


# In[65]:


temperature = 35
if temperature > 30:
    print("it is warm")
    print("drink water")
print("done")


# In[66]:


temperature = 15
if temperature > 30:
    print("it is warm")
    print("drink water")
print("done")


# In[68]:


age = 22
if age >=18:
    message = "Eligible"
else:
    message = "Not Eligible"
    
print(message)


# In[70]:


age = 12    #short form of above code
message = "eligible" if age>=18 else "Not eligible"
print(message)


# # Membership operator

# In[50]:


str1 = "I have a lazy dog"


# In[51]:


str1


# In[56]:


"dog" in str1


# In[54]:


'lion' in str1


# In[57]:


mylist = [1,3,19,32,48,77]


# In[58]:


65 in mylist


# In[59]:


19 in mylist


# # Identity Operators

# In[60]:


#Compare memory locations of value telling us if the two datapoints have same values as well as same datatype


# In[62]:


a=42
b='42'
a is b   #checks if values and datatype is same


# In[63]:


c = 42
a is c


# # Logical Operators

# In[84]:


a == True


# In[88]:


if a == True:
    print("Eligible")


# In[92]:


high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible")


# In[93]:


high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("not Eligible")


# In[98]:


high_income = False
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")


# In[99]:


high_income = False
good_credit = True
if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")


# In[100]:


high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not Eligible")


# In[101]:


high_income = False
good_credit = True
student = False

if not student:
    print("Eligible")
else:
    print("Not Eligible")


# In[103]:


high_income = True
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("not Eligible")


# In[105]:


high_income = False
good_credit = True
student = False                 # here if the first operator is false, it wont even run the other code nad directly give not eligible while using an 'and' operator
if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("not Eligible")


# In[106]:


high_income = False
good_credit = True
student = False                 # here if any operator is true, it wont even run the other code nad directly give eligible while using an 'or' operator
if (high_income or good_credit) or not student:
    print("Eligible")
else:
    print("not Eligible")


# ## Comparison Operator

# In[120]:


# age should be between 18 and 65
age = 22
if 18 <= age < 65:
        print("Eligible")


# ## While Loop

# In[121]:


i=1
while i<=5:     
    print("Telusko")
    i= i+1  #increment
    


# In[124]:


i=5
while i>=1:
    print("Telusko")
    i= i-1  #decrement
    


# In[125]:


i=5
while i>=1:
    print("Telusko", i)
    i= i-1  #decrement


# In[137]:


i=5
j=1
while i<=1:
    print("Telusko") 
    i= i-1
while j<=4:
    print("Rocks")
    j= j+1


# In[152]:


i=1
while i<=5:
    print("Telusko", end = " ")
    i= i+1
    print()
    j=1
while j<=4:
    print("Rocks", end = " ")
    j= j+1
    
    print()


# # For Loop

# In[154]:


x = ['navin', 65, 2.5]

for i in x:  
    print(i)   


# In[1]:


for i in range(10):  
    print(i)   


# In[2]:


for i in range(11,21,1):   #starting point, ending point, no of iterations
    print(i)   


# In[3]:


for i in range(11,21,2):   #starting point, ending point, no of iterations
    print(i)   


# In[4]:


for i in range(20,11):   #it will give us nothing as range always goes in ascending order
    print(i)   


# In[5]:


for i in range(20,11,-1):   #-1 to go in reverse
    print(i)   


# In[14]:


for i in range(1,21):
    if (i % 5) != 0:
        print (i)


# # BITWISE OPERATORS

# In[15]:


~12  #tilde operator , -13 is a complement of 12


# In[16]:


~41


# In[17]:


~-12


# In[18]:


12 & 13  #Bitwise And operator, if both are 1 then only 1


# In[19]:


12 | 13 #Bitwise OR Operator, if any one of them is 1 then 1


# In[20]:


25 & 30


# In[21]:


12 ^ 13  #XOR opeartor. if both are same them 0 else 1


# In[22]:


25 ^ 13


# In[23]:


10 << 2 #left shift operator, shiting 10 by 2 bits to the left


# In[24]:


10>>2 #Right shift operator, shifting 10 by 2 bits to the right


# # Kwargs

# In[41]:


def person (name, **data) 


# In[42]:


person ('navin', age = 28, city = 'Mumbai', mob = 4703653)


# In[35]:


def person (name, **data):  #double star it means your passing multiple arguments with the help of keywords
    print(name)
    for i, j in data.items():  #to print key and value pair
        print(i,j)
    


# In[36]:


person ('navin', age = 28, city = 'Mumbai', mob = 4703653)


# # Global Vs Local Variable

# In[59]:


a=10
def something():
    a=15
    b=8
    print(a)


# In[60]:


print(a)


# In[70]:


a=10
def something():
    a=15
    print("in function", a)
something()
print("outside",a)


# In[71]:


a=10
def something():
    a=15
    print("in function", a)
something()
print("outside", a)


# In[72]:


a=10
def something():
    print("in function", a)  #we van access gloval variable as local variable
something()
print("outside", a)


# In[73]:


a=10
def something():
    global a  # here we are letting python know that we want to change the global variable to 15
    a=15
    print("in function", a)
something()
print("outside", a)


# In[74]:


a=10
print(id(a))
def something():
  
    x= globals() ['a']
    print("in function", a)
something()
print("outside", a)


# # Lamda

# In[30]:


def square (a):
    return a*a

result = square(5)
print(result)


# In[31]:


square(5)


# In[32]:


f=lambda a:a*a  #functions are objects in python

result = f(5)
print(result)


# In[33]:


f=lambda a,b:a+b  #defining a function with the help of lambda and it is an anonymous finction i.e it does not have a name

result = f(5,6)
print(result)


# In[34]:


def is_even(n):
    return n%2==0
nums = [3,2,6,8,4,6,2,9]

evens = list(filter(is_even,nums))  # filter will give u a list of sequence, is_even is not an in build function, so need to define the function
print(evens)


# In[35]:


nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n:n%2==0,nums))  # reduce the no of lines using lambda
print(evens)  #thus lambda can take any no of arguments, and return 1 expression 


# # Filter Map Reduce  

# In[36]:


#Want to double the no of even numbers received

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n:n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))  #map takes a function and an iterable. so we are using lambda function and evens as iterable

print(doubles)


# In[39]:


#we want to reduce the values, instead of having multiple values, we need 1 value, add all of the above values

from functools import reduce

def add_all(a,b):
    return a+b

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n:n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))  #map takes a function and an iterable. so we are using lambda function and evens as iterable

sum = reduce(add_all,doubles)       #reduce belongs to functools, reduce takes function and sequence
print(sum)


# In[40]:


#lets do the above code with lambda
from functools import reduce

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n:n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))  #map takes a function and an iterable. so we are using lambda function and evens as iterable

sum = reduce(lambda a,b:a+b,doubles)       #reduce belongs to functools, reduce takes function and sequence
print(sum)  # at one point it will take 2 values while adding, which is reduced here


# In[ ]:




