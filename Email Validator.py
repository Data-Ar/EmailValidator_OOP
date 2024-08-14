#!/usr/bin/env python
# coding: utf-8

# In[1]:


def email_validator(email):
    if email.count('@') != 0 and email.count('.') != 0:
        return True
    else:
        return False


# In[3]:


email = 'sulaiman.afolabi@gmail.com'


# In[5]:


email_validator(email)


# In[6]:


email = 'afolabi.sulaiman.com'
email_validator(email)


# In[ ]:


# best form of testing my function


# In[7]:


email_validator('afolabisulaiman924@gmail.com')


# In[ ]:


# another more generic function


# In[20]:


def email_validator2(email):
    if email.count('@') != 0 and email.count('.') != 0:
        return True
    else:
        return False


# In[21]:


def test_email_validator(email):
    assert email_validator2('juno@gmail.com') == True
    assert email_validator2('juno@gmail@.com') == False


# In[ ]:




