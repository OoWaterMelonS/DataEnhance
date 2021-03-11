# coding:utf-8
import os
import stat
import shutil


def delete_file(filePath):
    if os.path.exists(filePath):
        for fileList in os.walk(filePath):
            for name in fileList[2]:
                os.chmod(os.path.join(fileList[0], name), stat.S_IWRITE)
                os.remove(os.path.join(fileList[0], name))
                shutil.rmtree(filePath)
                return "delete ok"
        os.removedirs(filePath)
    else:
        return "no filepath"

# path = 'E:/taidi/DataEnhance/data/Black coal'
#
# print(os.path.exists(path))
# delete_file(path)
