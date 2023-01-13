# 随机取文件
# # -*- coding:utf-8 -*-
# """
# 作者：sunli
# 日期：2022年03月14日14:06
# """

import os
import random
import shutil


def moveFile(fileDir, trainDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    # rate1 = 0.8  # 自定义抽取csv文件的比例，比方说100张抽80个，那就是0.8
    rate1 = 0.1
    picknumber1 = int(filenumber*rate1)  # 按照rate比例从文件夹中取一定数量的文件
    sample1 = random.sample(pathDir, picknumber1)  # 随机选取picknumber数量的样本
    for name in sample1:
        # for Windows
        # shutil.move(fileDir + '/' + name, trainDir + "\\" + name)
        # for linux
        shutil.copy(fileDir + '/' + name, trainDir + "/" + name)


if __name__ == '__main__':
    fileDir = 'D:/GitHubSYNC/CommonlyUsedScript/data'
    testDir = 'D:/GitHubSYNC/CommonlyUsedScript/testdata'
    moveFile(fileDir, testDir)
