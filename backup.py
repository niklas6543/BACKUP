import os, datetime, shutil

BACKUP_DIR = ""
CURRENT_DIR = "./"

def copyDIR(srcDir, dstDir):
    for file in os.listdir(srcDir):
        file_path = os.path.join(srcDir, file)
        unixTime = os.path.getctime(file_path);
        realTime = datetime.datetime.fromtimestamp(
                         int(os.path.getctime(file_path))
                    ).strftime("%Y-%m-%d %H:%M:%S")
    
    #if os.path.isfile(file_path):
    #    shutil.copy(file_path, dstdir)
        print(("%s # %s") % (file, realTime))
copyDIR(CURRENT_DIR, BACKUP_DIR)	

