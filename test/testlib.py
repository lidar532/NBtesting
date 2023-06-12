#!/usr/bin/env python
# coding: utf-8

# ## Imports

# In[ ]:


import  panel as pn
pn.extension()
import test.Folder_Selector


# ## Globals

# In[ ]:


Debug = False


# In[ ]:


if Debug:
  print('Debugging testlib.ipynb')


# ## Funtions

# In[ ]:


def test_a():
  print('This is test_a.')


# In[ ]:


def test_b():
  print('this is test_b.')


# In[ ]:


def test_widget(parent=None, CallBack_func=None ):
  
  def local_ok_callback( value ):
    txt_w.value = value[0]
    if CallBack_func:
      CallBack_func( value[0] )
    
  def event_h( event ):
    txt_w.value = event.obj.name
    c_w.value   = txt_w.value
    if txt_w.value == 'File':
      test.Folder_Selector.Folder_Selector( c_w, CallBack_func = local_ok_callback )
         
  File_b = pn.widgets.Button(name="File")
  a_b    = pn.widgets.Button(name="Run")
  b_b    = pn.widgets.Button(name="Stop")
  c_b    = pn.widgets.Button(name="No Op")
  date_w = pn.widgets.DatePicker(name='Date')
  txt_w  = pn.widgets.StaticText(name='Debug:', value='at start txt.')
  for i in [ File_b, a_b, b_b, c_b]:
    i.on_click( event_h )
  r_w = pn.Row("Master Branch", File_b, a_b, b_b, c_b)
  c_w = pn.Column( date_w, 
                   r_w, 
                   txt_w )
  return c_w


# In[ ]:


if Debug:
  def my_cb( value ):
    print('my_cb:', value )

  r_w = pn.Row("A row")
  w  = test_widget( CallBack_func = my_cb )
  
  w.servable()
  display(w)


# In[ ]:


if Debug:
  print(w.Selected_Folder)

