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

#evaluate single person for cash benefit, eligible if there is at least one child, 1 or fewer adults
def is_eligible_cash_benefit(person, household):
    numAdults = 0
    numChildren = 0

    #nested function specific to cash benefit
    def is_child(person, household):
        focal = person
        if age(focal) > 17:
            return False 
        #if < 18 and is a child of someone in the household then true
        for hhm in household:
            if relationship(focal, hhm) == 'Child':
                print(focal + " is a child")
                return True
    
    #nested function specific to cash benefit   
    def is_parent(person, household):
        focal = person
        for hhm in household:
            if relationship(focal, hhm) == 'Parent' & relationship(focal, hhm) != None :
                print(focal + " is a parent of " + hhm)
                return True
    
    def under_19(person): return (
        (age(person) == 18) |
            ((age(person) < 18) & 
             ~(age(person) >= 19)))

    #get count of children and adults
    for person in household:
        if(age(person) < 18 & is_child(person, household)):
            numChildren += 1
        if(age(person) > 18 | is_parent(person, household)):
            numAdults += 1

    #if under 18 or (just for testing) not greater than or equal to 19 or equal to 18 and 0 or more adults and 1 or more children
    return (under_19(person) & 
        numAdults >= 0 & 
        numChildren > 1
        )
        

def is_eligible_food_benefit(person):
    return False

def is_eligible_health_benefit(person):
    return False

#takes list of household members and evalutes whether anyone in the household list is eligible for a benefit
def household_has_eligible_member(household): 

    for person in household:
        return (
            is_eligible_cash_benefit(person, household) | 
            (is_eligible_food_benefit(person) & is_eligible_health_benefit(person))
        )
    return False


# Base-level facts from the rules
# These lookup facts from the fact list
def age(p): return fact("num", "age", p)
def gender(p): return fact("str", "gender", p)
def relationship(a, b): return fact("str", "relationship", a, b)
def citizenship(p): return fact("citizenship", p)

# FACTS




# USAGE


# Getting the value of a fact
# fact("gender","jim").value
# fact("relationship","jim","jane").value

# Invoking rules
#is_qualifying_relative("jim","jane").value
household = ["jim", "jane"]
print(household_has_eligible_member(household))

# Apply the rules to a fact pattern
# apply_rules('sandbox.is_qualifying_relative("jim","jane")',
#             [Fact("age", "jim", None, 88),
#              Fact("gender","jone",None,"Female")]))

# Initiate an interactive interview
# investigate('sandbox.is_qualifying_relative("jim","jane")')
