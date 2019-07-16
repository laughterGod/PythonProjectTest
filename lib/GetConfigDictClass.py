#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ConfigParser
import string
import os
import sys

home_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir)
#sys.path.append(home_dir + "/lib/")
conf_dir = home_dir + '/conf/'
#print conf_dir
sys.path.append(conf_dir)

class GetConfigDictClass(ConfigParser.ConfigParser):
    def __init__(self, filename):
        """
        __init__:初始化该类

        """
        ConfigParser.ConfigParser.__init__(self)
        self.filename =  os.path.join(conf_dir, filename)
        if os.path.isfile(self.filename):
            ConfigParser.ConfigParser.read(self, self.filename)
        else:
            self.filename =  os.path.join(conf_dir, "main.cfg")
            ConfigParser.ConfigParser.read(self, self.filename)


if __name__ == '__main__':
    cf = GetConfigDictClass("test.cfg")
    print cf.sections()
    res = cf.get('Section1', 'foo')
    print res
