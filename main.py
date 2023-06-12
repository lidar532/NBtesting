#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import panel as pn
import sys


# In[ ]:


Debug = False


# In[ ]:


if Debug:
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


if Debug:
  print(my_w.Selected_Folder)

