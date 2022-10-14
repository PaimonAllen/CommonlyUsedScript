# -*- coding: utf-8 -*-
# !/usr/bin/python

import os

# current_directory = os.path.dirname(os.path.abspath('__file__'))

PATH = os.path.abspath(os.path.join(os.getcwd(), "dataset_copy"))

def rename_file(oldname, val):
    oldname = os.path.join(PATH, oldname)
    # newname = oldname 
    print(oldname)
    newname = f'test{val}.jpg'
    # newname = os.path.join(PATH,newname)+'.txt'
    newname = os.path.join(PATH,newname)
    # newname = newname+"1"

    os.rename(oldname, newname)
    # print("oldname -------------> newname ", oldname,newname)
 
if __name__=="__main__":
    fileList = os.listdir(PATH)
    fileList.sort()
    print(fileList)
    i = 15
    for name in fileList:
        print(i)
        rename_file(name, i)
        i += 1


