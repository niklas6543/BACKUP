#!/usr/bin/python3

import os, datetime, shutil

dstDir = "../back"
srcDir = "../"

def copyFiles(files):
    #for file in os.listdir(srcDir):
    for file in files: 
       file_path = os.path.join(srcDir, file)
        
#       if os.path.isfile(file_path):
       shutil.copytree(file_path, dstDir)
        
       print(("%s") % (file_path))

def getChanges():
    files = [] 
    dstFiles = {}
    srcFiles = {}

    for fileSrc in os.listdir(srcDir):
        fileSrcPath = os.path.join(srcDir, fileSrc)

#        if os.path.isdir(fileSrcPath):
#            print(fileSrc)
#            for file in os.listdir(fileSrcPath):
#                print(file)

        uTimeSrc = os.path.getctime(fileSrcPath);
        rTimeSrc = datetime.datetime.fromtimestamp(
                         int(os.path.getctime(fileSrcPath))
                    ).strftime("%Y-%m-%d %H:%M:%S")

        srcFiles[fileSrc] = uTimeSrc
    
    for fileDst in os.listdir(dstDir):
        fileDstPath = os.path.join(dstDir, fileDst)
        uTimeDst = os.path.getctime(fileDstPath);
        rTimeDst = datetime.datetime.fromtimestamp(
                         int(os.path.getctime(fileDstPath))
                    ).strftime("%Y-%m-%d %H:%M:%S")
        dstFiles[fileDst] = uTimeDst

    for (k, v) in srcFiles.items():
        if k in dstFiles.keys():
            if v > dstFiles[k]:
            #print(("%s # %s") % (fileDst, fileSrc))
                files.append(k)
        elif k  != 'BACKUP':
            files.append(k)
            
    

    return files 


copyFiles(getChanges())	

