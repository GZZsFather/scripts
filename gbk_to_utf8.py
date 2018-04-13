#! /usr/local/bin/python3

### python3 path use your own one

import sys
import os

if __name__ == "__main__":
    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print("No such file!")

    else:
        obj = open(filepath,'r+',encoding='gbk')
        lines = obj.readlines()
        obj.close()

        des = open(filepath,'w+')
        for line in lines:
            des.writelines(line)
            des.write('/n')
