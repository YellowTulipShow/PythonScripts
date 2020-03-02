# coding: UTF-8

import copy

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

def __test_copy_deepcopy():
    new = { 'vint': 11, }
    old = copy.deepcopy(new)
    print('复制数值:', old['vint'] == new['vint'])
    old['vint'] = 22
    print('修改数值:', old['vint'] != new['vint'])

    new = { 'vstr': 'qqq', }
    old = copy.deepcopy(new)
    print('复制字符串:', old['vstr'] == new['vstr'])
    old['vstr'] = 'www'
    print('修改字符串:', old['vstr'] != new['vstr'])

    new = { 'varr': [1,2,3], }
    old = copy.deepcopy(new)
    print('复制数组:', old['varr'] == new['varr'])
    old['varr'].append(4)
    print('修改数组:', len(old['varr']) != len(new['varr']))

    new = {
        'vobj': {
            'a': 1,
        },
    }
    old = copy.deepcopy(new)
    print('复制对象:', old['vobj']['a'] == new['vobj']['a'])
    old['vobj']['a'] = 2
    print('修改数组:', old['vobj']['a'] != new['vobj']['a'])

if __name__ == '__main__':
    __test_trim()
    __test_copy_dict()
    __test_copy_deepcopy()
