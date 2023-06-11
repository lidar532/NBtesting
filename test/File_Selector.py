#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import panel as pn
pn.extension('floatpanel') 


# ###    def File_Selector( parent, initial_dir='/', CallBack_func = None ):

# In[ ]:


def File_Selector( parent, initial_dir='/', CallBack_func = None ):
  #selected_path_name = None
  
  def button_handler(event):
    floatpanel.status = 'closed'
    
    if event.obj.name   == 'Ok':
      parent.CORS_folder = file_w._directory.value       
    elif event.obj.name == 'Cancel':
      parent.CORS_folder = None
      
    if CallBack_func != None:
      CallBack_func( [parent.CORS_folder, event]  )

  file_w          = pn.widgets.FileSelector(initial_dir,     root_directory ='/', refresh_period=500)
  folder_sel_b    = pn.widgets.Button(name='Ok',     button_type='primary')
  folder_cancel_b = pn.widgets.Button(name='Cancel', button_type='primary')
  folder_w        = pn.WidgetBox(file_w, pn.Row(folder_sel_b, folder_cancel_b) )
  floatpanel      = pn.layout.FloatPanel(folder_w, name='Basic FloatPanel', margin=20, contained=False, position='center')
  folder_sel_b.on_click(    button_handler )
  folder_cancel_b.on_click( button_handler )
  parent.append( floatpanel )
  return floatpanel


# ### Test & Debug: File_Selector( parent, initial_dir='/', CallBack_func = None ):

# In[ ]:


Testing = False
if Testing:
  import panel as pn
  pn.extension('floatpanel') 
  
  # Optional Function to be called once 'Ok' or 'Cancel' buttons are pressed.
  def My_callBack( v ):
    #print(f'My_callBack( v={v}')
    debug_w.value = main_w.CORS_folder

  def Button_commands( event ):
    w = File_Selector( main_w, CallBack_func = My_callBack )
    
  b_w = pn.widgets.Button(name='Select File')
  debug_w = pn.widgets.StaticText(name='Debug:', value='nothing yet.')
  main_w = pn.Row( "Main", b_w, debug_w )
  b_w.on_click( Button_commands )
  main_w.servable()
  main_w


# In[ ]:


if Testing:
  print(main_w.CORS_folder)

