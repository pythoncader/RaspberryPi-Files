#useful code to read output of command in terminal
import os
a  = os.popen('ls').readlines()
print(a)
os.system(f"ls {a[0]}") #prints out the files and directories that are in the first directory