
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


#Importing All English Words i.e. 466544


# In[15]:


data=open("words.txt","r+")
str=data.readlines()
data.close()


# In[16]:


#Making a list of all the Words


# In[17]:


li=[0]*466544
m=0
for i in str:
        li[m]=i[0:len(i)-1]
        if li[m][-1]in [ ',' , '\'' ,'!' ,'.' ,'"' ,'[' ,']' , '{' , '}','\n','~','`','/','-']:
            j=li[m]
            li[m]=j[0:(len(j)-1)]
        m=m+1
li.append("Hi")
li=sorted(li)


# In[18]:


#The data that has to be checked also needs formating 


# In[19]:


data2=open("raw.txt","r+")
temp=data2.readlines()
string=""
for i in temp:
    string=string+i
data2.close()
string=string.split()
for i in string:
    if i[-1]in [ ',' , '\'' ,'!' ,'.' ,'"' ,'[' ,']' , '{' , '}','\n','~','`','/','-']:
            j=i
            i=j[0:(len(j)-1)]


# In[20]:


t=[]
m=0
for j in string:
    if not(j.lower() in li):
        t.append(m)
    m += 1


# In[21]:


temp=""
for i in t:
    temp=temp+'-'+string[i]
print (" the words misspelled are: "+temp+".")

