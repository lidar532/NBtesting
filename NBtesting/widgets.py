# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/20_widgets.ipynb.

# %% auto 0
__all__ = ['FolderSelector']

# %% ../nbs/20_widgets.ipynb 3
import panel as pn
import sys

# %% ../nbs/20_widgets.ipynb 9
def FolderSelector( parent,              # Parent widget
                   initial_dir='/',      # Dir to start in.
                   CallBack_func = None  # Function to call with selected folder.
                  ) ->object:            # The folder selector object
    def button_handler(event):
      floatpanel.status = 'closed'
      
      if event.obj.name   == 'Ok':
        parent.Selected_Folder = file_w._directory.value  
      elif event.obj.name == 'Cancel':
        parent.Selected_Folder = None
        
      if CallBack_func != None:
        CallBack_func( [parent.Selected_Folder, event]  )

    file_w          = pn.widgets.FileSelector(initial_dir,     root_directory ='/', refresh_period=500)
    FolderSel_b    = pn.widgets.Button(name='Ok',     button_type='primary')
    folder_cancel_b = pn.widgets.Button(name='Cancel', button_type='primary')
    folder_w        = pn.WidgetBox(file_w, pn.Row(FolderSel_b, folder_cancel_b) )
    floatpanel      = pn.layout.FloatPanel(folder_w, name='Basic FloatPanel', margin=20, contained=False, position='center')
    floatpanel.Selected_Folder = None
    FolderSel_b.on_click(    button_handler )
    folder_cancel_b.on_click( button_handler )
    parent.append( floatpanel )
    return floatpanel
