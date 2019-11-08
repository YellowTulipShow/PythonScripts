# coding: UTF-8

a = 1
b = 2
c = 3
d = 4
max = (a if a > b else b)
print(max)
max = (a > b and [a] or [b])[0] #list
print(max)
max = a>b and a or b>c and b or c>d and c or d
print(max)
max = a if a>b else b if b>c else c if c>d else d
print(max)

'''
学习到的博客文章
https://www.jb51.net/article/41974.htm

Python 官网对于三目表达式的讨论
https://www.python.org/dev/peps/pep-0308/
'''
