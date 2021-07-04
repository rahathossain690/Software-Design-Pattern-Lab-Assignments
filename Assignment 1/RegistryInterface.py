"""
Rahat Hossain
SH-32
2-7-21
"""

from abc import ABCMeta, abstractmethod

class RegistryInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def register(self):
        pass
    

    @abstractmethod
    def renew(self):
        pass

    @abstractmethod
    def registry_information(self):
        pass