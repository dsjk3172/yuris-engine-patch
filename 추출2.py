import re
import os.path

path = os.getcwd()
filelist = os.listdir(f"{path}/원본")

for i in filelist:
    ReadFile = open(f"{path}/원본/{i}", 'r' , encoding='UTF-16LE')
    writefile = open(f"{path}/시스템 문장 추출본/{i}", 'w', encoding='UTF-16LE')
    readline = ReadFile.readlines()

    abc = list()

    r = re.compile('.*ANI.*')
    for i in readline:
        abc = re.findall(r, i)
        contents = "".join(abc) + "\n"
        writefile.write(contents)
    writefile.close()