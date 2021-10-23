#!/usr/bin/env python
# coding: utf-8

# In[2]:


java = int(input("Enter Marks of Java : "))
cpp = int(input("Enter Marks of C++ : "))
database= int(input("Enter Marks of Database : "))
total =300
obt_marks = java+cpp+database

percentage = (obt_marks*100)/total

print("Obtained Marks :{obt_marks} out of 300")

if percentage >=0 and percentage <= 100:
    
    if percentage >=80 and percentage <=100:
        print("Your grade is A+")
    elif percentage >=70 and percentage <80:
        print("Your grade is A")
    elif percentage >=60 and percentage <70:
        print("Your grade is B")
    elif percentage >=40 and percentage <60:
        print("Your grade is C")
    elif percentage >=1 and percentage <40:
        print("Your Fail")    


# In[ ]:




