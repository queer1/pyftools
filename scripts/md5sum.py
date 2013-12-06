#!/usr/local/bin/python3

import os
from hashlib import md5

def checksum(filename):
    chunk_size = 1048576 #1024*1024 (1MiB)
    f = open(filename,"rb");
    data = f.read(chunk_size)
    md5_checksum = md5()
    while data:
        md5_checksum.update(data)
        data = f.read(chunk_size)
    return md5_checksum.hexdigest()
    
    
for (path,listOfDir,listOfFile) in os.walk('/home/khyale/teste'):
    for f_k in listOfFile:
        filename = os.path.join(path,f_k)
        print(checksum(filename) + '  ./' + os.path.relpath(filename,'/home/khyale/teste'))
