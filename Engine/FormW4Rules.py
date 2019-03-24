from dsl import *
#https://www.irs.gov/pub/irs-pdf/fw4.pdf
#IRS Form w4(2019) rules

#can we make person/spouse global?
def personal_allowances_wksheet_complete(person, spouse): return(
        claiming_self(person) + file_married_jointly(person, spouse) + file_head_of_household(person) 
        + only_job_or_low_wage_second(person, spouse) + child_tax_credit() + credit_for_other_dependents() 
        + other_credits() 
    )


#A, default to true/1?
def claiming_self(person): 
    #fix if
    If(is_claiming_self(person)):
        return 1

#B, married, filing jointly
def file_married_jointly(person, spouse): 
    If(And(is_married(person, spouse), 
        filing_jointly(person))):
        return 1 

#intermediates help with readability? 
def filing_jointly(person): 
    return(tax_status)


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
    
def married_filing_separately(person, spouse): 
    return(
        And(is_married(person, spouse),
        filing_separately(person))
    )

def filing_separately(p): 
    return(
        Not(
            filing_jointly(p)
            )
            )

def child_tax_credit(person, spouse): 
    """
    Child tax credit. See Pub. 972, Child Tax Credit, for more information.
    • If your total income will be less than $71,201 ($103,351 if married filing jointly), enter 4 for each eligible child.
    • If your total income will be from $71,201 to $179,050 ($103,351 to $345,850 if married filing jointly), enter 2 for each
    eligible child.
    • If your total income will be from $179,051 to $200,000 ($345,851 to $400,000 if married filing jointly), enter 1 for
    each eligible child.
    • If your total income will be higher than $200,000 ($400,000 if married filing jointly), enter -0- . . . . . . .
    """

    If(spouse is not None):
        If(file_married_jointly(person, spouse)):
            If(total_income(person) + total_income(spouse) < 103,351):
                return 4 * num_children(person)
            elif(And(total_income(person) + total_income(spouse) >= 103,351,
                total_income(person) + total_income(spouse) <= 345,850)):
                return 2 * num_children(person)
            elif(And(total_income(person) + total_income(spouse) >= 345,851,
                total_income(person) + total_income(spouse) <= 400,000)):
                return num_children(person)
            else:
                return 0

    #no spouse
    else:
        If(total_income(person) < 71,201):
            return 4 * num_children(person)
        elif(And(total_income(person) >= 71,201,
            total_income(person) <=179,051)):
            return 2 * num_children(person)
        elif(And(total_income(person) >= 179,051,
            total_income(person) <=200,000)):
            return num_children(person)
        else:
            return 0

def credit_for_other_dependents(): 
    """
    Credit for other dependents. See Pub. 972, Child Tax Credit, for more information.
    • If your total income will be less than $71,201 ($103,351 if married filing jointly), enter “1” for each eligible dependent.
    • If your total income will be from $71,201 to $179,050 ($103,351 to $345,850 if married filing jointly), enter “1” for every
    two dependents (for example, “-0-” for one dependent, “1” if you have two or three dependents, and “2” if you have
    four dependents).
    • If your total income will be higher than $179,050 ($345,850 if married filing jointly), enter “-0-” . . . . . .
    """
    If(spouse is not None):
        If(file_married_jointly(person, spouse)):
            If(total_income(person) + total_income(spouse) < 103,351):
                return num_dependents(person)
            elif(And(total_income(person) + total_income(spouse) >= 103,351,
                total_income(person) + total_income(spouse) <= 345,850)):
                return math.floor(num_dependents(person) / 2)
            elif(total_income(person) + total_income(spouse) > 345,850):
                return 0
    #no spouse
    else:
        If(total_income(person) < 71,201):
            return num_dependents(person)
        elif(And(total_income(person) >= 71,201,
            total_income(person) <=179,051)):
            return math.floor(num_dependents(person) / 2)
        elif(total_income(person) > 179,050):
            return 0


def other_credits(person): 
    """
    Other credits. If you have other credits, see Worksheet 1-6 of Pub. 505 and enter the amount from that worksheet
    here. If you use Worksheet 1-6, enter “-0-” on lines E and F . . . . 
    """
    If(has_other_credits(person)):
        return other_credits_pub505(person)
    else:
        return 0


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
def is_married(person, spouse): 
    return marital_status(p) == "Married"

def marital_status(p):
    return(In("str", "marital_status", p, None, "What is {0}'s marital status?"))

def tax_status(p):
    return In("str", "tax_status", p, None, "How does {0} plan to file taxes?")

def head_of_household(p): 
    return(In("bool", "head_of_household", p, None, "Is {0} the head of their household?"))

#converting boolean to integer for summing, is there a better pattern to employ?
def is_claiming_self(p): 
    return(In("bool", "claim_self", p, None, "Does {0} intend to claim themself?"))

def employment_status(p): 
    return(In("str", "employment_status", p, None, "What is {0}'s employment status?"))

def wages_from_second_job(p): 
    return In("num", "second_job_wages", p, None, "What was the total sum of wages for {0} from their second job last year?")

def persons_wages(p):
    return In("num", "wages", p, None, "What was the total sum of wages for {0} last year?")

def count_of_jobs(p):
    return In("num", "number_of_jobs", p, None, "How many jobs did {0} simultaneously hold last year?")

#certainty < 1, is single single or is single/widowed single?
def is_single(p):
    return Or(marital_status(p) == "Single, unmarried, or legally separated", 
    marital_status(p) == "Widowed (spouse died during the tax year)",
    marital_status(p) == "Widowed (spouse died before the tax year)")

def has_other_credits(p):
    return In("bool", "has_other_credits_pub505", p, None, "Does {0} have other credits from Worksheet 1-6 of Pub. 505?")

def other_credits_pub505(p):
    return In("num", "other_credits_pub505", p, None, "How many other credits does {0} have from Worksheet 1-6 of Pub. 505?")