from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    pass
    @property #abstract property
    @abstractmethod
    def alias(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property #abstract property
    def alias(self):
        return f"{self.__alias}"

class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property #abstract property
    def alias(self):
        return f"{self.__alias}"

class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property #abstract property
    def alias(self):
        return f"{self.__alias}"

class MichaelAngelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property #abstract property
    def alias(self):
        return f"{self.__alias}"