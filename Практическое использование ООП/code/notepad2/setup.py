import sys
from cx_Freeze import setup, Executable
import os


print(os.getcwd())
path = os.getcwd()
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    opts = {"includes": ["re", "atexit"],'include_files': [
                                'blue-folder-open-document.png',
                                'arrow-curve-180-left.png',
                              'images/arrow-curve.png',
                              'images/blue-folder-open-document.png',
                              'images/blue-folder-open-document.png',
                              'images/clipboard-paste-document-text.png',
                              'images/disk--pencil.png',
                              'images/disk.png',
                              'images/document-copy.png',
                              'images/scissors.png',
                              'images/selection-input.png']}

setup(name="Notepad2020",
      version='0.1',
      description = "Notepad",
      options={
          'bdist_mac': {
              'bundle_name': "XXX",
          }

      },
      author = "Paul",

      executables = [Executable('notepad.py', base=base)])


