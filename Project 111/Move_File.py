import os
print(dir(os))
import shutil
file=os.listdir()
print(file)
b=os.path.exists('C:/Users/Dell/Project 111')
from_dir='C:\Users\Dell\OneDrive\Desktop\Document_files'
to_dir='C:\Users\Dell\OneDrive\Desktop\Project 111'
copied=shutil.move(from_dir,to_dir)
