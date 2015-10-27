#! /bin/env python
# encoding=utf-8
# gusimiu@baidu.com
# 

import sys
import c_dmsearch

class DMSearchDict:
    def __init__(self):
        self.__dict_handle = c_dmsearch.create()
        if self.__dict_handle == -1:
            sys.stderr.write('Create dict fail! ret=%d\n' % self.__dict_handle)

    def add(self, lemma, prop=None):
        if prop is None:
            return c_dmsearch.add(self.__dict_handle, lemma)
        else:
            return c_dmsearch.add(self.__dict_handle, lemma, prop)

    def save(self, output_filename):
        return c_dmsearch.save(self.__dict_handle, output_filename)

    def load(self, filename):
        return c_dmsearch.load(self.__dict_handle, filename)

    def find(self, s):
        return c_dmsearch.find(self.__dict_handle, s)

if __name__=='__main__':
    pass
