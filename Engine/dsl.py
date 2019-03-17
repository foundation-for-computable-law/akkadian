import operator


# FACTS - MACHINERY


# Stores pieces of knowledge about the world
class Fact:

    # Initializer / Instance Attributes
    def __init__(self, name, subject, object, value):
        self.name = name
        self.subject = subject
        self.object = object
        self.value = value


# Data structures
facts = []
missing_info = []


# List of asserted facts (with mock values)
facts = [
    Fact("age", "jim", None, 8),
    Fact("age", "jane", None, 92),
    Fact("gender", "jim", None, "Male"),
    Fact("gender", "jane", None, "Female"),
    Fact("relationship", "jim", "jane", "Parent")
]


# Gets the value for a fact
def fact(name, subj, obj = None):
    lookup = list(filter(lambda x: x.name == name and x.subject == subj and x.object == obj, facts))
    if lookup == []:
        missing_info.append([name, subj, obj])
        return T(None)
    else:
        return T(lookup[0].value)

def delete_duplicates(x):
  return list(dict.fromkeys(x))


# T OBJECTS
# Eventually, these will be temporal objects

class T: 
    def __init__(self, value): 
        self.value = value
  
    # &
    def __and__(self, o):
        if self.value == False or o.value == False:
            return T(False)
        elif self.value == None or o.value == None:
            return T(None)
        else:
            return T(True)

    # |
    def __or__(self, o): 
        if self.value == True or o.value == True:
            return T(True)
        elif self.value == None or o.value == None:
            return T(None)
        else:
            return T(False)

    # ~
    def __invert__(self):
        if self.value == None:
            return T(None)
        else:
            return T(not self.value)

    # Arithmetic...
    def __add__(self, o): 
        return process_binary(operator.add, self, o)

    def __radd__(self, o): 
        return process_binary(operator.add, self, o)
    
    def __mul__(self, o): 
        return process_binary(operator.mul, self, o)

    def __rmul__(self, o): 
        return process_binary(operator.mul, self, o)
    
    def __sub__(self, o): 
        return process_binary(operator.sub, self, o)

    def __rsub__(self, o): 
        return process_binary(operator.sub, o, self)
    
    def __truediv__(self, o): 
        return process_binary(operator.truediv, self, o)

    def __rtruediv__(self, o): 
        return process_binary(operator.truediv, o, self)
    
    # Comparison...
    def __lt__(self, o):
        return process_binary(operator.lt, self, o)

    def __le__(self, o): 
        return process_binary(operator.le, self, o)

    def __eq__(self, o):
        # Hacking equality == playing with fire
         return process_binary(operator.eq, self, o)

    def __ne__(self, o): 
        return ~ (self == o)

    def __gt__(self, o): 
        return process_binary(operator.gt, self, o)

    def __ge__(self, o): 
        return process_binary(operator.ge, self, o)

    # TODO: Add list operators


# Internal processing of binary operators
# TODO: Make this a private method, if possible
def process_binary(f, a, b):
    if is_none(a) or is_none(b):
        return T(None)
    elif type(a) is T and type(b) is T:
        return T(f(a.value, b.value))
    elif type(a) is T:
        return T(f(a.value, b))
    else:
        return T(f(a, b.value))


def is_none(a):
    return type(a) is T and a.value == None

