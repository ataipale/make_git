#!/usr/local/bin/Python -tt

import sys
import os
import shutil
import pudb


def namePath(n):
    newPath = os.getcwd()+"/.myvcs/%d" % (n)
    return newPath

def giveVersion():
    # pudb.set_trace()
    snapShotID = 1
    while (os.path.exists(namePath(snapShotID))):
        snapShotID = snapShotID + 1
        print snapShotID
    return snapShotID

def ignore(curDir, contentList):
    return ['.myvcs']


def copyFiles(directory, topLevel = None):
    if topLevel == None:
        topLevel = directory
    print directory
    q = raw_input("type something")
    fileList = os.listdir(directory)
    for file in fileList:
        filePath = directory + "/" + file
        shortFile = os.path.relpath(filePath, topLevel)
        newPath = os.getcwd() + "/" + shortFile
        if os.path.isdir(filePath):
            if os.path.exists(newPath):
                shutil.rmtree(newPath)
            os.mkdir(newPath)
            copyFiles(filePath, topLevel)
        else:
            shutil.copy(filePath, newPath)

if __name__ == '__main__':

    command = sys.argv[1]

    if (command == "copy"):
        shutil.copytree(os.getcwd(), namePath(giveVersion()), ignore = ignore)

    if(command == "checkout"):
        dirOriginal = int(sys.argv[2])
        print "checked out"
        copyFiles(namePath(dirOriginal))





# Below is my attempt at writing the tree copying method recursively.
# Question: Why isnt this working? how would i name the new file 
# being copied to if i wanted to do that?
# 
# QUESTION: now only using file in same folder as test program
# How do i get it to be able to sue any program path
# or command to give full file path from directory name input?

# def copyFiles(directory):
#     fileList = os.listdir(directory)
#     for file in fileList:
#         if os.path.isdir(file):
#             copyFiles(file)
#         else:
#             shutil.copy(file, newPath)

# copyFiles(dirOriginal)



    

        
