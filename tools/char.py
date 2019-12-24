# coding: UTF-8

def ToChars(char_string):
    # 字符串转字符数组序列
    return [c for c in char_string];

def ToString(chars):
    # 字符数组序列转为字符串
    return ''.join(chars)

def ASCII_ALL():
    # 33, 127 -> ASCII 所有常用字符
    return '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def ASCII_Number():
    # 48,58 -> 阿拉伯数字
    return '0123456789';

def ASCII_UpperEnglish():
    # 65,91 -> 大写英文
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ASCII_LowerEnglish():
    # 97,123 -> 小写英文
    return 'abcdefghijklmnopqrstuvwxyz'

def ASCII_Special():
    # 特别字符
    c_33_48 = '!"#$%&\'()*+,-./'
    c_58_65 = ':;<=>?@'
    c_91_97 = '[\\]^_`'
    c_123_127 = '{|}~'
    return c_33_48 + c_58_65 + c_91_97 + c_123_127

def ASCII_WordText():
    # ASCII 常用工作文本字符
    return ASCII_Number() + ASCII_LowerEnglish() + ASCII_UpperEnglish()

def ASCII_Hexadecimal():
    # ASCII 码十六进制组成字符
    return '0123456789abcdef'

if __name__ == '__main__':
    print('ASCII 所有常用字符:\n\t', ASCII_ALL())
    print('ASCII 常用工作文本字符:\n\t', ASCII_WordText())
    print('阿拉伯数字:\n\t', ASCII_Number())
    print('大写英文:\n\t', ASCII_UpperEnglish())
    print('小写英文:\n\t', ASCII_LowerEnglish())
    print('特别字符:\n\t', ASCII_Special())
    print('ASCII 码十六进制组成字符:\n\t', ASCII_Hexadecimal())
