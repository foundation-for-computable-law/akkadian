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


# List of missing facts
missing_info = []


# List of asserted facts
facts = []


# Applies substantive rules to a fact pattern
# The goal is entered as a string, for example: "module.fcn('jim')"
def apply_rules(goal, fs):
    exec("import " + goal[0:goal.find('.')]) # Note: causes the imported module to be reevaluated
    missing_info.clear()
    for item in fs:
        facts.append(item)
    result = eval(goal)
    progress = len(facts) / max(len(facts) + len(missing_info), 1)
    return {
        "result": result.pretty(),
        "missing_info": missing_info,
        "progress" : round(progress, 2)
        }


# Gets the value for a fact
def fact(name, subj, obj = None):
    lookup = list(filter(lambda x: x.name == name and x.subject == subj and x.object == obj, facts))
    if lookup == []:
        # Prevent duplicates from being added
        if list(filter(lambda x: x[0] == name and x[1] == subj and x[2] == obj, missing_info)) == []:
            missing_info.append([name, subj, obj]) 
        return T(None)
    else:
        return T(lookup[0].value)


# T OBJECTS
# Eventually, these will be temporal objects

class T: 
    def __init__(self, value, cf = 1): 
        self.value = value
        self.cf = cf  # certainty factor

    # Display the value as a string
    def pretty(self):
        return str(self.value) + " (" + str(round(self.cf*100)) + "% certain)"
  
    # &
    def __and__(self, o):
        return internal_and(self, o)
    def __rand__(self, o):
        return internal_and(self, o)
    
    # |
    def __or__(self, o): 
        return internal_or(self, o)
    def __ror__(self, o): 
        return internal_or(self, o)

    # ~
    def __invert__(self):
        if self.value == None:
            return T(None)
        else:
            return T(not self.value, self.cf)

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

    def __rgt__(self, o): 
        return process_binary(operator.gt, o, self)
    
    def __ge__(self, o): 
        return process_binary(operator.ge, self, o)

    def __rge__(self, o): 
        return process_binary(operator.ge, o, self)
    
    # TODO: Add list operators


def internal_and(a, b):
    if type(a) is T and type(b) is T:
        return more_internal_and(a.value, b.value, a.cf * b.cf)
    elif type(a) is T:
        return more_internal_and(a.value, b, a.cf)
    elif type(b) is T:
        return more_internal_and(b.value, a, b.cf)
    else:
        return more_internal_and(a, b, 1)


def more_internal_and(a, b, cf):
    if a == False or b == False:
        return T(False, cf)
    elif a == None or b == None:
        return T(None, cf)
    else:
        return T(True, cf)

    
def internal_or(a, b):
    if type(a) is T and type(b) is T:
        return more_internal_or(a.value, b.value, a.cf + b.cf - (a.cf * b.cf))
    elif type(a) is T:
        return more_internal_or(a.value, b, a.cf)
    elif type(b) is T:
        return more_internal_or(b.value, a, b.cf)
    else:
        return more_internal_or(a, b, 1)


def more_internal_or(a, b, cf):
    if a == True or b == True:
        return T(True, cf)
    elif a == None or b == None:
        return T(None, cf)
    else:
        return T(False, cf)

    
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

