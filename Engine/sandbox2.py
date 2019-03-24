from dsl import *


# RULES


#https://www.irs.gov/pub/irs-pdf/fw4.pdf
#IRS Form w4(2019) rules

#can we make person/spouse global?
def personal_allowances_wksheet_complete(person, spouse): return(
        claiming_self(person) + file_married_jointly(person, spouse) + file_head_of_household(person) +
        only_job_or_low_wage_second(person, spouse) + child_tax_credit() + credit_for_other_dependents() +
        other_credits() 
    )


#A, default to true/1?
def claiming_self(person): 
    if(claiming_self(person)):
        return (1)

#B, married, filing jointly
def file_married_jointly(person, spouse): 
    if(And(is_married(person, spouse), filing_jointly(person))):
        return 1 

#intermediates help with readability? 
def filing_jointly(person): return(tax_status)


#convert boolean to 1/0 for adding?
#C, head of household
def file_head_of_household(person): 
    #playing with docstring
    """
        Line C. Head of household please note:
    Generally, you may claim head of household
    filing status on your tax return only if you’re
    unmarried and pay more than 50% of the
    costs of keeping up a home for yourself and
    a qualifying individual. See Pub. 501 for
    more information about filing status
    """
    if(head_of_household(person)):
        return 1
    else:
        return 0



def only_job_or_low_wage_second(person, spouse):
    """
    • You’re single, or married filing separately, and have only one job; or
    •  You’re married filing jointly, have only one job, and your spouse doesn’t work; or
    • Your wages from a second job or your spouse’s wages (or the total of both) are $1,500 or less
    """
    #dev question, could we infer "only one job" as one active wages/employment record? Probably a question for policy team.
    #formatting? #readability?
    if(
        And(
            Or(is_single(person), 
            married_filing_separately)
        ),
        has_only_one_job(person)):
        return 1
    elif(
        And(
            file_married_jointly(person, spouse),
            has_only_one_job(person),
            spouse_unemployed(spouse))
    ):
        return 1
    elif(combined_couple_wages(person, spouse) <= 1500):
        return 1
    
def married_filing_separately(person, spouse): return(
    And(is_married(person, spouse),
    filing_separately(person)))

def filing_separately(p): return(Not(filing_jointly(p)))

def child_tax_credit(): return(0)
def credit_for_other_dependents(): return(0)
def other_credits(): return(0)


def spouse_unemployed(s): return(
    employment_status(s) != "Employed"
    )

def combined_couple_wages(person, spouse):
    #wages from person's first job, wages from spouse's job
    if(spouse is None):
        return wages_from_second_job(person)
    else:
        return wages_from_second_job(person) + persons_wages(spouse)

def has_only_one_job(person):
    if(count_of_jobs(person) == 1):
        return True
    else:
        return False
    



#base level attributes? Can we make these "fall out"?
def is_married(person, spouse): return relationship(person, spouse) == "Married"

def tax_status(p):
    return In("str", "tax_status", p, None, "How does {0} plan to file taxes?")

def head_of_household(p): return(In("bool", "head_of_household", p, None, "Is {0} the head of their household?"))

#converting boolean to integer for summing, is there a better pattern to employ?
def is_claiming_self(p): return(
    In("bool", "claim_self", p, None, "Does {0} intend to claim themself?")
    )

#can't prove !is_married without including a spouse, better way? Save married as var?
#def is_single(p): return(!is_married(person, spouse))


def employment_status(p): return(
    In("str", "employment_status", p, None, "What is {0}'s employment status?")
    )

def wages_from_second_job(p): 
    return In("num", "second_job_wages", p, None, "What was the total sum of wages for {0} from their second job last year?")

def persons_wages(p):
    return In("num", "wages", p, None, "What was the total sum of wages for {0} last year?")

def count_of_jobs(p):
    return In("num", "number_of_jobs", p, None, "How many jobs did {0} simultaneously hold last year?")







################### MOCK RULES ###################
# Evaluates whether anyone in the household list is eligible for a benefit
def household_has_eligible_member(household):
    return Exists(lambda x: eligible_member(x, household), household)


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
               Exists(lambda x: relationship(person, x) == 'Child', household))


def is_parent(person, household):
    return Exists(lambda x: Or(relationship(person, x) == "Parent",
                                relationship(x, person) == "Child"),
                  household)


def under_19(person):
    return age(person) < 19


# Get count of children
def num_children(person, household):
    return Count_if(household, And(age(person) < 18,
                                   is_child(person, household)))


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
def age(p):
    return In("num", "age", p, None, "How old is {0}?")


def gender(p):
    return In("str", "gender", p, None, "What is {0}'s gender?")


def relationship(a, b):
    return In("str", "relationship", a, b, "How is {0} related to {1}?")


def citizenship(p):
    return In("str", "citizenship", p, None, "What is {0}'s U.S. citizenship status?")



# USAGE


# Invoking rules
# household = ["jim", "jane"]
# print(household_has_eligible_member(household))
