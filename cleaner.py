
import os
import shutil
import time

delFolCon=0#delted folders
delFilCon=0#deleted files

path=input("Input Path Here: ")

days=30#amount of time

sec=time.time()-days*24*60*60#seconds

def GFA(path):#GFA = get file age
    ctime=os.stat(path).st_ctime
    return ctime #output of user defined function

def remFolder(path):#remove folder
    if not shutil.rmtree(path):
        print(f"{path} is removed succsefully")

    else:
        print(f"{path} could not be removed")

def remFile(path):#remove file
    if not os.remove(path):
        print(f"{path} is removed succsefully")

    else:
        print(f"{path} could not be removed")

if os.path.exists(path):
    for rootFolders,folders,files in os.walk(path):
        if sec>=GFA(rootFolders):
            remFolder(rootFolders)
            delFolCon+=1
            break
        else: 
            for folder in folders:
                folderPath=os.path.join(rootFolders,folder)
                if sec>=GFA(folderPath):
                    remFolder(folderPath)
                    delFolCon+=1
                    break
            for file in files:
                filePath=os.path.join(rootFolders,file)
                if sec>=GFA(filePath):
                    remFile(filePath)
                    delFilCon+=1
    else:
        if sec>=GFA(path):
            remFile(path)
            delFilCon+=1
else:
    print(f"{path} is not here sorry")
    delFilCon+=1

print(f"total folders removed: {delFolCon}")
print(f"total files removed: {delFilCon}")