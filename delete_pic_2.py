import os


# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            num = f.split("-")[1].split('.')[0]
            if num == '2':
                str = os.path.join(root,f)
                os.remove(str)

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))
path = 'E:/taidi/DataEnhance/bmp2jpg/'

walkFile(path)

