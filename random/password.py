# coding: UTF-8
import random

nmin = 11
mmax = 19

sl = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

sl = '0123456789'
sl += 'abcdefghijklmnopqrstuvwxyz'
# sl += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# sl += '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

## 输出 ASCII 常用字符编码表
# for i in range(0, len(sl)):
#     print("i:", i+33, "c:", sl[i])

sl = [ c for c in sl]
rl = random.randint(nmin, mmax)
sl = random.sample(sl, rl)
sl = ''.join(sl)

print("{}  位数:{}\n".format(sl, len(sl)))
