 # coding: UTF-8

import sys
import os
import json
import re
import datetime
import platform

sys.path.append('.')
import convert

def to_abs_directory(relatice_directory):
    abs_path = os.path.abspath(relatice_directory)
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
    return abs_path

def to_abs_path(relatice_directory, file):
    abs_directory = to_abs_directory(relatice_directory)
    def to_abs_file(abs_directory, file, symbol):
        if symbol in abs_directory:
            abs_directory = convert.trimEnd(abs_directory, symbol=symbol)
            abs_directory = abs_directory + symbol + file
        return abs_directory
    if '\\' in abs_directory:
        return to_abs_file(abs_directory, file, '\\')
    if '/' in abs_directory:
        return to_abs_file(abs_directory, file, '/')
    if 'Window' in platform.platform():
        return to_abs_file(abs_directory, file, '\\')
    return abs_directory

def file_read(abs_path):
    f = open(abs_path, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return content

def file_write(abs_path, content):
    f = open(abs_path, 'w', encoding='utf-8')
    f.write(content)
    f.close()
    return abs_path

# 原文链接：https://blog.csdn.net/mouday/article/details/91047387
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

def config_json_file_read(abs_path):
    content = file_read(abs_path)
    content = re.sub(r",(\s*[\}\]])", r"\1", content)
    return json.loads(content)

def config_json_file_write(abs_path, dict):
    content = json.dumps(dict, indent=4, ensure_ascii=False, cls=DateEncoder)
    return file_write(abs_path, content)

if __name__ == '__main__':
    path = to_abs_path('../config', 'databases.json')
    content = config_json_file_read(path)
    print(content)
    path = to_abs_path('../__auto__/config', 'databases.json')
    path = config_json_file_write(path, content)
    print(path)