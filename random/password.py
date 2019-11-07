# coding: UTF-8

import random
import sys

sys.path.append('../Tools')
import char

def GetString(max_length, min_length = 1, char_string = ''):
    if not char_string or char_string is '':
        char_string = char.ASCII_ALL()
    clist = char.ToChars(char_string)
    index = random.randint(min_length, max_length)
    clist = random.sample(clist, index)
    return ''.join(clist)

if __name__ == '__main__':
    value = GetString(min_length = 15, max_length = 18)
    print("位数:", len(value))
    print("值:\n\t", value, '\n')
