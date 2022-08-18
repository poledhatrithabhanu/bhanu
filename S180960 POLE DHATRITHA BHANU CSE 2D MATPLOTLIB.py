#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


# In[6]:


fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,.2,.2])


# In[7]:


#now plot (x,y)on both axes.and cal  your figure ogject to show it
ax1.plot(x,y,color='black')
ax2.plot(x,y,color='red')
fig


# In[8]:


#Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,.4,.4])

ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.plot(x,z)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.plot(x,y)
ax2.set_xlim(left=20,right=22)
ax2.set_ylim(bottom=30,top=50)


# In[9]:


# Use plt.subplots(nrows=1, ncols=2) to create the plot below
fig,axes=plt.subplots(1,2)
axes[0].plot(x,y,lw=3,ls='--')
axes[1].plot(x,z,color='r',lw=4)


# In[12]:


#See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code
fig,axes=plt.subplots(1,2,figsize=(12,2))
axes[0].plot(x,y,lw=3,ls='--')
axes[1].plot(x,z,color='r',lw=4)


# In[13]:


#Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,.4,.4])

ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.plot(x,z)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.plot(x,y)
ax2.set_xlim(left=20,right=22)
ax2.set_ylim(bottom=30,top=50)


# In[14]:


fig,axes=plt.subplots(nrows=1,ncols=2)


# In[ ]:




