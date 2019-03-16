# RULEBASE

# Substantive rules

def is_qualifying_relative(a, b): return (
    age(a) < 18 and
    age(b) >= 18 and
    gender(b) == 'Female' and
    not relationship(a, b) == "Child")


# Base-level facts from the rules
# These lookup facts from the fact list
def age(p): return fact("age", p)
def gender(p): return fact("gender", p)
def relationship(a, b): return fact("relationship", a, b)


# FACTS - MACHINERY


# Stores pieces of knowledge about the world
class Fact:

    # Initializer / Instance Attributes
    def __init__(self, name, subject, object, value):
        self.name = name
        self.subject = subject
        self.object = object
        self.value = value


# List of asserted facts (with mock values)
facts = [
    Fact("age", "jim", None, 8),
    Fact("age", "jane", None, 92),
    Fact("gender", "jim", None, "Male"),
    Fact("gender", "jane", None, "Female"),
    Fact("relationship", "jim", "jane", "Parent")
]


# List of missing facts
missing_info = []


# Gets the value for a fact
def fact(name, subj, obj = None):
    lookup = list(filter(lambda x: x.name == name and x.subject == subj and x.object == obj, facts))
    if lookup == []:
        missing_info.append([name, subj, obj])
        return None
    else:
        return lookup[0].value

def delete_duplicates(x):
  return list(dict.fromkeys(x))


# USAGE


# Getting the value of a fact
print(fact("gender","jim"))
print(fact("citizenship","jim"))
print(fact("relationship","jim","jane"))

# Invoking rules
print(age("jim"))
print(is_qualifying_relative("jim","jane"))

# Getting a list of missing information
missing_info = []
relationship("jim","art") == "Siblings" and gender("jim") == 'Female'
print(missing_info)


