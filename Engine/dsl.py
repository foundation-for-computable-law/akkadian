
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
        return self.value + o.value
    
    def __mul__(self, o): 
        return self.value * o.value

    def __sub__(self, o): 
        return self.value - o.value

    def __truediv__(self, o): 
        return self.value / o.value

    # Comparison...
    def __lt__(self, o):
        if type(self) is T and type(o) is T:
            return self.value < o.value
        elif type(self) is T:
            return self.value < o
        else:
            return self < o.value

    def __le__(self, o): 
        if self == T(None) or o == T(None):
            return T(None)
        elif type(self) is T and type(o) is T:
            return self.value <= o.value
        elif type(self) is T:
            return self.value <= o
        else:
            return self.value <= o.value

    def __eq__(self, o): 
        return T(self.value == o.value)

    def __ne__(self, o): 
        return self.value != o.value

    def __gt__(self, o): 
        return self.value > o.value

    def __ge__(self, o): 
        if self == T(None) or o == T(None):
            return T(None)
        elif type(self) is T and type(o) is T:
            return self.value >= o.value
        elif type(self) is T:
            return self.value >= o
        else:
            return self.value >= o.value

    # TODO: Add list operators



