from dsl import *


# RULES

# Substantive rules

#def is_qualifying_relative(a, b): return (
#    (age(a) < 18) &
#    (age(b) >= 18) &
#    (gender(b) == 'Female') &
#    ~ (relationship(a, b) == "Child")
#    )


def is_qualifying_relative(a, b): return (
    And(age(a) < 18,
        age(b) >= 18,
        gender(b) == 'Female',
        Not(relationship(a, b) == "Child"))
    )


# FACTS

def age(p): return fact("num", "age", p, None, "How old is {0}?")


def gender(p): return fact("str", "gender", p, None, "What is {0}'s gender?")


def relationship(a, b): return fact("str", "relationship", a, b, "How is {0} related to {1}?")


def citizenship(p): return fact("citizenship", p, None, "What is {0}'s U.S. citizenship status?")


# USAGE


# Getting the value of a fact
# fact("gender","jim").value
# fact("relationship","jim","jane").value

# Invoking rules
#is_qualifying_relative("jim","jane").value

# Apply the rules to a fact pattern
# apply_rules('sandbox.is_qualifying_relative("jim","jane")',
#             [Fact("age", "jim", None, 88),
#              Fact("gender","jone",None,"Female")]))

# Initiate an interactive interview
investigate('sandbox.is_qualifying_relative("Jim","Lucy")')
