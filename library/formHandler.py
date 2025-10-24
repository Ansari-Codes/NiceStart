from typing import Any


class Variable:
    def __init__(self, name: str, value = None):
        self.name = name
        self.value = value

class Group:
    def __init__(self, variables = [], name:str = "Group"):
        self.variables = variables
        self._name = name
    
    def add_variable(self, variable):
        self.variables.append(variable)
    
    def to_dict(self):
        toDict = {}
        for i in self.variables:
            toDict[i.name] = i.value
        return toDict
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name == '_name':
            raise AttributeError("You cannot set _name, it is reserved!")
        setattr(self, name, value)
    
    def __getattr__(self, name):
        if name == 'variables':
            return self.variables
        elif name == '_name':
            raise AttributeError("_name is reserved for Group, you cannot access it.")
        elif name in [i.name for i in self.variables]:
            return [i for i in self.variables if i.name == name][0]
        else:
            raise AttributeError(f"Not Known property of Group: {name}")
    
    def __repr__(self):
        return f'{self.name.title()} Data:' + '\n' + '\n'.join([f"\t{i.name} = {i.value}" for i in self.variables])