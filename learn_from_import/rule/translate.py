# coding: UTF-8

from interface import IShow

class translate(IShow):
    def __init__(self):
        print('case translate.__init__()')
    def show(self):
        file.read()
        print('case translate.show()')

if __name__ == '__main__':
    tran = translate()
    tran.show()
