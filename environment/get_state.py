# -*- coding:utf8 -*-
 
import os
import sys
 
TEST_CONF="""messagescan=no
hd=default,vdbench=/root,user=root,shell=ssh
hd=hd1,system=ceph-mon1
fsd=fsd1,anchor=/mnt/cephfs,depth=2,width=10,files=100,size=25k
fwd=format,threads=50,xfersize=4k
fwd=fwd1,fsd=fsd1,host=hd1,operation=read,fileio=random,fileselect=random,xfersize=4k,threads=50
rd=rd1,fwd=fwd*,fwdrate=max,elapsed=3,interval=1,format=yes
"""
def gen_test_file(file_name): 
    with open(file_name, 'w') as fw:
        fw.write(TEST_CONF)
        fw.close()
    return
 
def run_vdbench():
    fileName = 'test'
    gen_test_file('./{}'.format(fileName))
 
    cmd='./vdbench -f {}'.format(fileName) + ' -o ./result/'
    os.system(cmd)



    
if __name__ == '__main__':
    run_vdbench()
    sys.exit(0)
