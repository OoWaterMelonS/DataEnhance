import os
import pathlib
import random
import shutil


def moveFileToTest(path):
    for root, dirs, files in os.walk(path):
        if len(files) == 17:
            num = list(range(0, 17, 1))
            b = random.sample(num, 5)
            files_list = list(files)
            for i in range(5):
                try:
                    path = root + '/' + files_list[b[i]]
                    if pathlib.Path(path).exists():
                        full_path = path
                        paths = path.split("/")
                        des_path = testDir + paths[4] + '/'
                        if not os.path.exists(des_path):
                            os.mkdir(testDir + paths[4] + '/')
                        shutil.move(full_path, des_path)
                except IndexError:
                    print("list index out of range")
            return
        elif len(files) == 12:
            print("data had been handled already")
        else:
            print("too many data were deleted!!!")


def func(path):
    if pathlib.Path(testDir).exists():
        del_file(testDir)

    a = []
    for root, dirs, files in os.walk(path):
        a.append(root)

    for i in range(len(a)):
        moveFileToTest(a[i])


def del_file(path):
    for i in os.listdir(path):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)


testDir = 'E:/taidi/DataEnhance/test/'
# func(testDir)
trainDir = 'E:/taidi/DataEnhance/train/'
func(trainDir)

#  对单个文件夹下面的图片进行删除
#  遍历文件夹下面的文件夹，对每一个文件夹执行随机删除文件操作
