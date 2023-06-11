#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import  panel as pn
pn.extension()
import test.File_Selector


# In[ ]:


def test_a():
  print('This is test_a.')


# In[ ]:


def test_b():
  print('this is test_b.')


# In[ ]:


def test_widget( callback=None):
  def event_h( event ):
    txt_w.value = event.obj.name
    c_w.value = txt_w.value
    if txt_w.value == 'File':
      test.File_Selector.File_Selector( c_w )
    if callback:
      callback(c_w.value)
  File_b = pn.widgets.Button(name="File")
  a_b = pn.widgets.Button(name="Run")
  b_b = pn.widgets.Button(name="Stop")
  c_b = pn.widgets.Button(name="No Op")
  date_w = pn.widgets.DatePicker(name='Date')
  txt_w = pn.widgets.StaticText(name='Debug:', value='at start txt.')
  for i in [ File_b, a_b, b_b, c_b]:
    i.on_click( event_h )
  r_w = pn.Row(File_b, a_b, b_b, c_b)
  c_w = pn.Column(date_w, r_w, txt_w )
  return c_w


# In[ ]:


if False:
  test_a()
  test_b()
  w = test_widget()
  w.servable()
  display(w)


# In[ ]:




