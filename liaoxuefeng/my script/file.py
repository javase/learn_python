import os
import os.path

# this folder is custom
rootdir = "E:\技术\学习研究\Python"
for parent, dirnames, filenames in os.walk(rootdir):
    # case 1:
    for dirname in dirnames:
        print("parent folder is:" + parent)
        print("dirname is:" + dirname)
        # case 2
    for filename in filenames:
        print("parent folder is:" + parent)
        print("filename with full path:" + os.path.join(parent, filename))


def createPathIfNotExist(path):
    ifExist = os.path.isdir(path)
    # 目录不存在
    if not ifExist:
        os.makedirs(path)
        if os.path.isdir(path):
            print('目录[%s]创建成功' % path)


createPathIfNotExist('/usr/local/dir_samba/files/excel/1')
