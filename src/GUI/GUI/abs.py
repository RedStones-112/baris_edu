from abc import *

class DBAbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def set_cammand(self):
        pass

    @abstractmethod
    def get_cammand(self, ID):
        pass

    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def disconnect_db(self):
        pass