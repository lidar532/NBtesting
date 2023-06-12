#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import panel as pn
pn.extension('floatpanel') 


# ## Globals

# In[ ]:


Debug = False


# In[ ]:


if Debug:
  print('Debugging Folder_Selector.ipynb')


# ###    def Folder_Selector( parent, initial_dir='/', CallBack_func = None ):

# In[ ]:


def Folder_Selector( parent, initial_dir='/', CallBack_func = None ):  
  def button_handler(event):
    floatpanel.status = 'closed'
    
    if event.obj.name   == 'Ok':
      parent.Selected_Folder = file_w._directory.value  
    elif event.obj.name == 'Cancel':
      parent.Selected_Folder = None
      
    if CallBack_func != None:
      CallBack_func( [parent.Selected_Folder, event]  )

  file_w          = pn.widgets.FileSelector(initial_dir,     root_directory ='/', refresh_period=500)
  folder_sel_b    = pn.widgets.Button(name='Ok',     button_type='primary')
  folder_cancel_b = pn.widgets.Button(name='Cancel', button_type='primary')
  folder_w        = pn.WidgetBox(file_w, pn.Row(folder_sel_b, folder_cancel_b) )
  floatpanel      = pn.layout.FloatPanel(folder_w, name='Basic FloatPanel', margin=20, contained=False, position='center')
  floatpanel.Selected_Folder = None
  folder_sel_b.on_click(    button_handler )
  folder_cancel_b.on_click( button_handler )
  parent.append( floatpanel )
  return floatpanel


# ### Test & Debug: File_Selector( parent, initial_dir='/', CallBack_func = None ):

# In[ ]:


if Debug:
  import panel as pn
  pn.extension('floatpanel') 
  
  # Optional Function to be called once 'Ok' or 'Cancel' buttons are pressed.
  def My_callBack( v ):
    debug_w.value = main_w.Selected_Folder

  def Button_commands( event ):
    w = Folder_Selector( main_w, CallBack_func = My_callBack )
    
  b_w = pn.widgets.Button(name='Select Folder')
  debug_w = pn.widgets.StaticText(name='Selected Folder:', value='nothing selected yet.')
  main_w = pn.Row( "Main", b_w, debug_w )
  main_w.Selected_Folder = None
  b_w.on_click( Button_commands )
  display(main_w.servable())
#main_w


# In[ ]:


if Debug:
  print(main_w.Selected_Folder)

