import os
os.chdir('./txt')
a = 0
#创建文件
while (a<5):
    f = open('python'+str(a)+'.txt','w')
    f.write('hello world')
    f.close()
    a = a+1
#修改文件名称
file_lists = os.listdir()
for file_name in file_lists:
    os.rename(file_name,'志祥制造'+file_name)
