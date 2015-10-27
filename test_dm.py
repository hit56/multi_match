#! /bin/env python
# encoding=utf-8
# gusimiu@baidu.com
# 

import sys
import dmdict

if __name__=='__main__':
    d = dmdict.DMSearchDict()
    if len(sys.argv)>=2 and sys.argv[1] == '-l':
        sys.stderr.write('Run in load mode:\n')
        d.load('./test.dm')
        print 'load over.'

    else:
        sys.stderr.write('Run in save mode:\n')
        d.add('abcdef', 1)
        d.add('ab', 3)
        d.add('cde')

        d.save('./test.dm')

    print 'I_FIND(expect some outputs):'
    for ans in d.find('this is a abcdef and abc and abcde text'):
        print ans
