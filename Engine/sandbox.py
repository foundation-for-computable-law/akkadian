from dsl import *


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

print(T(234)+T(1243124))
