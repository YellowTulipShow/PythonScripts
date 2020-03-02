# coding: UTF-8

import re
import copy

def trimStart(vstr, symbol=r'\s+'):
    vstr = str(vstr)
    vstr = re.sub(r"^" + symbol, "", vstr)
    return vstr

def trimEnd(vstr, symbol=r'\s+'):
    vstr = str(vstr)
    vstr = re.sub(symbol + r"$", "", vstr)
    return vstr

def trim(vstr, symbol=r'\s+'):
    vstr = trimStart(vstr, symbol=symbol)
    vstr = trimEnd(vstr, symbol=symbol)
    return vstr

def copy_dict(dict_old, dict_new):
    r = dict_old
    for key in dict_new:
        v = dict_new[key]
        if 'dict' in str(type(v)):
            ov = r.get(key, None)
            if ov:
                r[key] = copy_dict(ov, v)
            else:
                r[key] = copy_dict({}, v)
        else:
            r[key] = v
    return r

def fill_template(dict_template, dict_source):
    r = copy.deepcopy(dict_template)
    for key in r:
        v = dict_source.get(key, None)
        if not v:
            continue
        r[key] = copy.deepcopy(v)
    return r
