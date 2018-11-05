
# coding: utf-8

# In[1]:


import os 
os.getcwd()


# In[2]:


file= 'C:\\Users\\andre\Documents\Average high and low tempratures Victorvill.csv'


# In[3]:


import numpy as np
data = np.genfromtxt(file,skip_header=0,delimiter=',')


# In[4]:


data


# In[5]:


y = data[:,2]


# In[6]:


y


# In[7]:


import math 
from matplotlib import pyplot


# In[10]:


pyplot.plot(y,'r',x,'*')
pyplot.xlabel('Months')
pyplot.ylabel('Average High and Low Temprature')
pyplot.title('Annual Temprature')
pyplot.legend('-')


# In[9]:


x = data[:,1]


# In[11]:


file2= 'C:\\Users\\andre\Documents\Victorville CA crime rate.csv'


# In[12]:


data2=np.genfromtxt(file2,skip_header=0,delimiter=',')


# In[13]:


data2


# In[14]:


Y = data2[:,2]
X = data2[:,1]


# In[15]:


pyplot.plot(X,Y,)
pyplot.xlabel('Months')
pyplot.ylabel('Reported Crimes')
pyplot.title('Monthly Crime Rate Victorville')


# In[16]:


## atc edit

pyplot.plot(y,'r',x,'*')
pyplot.plot(X,Y*max(y)/max(Y),)
pyplot.xlabel('Months')
pyplot.ylabel('Average High and Low Temprature')
pyplot.title('Annual Temprature')
pyplot.legend('-')


# In[17]:


pyplot.plot(Y,y,'*')
pyplot.legend('*')
pyplot.xlabel('Crime Rate')
pyplot.ylabel('Temprature')


# In[18]:


import numpy as np 


# In[19]:


file2 = 'C:\\Users\\andre\\Documents\\Top 12 Cities for crime.csv'


# In[20]:


qq = np.genfromtxt(file2,skip_header=1, delimiter=',')


# In[21]:


qq


# In[22]:


w = qq[:,0]
# Population of the cities 
ww= qq[:,2]
# Property crimes per city 


# In[23]:


w


# In[24]:


ww


# In[25]:


def Volume_percrime():
    return (ww/w)*1000
# a function that takes in the number of property crimes divided by the population of the city and multiplies by 1000
# Provides the volume of crimes per 1000 people 


# In[26]:


Volume_Propertycrime= Volume_percrime()


# In[27]:


Volume_Propertycrime


# In[28]:


Volume_Propertycrime.max()


# In[29]:


Volume_Propertycrime.min()


# In[30]:


R = np.sort(Volume_Propertycrime)


# In[41]:


file3 = 'C:\\Users\\andre\\Documents\\Safe cities.csv'


# In[42]:


safe = np.genfromtxt(file3,skip_header= 1, delimiter= ',')


# In[43]:


safe


# In[44]:


a= safe[:,0]
b = safe[:,2]


# In[45]:


def Volume_percrime1():
    return (b/a)*1000


# In[46]:


f = Volume_percrime1()


# In[47]:


f


# In[48]:


L= np.sort(f)


# In[49]:


L


# In[50]:


pyplot.hist(R)
pyplot.hist(L)
pyplot.xlabel('Property Crime per 1000')
pyplot.ylabel('Number of Cities')
pyplot.legend('HL')
# H is for the blue high crime 
# L is for low crime 


# In[51]:


file4 = 'C:\\Users\\andre\\Documents\\San Bernandino Weather .csv'


# In[61]:


SBW = np.genfromtxt(file4,delimiter=',')


# In[62]:


SBWW = SBW[:,0]


# In[63]:


SBWW


# In[67]:


pyplot.plot(y,'red',SBWW,'blue', WW, 'g')
pyplot.xlabel('Months')
pyplot.ylabel('Average High in F')
pyplot.legend('VSI')


# In[57]:


file5 = 'C:\\Users\\andre\\Documents\\Different Weathers.csv'


# In[65]:


WW = np.genfromtxt(file5,skip_header= 1, delimiter= ',')


# In[66]:


WW

