#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2021 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import string
import itertools
from lib.data.data import pystrs,  pyoptions
from lib.fun.fun import finishprinter, countchecker, range_compatible, finalsavepath, fun_name


# get the dictionary list
def getchars(type):
    flag = str(type)
    chars = []
    if type in pystrs.base_dic_type:
        if flag == pystrs.base_dic_type[0]:
            chars = string.digits
        elif flag == pystrs.base_dic_type[1]:
            chars = string.ascii_lowercase
        elif flag == pystrs.base_dic_type[2]:
            chars = string.ascii_uppercase
        elif flag == pystrs.base_dic_type[3]:
            chars = string.printable[:36]
        elif flag == pystrs.base_dic_type[4]:
            chars = string.digits + string.ascii_uppercase
        elif flag == pystrs.base_dic_type[5]:
            chars = string.ascii_letters
        elif flag == pystrs.base_dic_type[6]:
            chars = string.printable[:62]
        return chars


def get_base_dic(objflag):
    storepath = finalsavepath(fun_name())

    objflag = getchars(objflag)
    countchecker(len(objflag), pyoptions.minlen, pyoptions.maxlen)

    # global variable transfer local variable to improved speed
    buffer = []
    buffer_size = pyoptions.buffer_size
    head = pyoptions.head
    tail = pyoptions.tail
    crlf = pyoptions.CRLF
    encode_name = pyoptions.encode
    encode_fun = pyoptions.operator.get(encode_name)

    with open(storepath, "a") as f:
        for i in range_compatible(pyoptions.minlen, pyoptions.maxlen+1):
            for item in itertools.product(objflag, repeat=i):
                if encode_name == "none":
                    buffer.append(head + "".join(item) + tail)
                else:
                    buffer.append(encode_fun(head + "".join(item) + tail))
                if len(buffer) == buffer_size:
                    f.write(crlf.join(buffer) + crlf)
                    buffer = []
        f.write(crlf.join(buffer))
    finishprinter(storepath)
