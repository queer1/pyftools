#!/usr/local/bin/python3

import os,sys
from hashlib import md5
from sys import argv

root_dir = argv[1]

def checksum(filename):
    try:
        f = open(filename,"rb")
        chunk_size = 1048576    #1024*1024 (1MiB)
        data = f.read(chunk_size)
        md5_checksum = md5()
        while data:
            md5_checksum.update(data)
            data = f.read(chunk_size)
    except IOError:
        return -1
    else:
        return md5_checksum.hexdigest()

def invalid_root(err):
    print('Error while reading '+root_dir)
    sys.exit()
        
for (path,listOfDir,listOfFile) in os.walk(top=root_dir,onerror=invalid_root):
    for f_k in listOfFile:
        filename = os.path.join(path,f_k)
        hexValue = checksum(filename)
        if hexValue!=-1:
            print(hexValue+'  ./'+os.path.relpath(filename,root_dir))
        else:
            print('Error while reading'+'  ./'+os.path.relpath(filename,root_dir))
                
