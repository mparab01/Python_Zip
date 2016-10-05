
# coding: utf-8

# Built-In function in Python : Zip

# In[7]:

l = [1,2,3,4,6,7]
p = [9,8,7,6,5]

for pair in zip(l,p):
    print max(pair)


# In[6]:

x = zip(l,p)
print x


# In[3]:

t1 = (1,2,3,4)
t2 = (9,8,7,6,5)

x2 = zip(t1,t2)
print x2


# In[4]:

d1 = {1:'One', 2:'Two'}
d2 = {3:'Four', 4:'Five'}

x3 = zip(d1,d2)
print x3


# In[8]:

zip(d1,d2.itervalues())


# In[ ]:



