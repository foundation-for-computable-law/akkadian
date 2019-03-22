from dsl import *


# RULES


# Evaluates whether anyone in the household list is eligible for a benefit
def household_has_eligible_member(household):
    return Exists(household, eligible_member(_, household))


# High-level eligibility
def eligible_member(person, household):
    return Or(is_eligible_cash_benefit(person, household),
              And(is_eligible_food_benefit(person),
                  is_eligible_health_benefit(person)))


# evaluate single person for cash benefit, eligible if there is at least one child, 1 or fewer adults
def is_eligible_cash_benefit(person, household):
    return And(under_19(person),
               num_adults(person, household) >= 0,
               num_children(person, household) > 1)


# if < 18 and is a child of someone in the household then true
def is_child(person, household):
    return And(age(person) <= 16,
               Exists(household, relationship(person, _) == 'Child'))  # How should this function work?


def is_parent(person, household):
    return Exists(household, Or(relationship(person, _) == "Parent",
                                relationship(_, person) == "Child"))


def under_19(person):
    return age(person) < 19


# Get count of children
def num_children(person, household):
    return Count_if(household, And(age(person) < 18,
                                   is_child(person, household))) # How should this function work?


# Get count of adults
def num_adults(person, household):
    return Count_if(household, Or(age(person) > 18,
                                  is_parent(person, household)))


def is_eligible_food_benefit(person):
    return False


def is_eligible_health_benefit(person):
    return False




# Base-level facts from the rules
# These lookup facts from the fact list
def age(p): return fact("num", "age", p)


def gender(p): return In("str", "gender", p)


def relationship(a, b): return In("str", "relationship", a, b)


def citizenship(p): return In("citizenship", p)



# USAGE


# Invoking rules
# household = ["jim", "jane"]
# print(household_has_eligible_member(household))
