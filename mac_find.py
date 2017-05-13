#coding: utf-8
import re
from subprocess import PIPE,Popen

def mac_find(eth):
    ex = Popen('ifconfig '+ eth, stdin=PIPE, stdout=PIPE, shell=True)
    data = ex.stdout.read()
    data = ''.join(data)
    #print data
    wann = re.findall(r'\w\w\:\w\w\:\w\w\:\w\w\:\w\w\:\w\w', data)
    print ''.join(wann)

mac_find(raw_input('enter network interface:\n'))