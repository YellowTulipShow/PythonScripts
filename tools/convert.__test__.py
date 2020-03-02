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

def __test_fill_template():
    dict_template = {
        'vint': 11,
        'vstr': 'qqq',
        'varr': [4],
    }
    dict_source = {
        'vint': 22,
        'varr': [1,2,3],
    }
    dict_result = convert.fill_template(dict_template, dict_source)
    print('填充数值:', dict_result['vint'] == dict_source['vint'])
    print('填充字符串:', dict_result['vstr'] == 'qqq')
    dict_result['varr'].append(5)
    print('填充数组:', len(dict_result['varr']) != len(dict_source['varr']))

if __name__ == '__main__':
    __test_trim()
    __test_copy_dict()
    __test_copy_deepcopy()
    __test_fill_template()
