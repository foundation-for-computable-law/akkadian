from dsl import *


# RULES

# Substantive rules

def is_qualifying_relative(a, b): return (
    age(a) < 18 &
    age(b) >= 18 &
    gender(b) == 'Female' &
    ~ relationship(a, b) == "Child"
    )


# Base-level facts from the rules
# These lookup facts from the fact list
def age(p): return fact("age", p)
def gender(p): return fact("gender", p)
def relationship(a, b): return fact("relationship", a, b)


# FACTS




# USAGE


# Getting the value of a fact
# fact("gender","jim").value
# fact("relationship","jim","jane").value

# Invoking rules
# is_qualifying_relative("jim","jane").value

# Getting a list of missing information
# print(get_missing_data('sandbox.is_qualifying_relative("jim","jane")', "sandbox", []))
