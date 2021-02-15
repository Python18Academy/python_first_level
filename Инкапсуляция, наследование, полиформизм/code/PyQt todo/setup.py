import sys
from cx_Freeze import setup, Executable
import os
opts = {'include_files':['tick.png', 'data.db', 'mainwindow.ui']}


print(os.getcwd())
path = os.getcwd()
base = None
# opts = {"includes":"json", 'include_files': ['tick.png', 'data.db', 'mainwindow.ui']}
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="todo",
      version='0.1',
      description = "todo",
      options={
          'bdist_dmg': opts

      },
      author = "Noone",

      executables = [Executable('todo.py', base=base)])


