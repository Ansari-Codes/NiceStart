class Variable:
    def __init__(self, name: str, value = None):
        self.name = name
        self.value = value

class Form:
    def __init__(self, variables = [], name:str = "form"):
        self.variables = variables
        self.name = name
    
    def add_variable(self, variable):
        self.variables.append(variable)
    
    def to_dict(self):
        toDict = {}
        for i in self.variables:
            toDict[i.name] = i.value
        return toDict
    
    def __getattr__(self, name):
        if name == 'variables':
            return self.variables
        elif name in [i.name for i in self.variables]:
            return [i for i in self.variables if i.name == name][0]
        else:
            raise AttributeError(f"Not Known property of Form: {name}")
    
    def __repr__(self):
        return f'{self.name.title()} Data:' + '\n' + '\n'.join([f"\t{i.name} = {i.value}" for i in self.variables])