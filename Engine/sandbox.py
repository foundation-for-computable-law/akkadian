from dsl import *


# RULES

# Substantive rules

#def is_qualifying_relative(a, b): return (
#    (age(a) < 18) &
#    (age(b) >= 18) &
#    (gender(b) == 'Female') &
#    ~ (relationship(a, b) == "Child")
#    )


def is_qualifying_relative(a, b):
    return And(age(a) < 18,
               age(b) >= 18,
               gender(b) == 'Female',
               Not(relationship(a, b) == "Child"),
               assessment_date() > Date(2000, 1, 1))


def another_rule(p):
    return Or(age(p) >= 12,
              citizenship(p) == "U.S. Citizen")


# FACTS

def age(p):
    return In("num", "age", p, None, "How old is {0}?")


def gender(p):
    return In("str", "gender", p, None, "What is {0}'s gender?")


def relationship(a, b):
    return In("str", "relationship", a, b, "How is {0} related to {1}?")


def citizenship(p):
    return In("str", "citizenship", p, None, "What is {0}'s U.S. citizenship status?")


def assessment_date():
    return In("date", "assessment_date", None, None, "What is the assessment date?")


# USAGE


# Getting the value of a fact
# fact("gender","jim").value
# fact("relationship","jim","jane").value

# Invoking rules
# is_qualifying_relative("jim","jane").value

# Apply the rules to a fact pattern
#print(Apply_rules(['sandbox.is_qualifying_relative("Jim","Lucy")','sandbox.another_rule("Lucy")']))

# Initiate an interactive interview
# Investigate(['sandbox.is_qualifying_relative("Jim","Lucy")'],[Fact("assessment_date", None, None, Date(1999,1,1))])
Investigate(['sandbox.is_qualifying_relative("Jim","Lucy")'])

