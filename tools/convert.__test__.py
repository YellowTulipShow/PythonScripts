# coding: UTF-8

import convert

def __test_trim():
    test_str_trim = '  22 55 00 33  '
    print('trimStart: "{str}"'.format(str=convert.trimStart(test_str_trim)))
    print('trimEnd: "{str}"'.format(str=convert.trimEnd(test_str_trim)))
    print('trim: "{str}"'.format(str=convert.trim(test_str_trim)))
    test_str_trim = '14%@22 55 00 3314%@'
    print('trimStart: "{str}"'.format(str=convert.trimStart(test_str_trim, symbol=r'14%@')))
    print('trimEnd: "{str}"'.format(str=convert.trimEnd(test_str_trim, symbol=r'14%@')))
    print('trim: "{str}"'.format(str=convert.trim(test_str_trim)))

def __test_copy_dict():
    dict_old = {}
    dict_new = {
        'a': 1,
        'b': 2,
        'c': {
            'e': 555,
        }
    }
    convert.copy_dict(dict_old, dict_new)
    print(dict_old)
    dict_new = {
        'a': 3,
        'b': 4,
        'c': {
            'd': 22,
        },
    }
    convert.copy_dict(dict_old, dict_new)
    print(dict_old)
    dict_new = {
        'a': 5,
        'c': {
            'e': 666,
        },
    }
    convert.copy_dict(dict_old, dict_new)
    print(dict_old)

if __name__ == '__main__':
    __test_trim()
    __test_copy_dict()
