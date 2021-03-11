import csv
import os
import shutil
from del_directory import delete_file

def del_fun(path):
    if os.path.exists(path):
        delete_file(path)
    os.mkdir(path)

train_path = 'E:/taidi/DataEnhance/train/'
test_path = 'E:/taidi/DataEnhance/test/'
dataset_train = 'E:/taidi/DataEnhance/dataset/train/'
dataset_test = 'E:/taidi/DataEnhance/dataset/test/'
origin_path = train_path
goal_path = dataset_train
# origin_path = test_path
# goal_path = dataset_test


# del_fun(train_path)
with open('rock_label_1.csv', 'r') as f:



    reader = csv.reader(f)
    # Dark gray mudstone
    dgm = []
    # Light gray fine sandstone
    lgfs = []
    # Grey fine sandstone
    gfs = []
    # Dark gray silty mudstone
    dgsm = []
    # Grey argillaceous siltstone
    gas = []
    # Gray-black mudstone
    g_bm = []
    # Black coal
    bc = []
    for row in reader:
        if row[2] == 'Dark gray mudstone':
            dgm.append(row[0])
        elif row[2] == 'Light gray fine sandstone':
            lgfs.append(row[0])
        elif row[2] == 'Grey fine sandstone':
            gfs.append(row[0])
        elif row[2] == 'Dark gray silty mudstone':
            dgsm.append(row[0])
        elif row[2] == 'Grey argillaceous siltstone':
            gas.append(row[0])
        elif row[2] == 'Gray-black mudstone':
            g_bm.append(row[0])
        else:
            bc.append(row[0])


    del_fun(goal_path+'Dark gray mudstone')
    del_fun(goal_path+'Light gray fine sandstone')
    del_fun(goal_path+'Grey fine sandstone')
    del_fun(goal_path+'Dark gray silty mudstone')
    del_fun(goal_path+'Grey argillaceous siltstone')
    del_fun(goal_path+'Gray-black mudstone')
    del_fun(goal_path+'Black coal')


    for root, dirs, files in os.walk(origin_path):
        for i in range(len(dirs)):
            child_dir = dirs[i]
            temp = child_dir.split("-")[0]
            for root_child, dirs_child, files_child in os.walk(origin_path + child_dir):
                if temp in dgm:
                    list = []
                    for i in range(len(files_child)):
                        list.append(root_child + '/' + files_child[i])
                    for k in range(len(list)):
                        des_path = goal_path + 'Dark gray mudstone'
                        shutil.move(list[k], des_path)
                elif temp in lgfs:
                    list = []
                    for i in range(len(files_child)):
                        list.append(root_child + '/' + files_child[i])
                    for k in range(len(list)):
                        des_path = goal_path + 'Light gray fine sandstone'
                        shutil.move(list[k], des_path)
                elif temp in dgsm:
                    list = []
                    for i in range(len(files_child)):
                        list.append(root_child + '/' + files_child[i])
                    for k in range(len(list)):
                        des_path = goal_path + 'Dark gray silty mudstone'
                        shutil.move(list[k], des_path)
                elif temp in gfs:
                    list = []
                    for i in range(len(files_child)):
                        list.append(root_child + '/' + files_child[i])
                    for k in range(len(list)):
                        des_path = goal_path + 'Grey fine sandstone'
                        shutil.move(list[k], des_path)
                elif temp in gas:
                    list = []
                    for i in range(len(files_child)):
                        list.append(root_child + '/' + files_child[i])
                    for k in range(len(list)):
                        des_path = goal_path + 'Grey argillaceous siltstone'
                        shutil.move(list[k], des_path)
                elif temp in g_bm:
                    list = []
                    for i in range(len(files_child)):
                        list.append(root_child + '/' + files_child[i])
                    for k in range(len(list)):
                        des_path = goal_path + 'Gray-black mudstone'
                        shutil.move(list[k], des_path)
                else:
                    list = []
                    for i in range(len(files_child)):
                        list.append(root_child + '/' + files_child[i])
                    for k in range(len(list)):
                        des_path = goal_path + 'Black coal'
                        shutil.move(list[k], des_path)
