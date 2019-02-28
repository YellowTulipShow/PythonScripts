# coding: UTF-8
import random

sl = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

## 输出 ASCII 常用字符编码表
# for i in range(0, len(sl)):
#     print("i:", i+33, "c:", sl[i])

sl = [ c for c in sl]
rl = random.randint(11, 19)
sl = random.sample(sl, rl)
sl = ''.join(sl)

print("{}  位数:{}\n".format(sl, len(sl)))
