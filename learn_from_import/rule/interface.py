# coding: UTF-8

from abc import abstractmethod,ABCMeta

class IShow(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass
