import os

def create_Folder(DirPath,FolderName):
    if os.path.exists(DirPath):
        os.chdir(DirPath)
        os.mkdir(FolderName)
    else:
        print(DirPath, "does not exsist!!!!!!!")
        
        
        
create_Folder("E:\\","IloveYou")