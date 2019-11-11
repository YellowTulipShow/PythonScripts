# coding: UTF-8

import re

def trimStart(vstr):
    vstr = str(vstr)
    vstr = re.sub(r"^\s+", "", vstr)
    return vstr
def trimEnd(vstr):
    vstr = str(vstr)
    vstr = re.sub(r"\s+$", "", vstr)
    return vstr
def trim(vstr):
    vstr = trimStart(vstr)
    vstr = trimEnd(vstr)
    return vstr

if __name__ == '__main__':
    test_str_trim = '  22 55 00 33  '
    print('trimStart: "{str}"'.format(str=trimStart(test_str_trim)))
    print('trimEnd: "{str}"'.format(str=trimEnd(test_str_trim)))
    print('trim: "{str}"'.format(str=trim(test_str_trim)))
