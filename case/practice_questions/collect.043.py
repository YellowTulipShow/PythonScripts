# coding: UTF-8

print(r'''
【程序43】题目：求0—7所能组成的奇数个数。
''')

numlist = [i for i in range(0, 7+1)]
print(numlist)

for item in numlist:
    pass

# 01234567
# 10234567
# 12034567
# 12304567
# 12340567
# 12345067
# 12345607
# 12345670
# 21345670
# ...
# 23456701
# 32456701
# ...
# 34567012
# 43567012
# 35670124
# ...
# 70124356
# ...
# 01243567


012
021
102
120
201
210
