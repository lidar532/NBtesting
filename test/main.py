#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import panel as pn
import sys


# In[ ]:


if False:
  for p in sys.path:
    print(p)


# In[ ]:


import test.testlib
#import test.File_Selector


# In[ ]:


pn.extension()

my_w = test.testlib.test_widget()
my_w.servable()


# In[ ]:


my_w.CORS_folder

