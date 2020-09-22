#!/usr/bin/env python
# coding: utf-8

# In[1]:


Mxlim = int(input("INPUT MAX LIMIT TO FIND (<= 100000 HIGHLY RECOMMENDED) :"))
fib = []
fib.append(1)
fib.append(1)


# In[2]:


for i in range(2,Mxlim):
    fib.append(fib[i-1]+fib[i-2])


# In[3]:


FirstDigit = []
for i in range(1,11): FirstDigit.append(0)
for i in range(1,Mxlim):
    FirstDigit[int(str(fib[i])[0])] += 1


# In[4]:


FirstDigit = [i/(Mxlim-1) for i in FirstDigit]
for i, val in enumerate(FirstDigit):
    if i==0 : continue
    print("Probability for Digit "+str(i)+" : ",end="")
    print("%.16f"%val)


# In[5]:


def logFunc(x):
    return np.log10((x+1)/x)


# In[6]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10,0.1)
plt.plot(x,logFunc(x),color='red')
plt.plot(FirstDigit,color='blue')
plt.xlim(1.0,10.0)
plt.show()


# In[82]:


Deltalist = []
for i in range(1,10):
    Deltalist.append(logFunc(i)-FirstDigit[i])
for i,val in enumerate(Deltalist):
    print("Error in Digit " + str(i+1) + " : ",end="")
    print("%.16f"%val)


# In[ ]:




