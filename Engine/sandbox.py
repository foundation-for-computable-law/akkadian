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


# Base-level facts from the rules
# These lookup facts from the fact list
def age(p): return fact("num", "age", p)
def gender(p): return fact("str", "gender", p)
def relationship(a, b): return fact("str", "relationship", a, b)


# FACTS




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
# investigate('sandbox.is_qualifying_relative("jim","jane")')
