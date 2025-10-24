from abc import abstractmethod, ABC

class Model(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def create(self, obj: dict):
        pass

    @abstractmethod
    def create(self, obj: dict):
        pass

    @abstractmethod
    def delete(self, obj: dict):
        pass

class Required(Exception):pass
class ValidationError(Exception):pass
