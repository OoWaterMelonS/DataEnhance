# coding:utf-8
import os
from PIL import Image


# bmp 转换为jpg
def bmpToJpg(file_path,out_path):
    i = 0
    for fileName in os.listdir(file_path):
        i += 1
        print(fileName)
        newFileName = fileName[0:fileName.find(".")] + ".jpg"
        print(newFileName)
        im = Image.open(file_path + "\\" + fileName)
        im.save(out_path + "\\" + newFileName)
    print(i+"bmp file change success")

# 删除原来的位图
def deleteImages(file_path, imageFormat):
    command = "del " + file_path + "\\*." + imageFormat
    os.system(command)


def main():
    file_path = 'origin_data/classify/'
    out_path = 'bmp2jpg/'
    bmpToJpg(file_path,out_path)
    # deleteImages(file_path, "bmp")


if __name__ == '__main__':
    main()
