#! /usr/bin/python3
import os

#author QiangweiLuo
#frist time: 2018-08-06
#final time: 2018-08-06

print (os.popen("pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip").read())
result = os.popen("pip3 list --outdated")
resultSet = result.read()
data = resultSet.split()
if(len(data) != 0):
    for i in range(0, 8):
        data.pop(0)
    count = 0
    for item in data:
        if count % 4 == 0:
            print(os.popen("pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade " + item).read())
        count += 1