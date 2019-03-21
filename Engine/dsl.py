import datetime
import functools
import operator
from datetime import date


# TODO: Reorganize this file


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


# Generates an interactive interview to collect info to resolve a goal
def Investigate(goals: list, fs=[]):

    # Call the "apply rules" interface
    re = Apply_rules(goals, fs)

    # If all of the goals have been determined, present the results
    if re["complete"]:
        print(re["msg"])  # TODO

    # Otherwise, ask the next question...
    else:
        # Find out what the next question is
        nxt = re["missing_info"][0]

        # Ask it
        new = input(nxt[4])

        # Add the newly acquired fact to the fact list
        fs.append(Fact(nxt[1], nxt[2], nxt[3], convert_input(nxt[0], new)))

        # Go to step 1
        Investigate(goals, fs)


# Convert inputs from the terminal to the desired type
# Assumes dates are entered as yyyy-mm-dd
def convert_input(typ: str, val: str):
    if typ == "num":
        return float(val)
    elif typ == "date":
        return date.fromisoformat(val)
    elif typ == "str":
        return val
    elif typ == "bool":
        if val in ("true", "True", "T", "t", "yes", "y"):
            return True
        else:
            return False
    else:
        return val


# Applies substantive rules to a fact pattern
# Returns a determination or a list of needed information
# Each goal is entered as a string, for example: "module.fcn('jim')"
def Apply_rules(goals: list, fs=[]):

    # Load namespaces
    for goal in goals:
        exec("import " + goal[0:goal.find('.')]) # Note: causes the imported module to be reevaluated

    # Clear and reload data structures
    missing_info.clear()
    facts.clear()
    for item in fs:
        facts.append(item)

    # Evaluate goals (causing missing_info to be reloaded)
    results = list(map(eval, goals))

    # Estimate interview progress
    progress = len(facts) / max(len(facts) + len(missing_info), 1)

    # Have all of the goals been determined?
    complete = all(map(lambda x : x.value is not None, results))

    # For each result, format it as a dictionary
    # TODO: In each dictionary, include the function name that was being called
    result_blocks = list(map(lambda x : process_results(x), results))

    # Housekeeping
    facts.clear()

    # Mic drop
    return {
        "complete": complete,
        "progress": 1.0 if complete else round(progress, 2),
        "msg": results[0].pretty(),  # TODO: Generalize to multiple goals
        "results": result_blocks,
        "missing_info": [] if complete else missing_info
    }


# Gets the value for a fact
def In(typ: str, name: str, subj, obj, question=None):

    # See if the desired fact is in the "facts" data structure
    lookup = list(filter(lambda x: x.name == name and x.subject == subj and x.object == obj, facts))

    # If not, add it
    if lookup == []:

        # Prevent duplicates from being added
        if list(filter(lambda x: x[1] == name and x[2] == subj and x[3] == obj, missing_info)) == []:
            missing_info.append([typ, name, subj, obj, text_subst(subj, obj, question)])

        # Indicate lack of knowledge
        return T(None)

    # If the fact is known, return its value
    else:
        return T(lookup[0].value)


# Substitute the subject ({0}) and object ({1}) of a fact into the question text
def text_subst(sbj: str, obj: str, question: str):
    if obj is None:
        return question.format(sbj) + " "
    else:
        return question.format(sbj, obj) + " "


# T OBJECTS
# Eventually, these will be temporal objects

class T: 
    def __init__(self, value, cf=1):
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
        if self.value is None:
            return T(None)
        else:
            return T(not self.value, self.cf)

    # Arithmetic...
    def __add__(self, o): 
        return process_binary(operator.add, self, o)

    def __radd__(self, o): 
        return process_binary(operator.add, self, o)

    # TODO: Add short-circuiting for mul * 0
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


def And(*args):
    return functools.reduce(internal_and, args)


def Or(*args):
    return functools.reduce(internal_or, args)


def Not(a):
    if type(a) is T and a.value is None:
        return T(None)
    elif type(a) is not T:
        return T(not a, 1)
    else:
        return T(not a.value, a.cf)


# TODO: Implement lazy evaluation so args b and c are only invoked as needed
# TODO: Finish implementing certainty factors
def If(a, b, c):
    if is_none(a):
        return T(None, a.value)
    elif type(a) is not T and a is None:
        return T(None, 1)
    elif (type(a) is T and a.value is True) or (type(a) is not T and a is True):
        if type(b) is T:
            return b
        else:
            return T(b)
    else:
        if type(c) is T:
            return c
        else:
            return T(c)


# TODO: Make the methods below private, if possible


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
    if a is False or b is False:
        return T(False, cf)
    elif a is None or b is None:
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
    if a is True or b is True:
        return T(True, cf)
    elif a is None or b is None:
        return T(None, cf)
    else:
        return T(False, cf)

    
# Internal processing of binary operators

def process_binary(f, a, b):
    if is_none(a) or is_none(b):
        return T(None, max(get_cf(a), get_cf(b)))
    elif type(a) is T and type(b) is T:
        return T(f(a.value, b.value), a.cf * b.cf)
    elif type(a) is T:
        return T(f(a.value, b), a.cf)
    else:
        return T(f(a, b.value), b.cf)


def get_cf(a):
    if type(a) is T:
        return a.cf
    else:
        return 1


def is_none(a):
    return type(a) is T and a.value is None


# Given a T object, format its values into a dictionary
def process_results(result : T):
    return {
        "result": result.value,
        "certainty": result.cf,
        "msg": result.pretty(),
        "complete": result.value is not None
    }


# A convenience function to make date construction less verbose
# TODO: Handle uncertainty and T values
def Date(y : int, m : int, d: int):
    return date(y, m, d)


# Returns the current date
Now = date.today()
