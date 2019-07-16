#!/usr/bin/env python
#coding=utf-8

import requests
import sys
import os
import json

reload(sys)
sys.setdefaultencoding('utf-8') 

#from GetConfigDictClass import *

def as_num(x):
    y = '{:.5f}'.format(x)
    return(y)

def main():

    http_url = "http://httpbin.org/get"
    #http_params = {'wd': 'a'}
    response = requests.get(http_url)
    #response = requests.get(http_url,params=http_params)
    #print response.url
    print response.json()

if __name__ == "__main__":
    main()
