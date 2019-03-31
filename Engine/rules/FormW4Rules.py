from dsl import *
# https://www.irs.gov/pub/irs-pdf/fw4.pdf
# IRS Form w4(2019) rules


############### source rules ###############
def form_w4_complete(person, spouse):
    return And(
        personal_allowances_wksheet_complete(person, spouse),
        Or(
            (not plans_to_itemize_or_claim_adjustments(person)), deductions_adjustments_and_additional_income_wksht_complete(person)),
        Or(not two_earners_mult_jobs_wksht_required(person, spouse), two_earners_mult_jobs_wksht_complete(person, spouse)))



#######PERSONAL ALLOWANCES WORKSHEET#######
# can we make person/spouse global?
def personal_allowances_wksheet_complete(person, spouse):
    # check complete if line h is known?
    return personal_allowances_worksheet_line_h >= 0


# A, default to true/1?
def claiming_self(person):
    return If(is_claiming_self(person), 1, 0)


# B, married, filing jointly
def file_married_jointly(person, spouse):
    return If(And(is_married(person, spouse), filing_jointly(person)), 1, 0)


# intermediates help with readability?
def filing_jointly(p):
    return tax_status(p) == "Married Filing Jointly"


# convert boolean to 1/0 for adding?
# C, head of household
def file_head_of_household(person):
    # playing with docstring
    """
        Line C. Head of household please note:
    Generally, you may claim head of household
    filing status on your tax return only if you’re
    unmarried and pay more than 50% of the
    costs of keeping up a home for yourself and
    a qualifying individual. See Pub. 501 for
    more information about filing status
    """
    return If(head_of_household(person), 1, 0)


def only_job_or_low_wage_second(person, spouse):
    """
    • You’re single, or married filing separately, and have only one job; or
    •  You’re married filing jointly, have only one job, and your spouse doesn’t work; or
    • Your wages from a second job or your spouse’s wages (or the total of both) are $1,500 or less
    """
    # dev question, could we infer "only one job" as one active wages/employment record? Probably a question for policy team.
    # formatting? #readability?
    If(
        Or(
            And(
                Or(is_single(person),
                   married_filing_separately(person, spouse)),
                has_only_one_job(person)),
            And(
                file_married_jointly(person, spouse),
                has_only_one_job(person),
                spouse_unemployed(spouse)
            ),
            combined_couple_wages(person, spouse) <= 1500),
        1,
        0)


def married_filing_separately(person, spouse):
    return And(is_married(person, spouse),
               filing_separately(person))


def filing_separately(p):
    return Not(filing_jointly(p))


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
            If(total_income(person) + total_income(spouse) < 103, 351):
                return 4 * num_children(person)
            elif(And(total_income(person) + total_income(spouse) >= 103, 351,
                     total_income(person) + total_income(spouse) <= 345, 850)):
                return 2 * num_children(person)
            elif(And(total_income(person) + total_income(spouse) >= 345, 851,
                     total_income(person) + total_income(spouse) <= 400, 000)):
                return num_children(person)
            else:
                return 0

    # no spouse
    else:
        If(total_income(person) < 71, 201):
            return 4 * num_children(person)
        elif(And(total_income(person) >= 71, 201,
                 total_income(person) <= 179, 051)):
            return 2 * num_children(person)
        elif(And(total_income(person) >= 179, 051,
                 total_income(person) <= 200, 000)):
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
            If(total_income(person) + total_income(spouse) < 103, 351):
                return num_dependents(person)
            elif(And(total_income(person) + total_income(spouse) >= 103, 351,
                     total_income(person) + total_income(spouse) <= 345, 850)):
                return math.floor(num_dependents(person) / 2)
            elif(total_income(person) + total_income(spouse) > 345, 850):
                return 0
    # no spouse
    else:
        If(total_income(person) < 71, 201):
            return num_dependents(person)
        elif(And(total_income(person) >= 71, 201,
                 total_income(person) <= 179, 051)):
            return math.floor(num_dependents(person) / 2)
        elif(total_income(person) > 179, 050):
            return 0


def other_credits(person):
    """
    Other credits. If you have other credits, see Worksheet 1-6 of Pub. 505 and enter the amount from that worksheet
    here. If you use Worksheet 1-6, enter “-0-” on lines E and F . . . . 
    """
    return If(has_other_credits(person), other_credits_pub505(person), 0)


def personal_allowances_worksheet_line_h(person):
    return(claiming_self(person) + file_married_jointly(person, spouse) + file_head_of_household(person)
           + only_job_or_low_wage_second(person, spouse) + child_tax_credit(
               person) + credit_for_other_dependents(person)
           + other_credits(person))


#######Deductions, Adjustments, and Additional Income Worksheet#######
def deductions_adjustments_and_additional_income_wksht_complete(person):
    """
    Note: Use this worksheet only if you plan to itemize deductions, claim certain adjustments to income, or have a large amount of nonwage
    income not subject to withholding.
    """
    return ded_adj_adtl_inc_line_10 >= 0


def ded_adj_adtl_inc_line_1(person):
    # Enter an estimate of your 2019 itemized deductions. These include qualifying home mortgage interest,
    # charitable contributions, state and local taxes (up to $10,000), and medical expenses in excess of 10% of
    # your income. See Pub. 505 for details . . . . . . . . . . . . . . . . . . . . . .
    return itemized_deductions_2019(person)


def ded_adj_adtl_inc_line_2(person):
    # 2 Enter: { $24,400 if you’re married filing jointly or qualifying widow(er)
    # $18,350 if you’re head of household
    # $12,200 if you’re single or married filing separately } . .
    If(
            Or(filing_jointly(person), qualifying_widower(person))):
        return 24400
    Elif(head_of_household(person))
    return 18350
    Elif(
        Or(is_single(person), filing_separately(person)))
    return 12200


def ded_adj_adtl_inc_line_3(person):
    # Subtract line 2 from line 1. If zero or less, enter “-0-”
    If(ded_adj_adtl_inc_line_1(person) - ded_adj_adtl_inc_line_2(person) >= 0):
        return ded_adj_adtl_inc_line_1(person) - ded_adj_adtl_inc_line_2(person)
    Else:
        return False


def ded_adj_adtl_inc_line_4(person):
    # Enter an estimate of your 2019 adjustments to income, qualified business income deduction, and any
    # additional standard deduction for age or blindness (see Pub. 505 for information about these items) . .
    return estimate_2019_adj_to_inc_qual_bus_inc_ded_addtl_std_ded(person)


def ded_adj_adtl_inc_line_5(person):
    # Add lines 3 and 4 and enter the total
    return ded_adj_adtl_inc_line_3(person) + ded_adj_adtl_inc_line_4(person)


def ded_adj_adtl_inc_line_6(person):
    # Enter an estimate of your 2019 nonwage income not subject to withholding (such as dividends or interest) .
    return estimate_2019_nonwage_inc_not_subj_to_withholding(person)


def ded_adj_adtl_inc_line_7(person):
    # Subtract line 6 from line 5. If zero, enter “-0-”. If less than zero, enter the amount in parentheses
    return ded_adj_adtl_inc_line_5(person) - ded_adj_adtl_inc_line_6(person)


def ded_adj_adtl_inc_line_8(person):
    # Divide the amount on line 7 by $4,200 and enter the result here. If a negative amount, enter in parentheses.
    # Drop any fraction
    return math.floor(ded_adj_adtl_inc_line_7(person) / 4200)


def ded_adj_adtl_inc_line_9(person):
    # Enter the number from the Personal Allowances Worksheet, line H, above
    return personal_allowances_worksheet_line_h(person)


def ded_adj_adtl_inc_line_10(person):
    # Add lines 8 and 9 and enter the total here. If zero or less, enter “- 0 -”. If you plan to use the Two-Earners/
    # Multiple Jobs Worksheet, also enter this total on line 1 of that worksheet on page 4. Otherwise, stop here
    # and enter this total on Form W-4, line 5, page 1
    return max(ded_adj_adtl_inc_line_8(person) + ded_adj_adtl_inc_line_9(person), 0)


###############Two Earners/Multiple Jobs Wksht###############
    # Note: Use this worksheet only if the instructions under line H from the Personal Allowances Worksheet direct you here.

def two_earners_mult_jobs_wksht_required(person, spouse):
    # If you have more than one job at a time 
    # or are married filing jointly and you and your spouse both work, 
    # 
    # and the combined earnings from all jobs exceed $53,000 ($24,450 if married filing jointly), see the
    # Two-Earners/Multiple Jobs Worksheet on page 4 to avoid having too little tax withheld.  
    If(
        Or(two_earners_mult_jobs_wksht_required_single(person), two_earners_mult_jobs_wksht_required_couple(person, spouse)),
        True, False):


def two_earners_mult_jobs_wksht_required_single(person):
    If(And(count_of_jobs(person) > 1, total_income(person) > 53000), True, False)


def two_earners_mult_jobs_wksht_required_couple(person, spouse):
If(
    And(is_married(person), 
            filing_jointly(person, spouse), 
            couple_both_work(person, spouse),
            combined_couple_wages(person, spouse) > 24450), True, False)

    

def two_earners_mult_jobs_wksht_line_1(person):
    # Enter the number from the Personal Allowances Worksheet, line H, page 3 (or, if you used the
    # Deductions, Adjustments, and Additional Income Worksheet on page 3, the number from line 10 of that
    # worksheet)
    #tbd, logic to figure out which wksht has been completed
    If(plans_to_itemize_or_claim_adjustments(person), ded_adj_adtl_inc_line_10(person), personal_allowances_worksheet_line_h(person))

def two_earners_mult_jobs_wksht_line_2(person, spouse):
    # Find the number in Table 1 below that applies to the LOWEST paying job and enter it here. However, if you’re
    # married filing jointly and wages from the highest paying job are $75,000 or less and the combined wages for
    # you and your spouse are $107,000 or less, don’t enter more than “3” 
    If(
        # if then else?
        And(is_married(person), filing_jointly(person), highest_earning_job_from_couple(person, spouse) <= 75000, combined_couple_wages(person, spouse))):
        #assumes only one job, needs to be expanded
        return min(3, line_2_table_1_married_joint_lookup(min(persons_wages(person), persons_wages(spouse))))
    Elif(And(is_married(person), filing_jointly(person)):
        return two_earners_mult_jobs_wksht_table_1_married_joint_lookup(combined_couple_wages(person, spouse))
    Else:
        return two_earners_mult_jobs_wksht_table_1_all_others_lookup(persons_wages(person))

def two_earners_mult_jobs_wksht_line_3(person, spouse):

    # If line 1 is more than or equal to line 2, subtract line 2 from line 1. Enter the result here (if zero, enter “-0-”)
    # and on Form W-4, line 5, page 1. Do not use the rest of this worksheet
    If(two_earners_mult_jobs_wksht_line_1(person) >= two_earners_mult_jobs_wksht_line_2(person, spouse)):
        return two_earners_mult_jobs_wksht_line_2(person, spouse) - two_earners_mult_jobs_wksht_line_1(person)
    Else:
        return two_earners_mult_jobs_wksht_line_4(person)

def two_earners_mult_jobs_wksht_line_4(person, spouse):
    # Note: If line 1 is less than line 2, enter “-0-” on Form W-4, line 5, page 1. Complete lines 4 through 9 below to
    # figure the additional withholding amount necessary to avoid a year-end tax bill.
    # Enter the number from line 2 of this worksheet
    return two_earners_mult_jobs_wksht_line_2(person, spouse)

def two_earners_mult_jobs_wksht_line_5(person, spouse):
    # Enter the number from line 1 of this worksheet
    return two_earners_mult_jobs_wksht_line_1(person)

def two_earners_mult_jobs_wksht_line_6(person, spouse):
    # 6 Subtract line 5 from line 4 
    return two_earners_mult_jobs_wksht_line_4(person, spouse) - two_earners_mult_jobs_wksht_line_5(person, spouse)

def two_earners_mult_jobs_wksht_line_7(person, spouse):
    # Find the amount in Table 2 below that applies to the HIGHEST paying job and enter it here
    If(And(is_married(person), filing_jointly(person)):
        # assumes one job, needs to be expanded
        return two_earners_mult_jobs_wksht_table_2_married_joint_lookup(max(persons_wages(person), persons_wages(spouse)))
    Else:
        return two_earners_mult_jobs_wksht_table_2_all_others_lookup(persons_wages(person))
    


############### intermediates ###############
def spouse_unemployed(s):
    return employment_status(s) != "Employed"


def combined_couple_wages(person, spouse):
    # wages from person's first job, wages from spouse's job
    return If(is_single(person), wages_from_second_job(person), wages_from_second_job(person) + persons_wages(spouse))


def has_only_one_job(person):
    return count_of_jobs(person) == 1


# certainty < 1, is single single or is single/widowed single?
def is_single(p):
    return Or(marital_status(p) == "Single, unmarried, or legally separated",
              marital_status(p) == "Widowed (spouse died during the tax year)",
              marital_status(p) == "Widowed (spouse died before the tax year)")

def highest_earning_job_from_couple(person, spouse):
    #need temporal max function?
    return Max(highest_earning_job_wages(person), highest_earning_job_wages(spouse))



def two_earners_mult_jobs_wksht_table_2_married_joint_lookup(wages):
    If(wages <= 24900):
        return 420
    Elif(wages <= 84450):
        return 500
    Elif(wages <= 173900):
        return 910
    Elif(wages <= 326950):
        return 1000
    Elif(wages <= 413700):
        return 1330
    Elif(wages <= 617851):
        return 1450
    Else:
        return 1540

def two_earners_mult_jobs_wksht_table_2_all_others_lookup(wages):
    If(wages <= 7200):
        return 420
    Elif(wages <= 36975):
        return 500
    Elif(wages <= 81700):
        return 910
    Elif(wages <= 158225):
        return 1000
    Elif(wages <= 201600):
        return 1330
    Elif(wages <= 507800):
        return 1450
    Else:
        return 1540

def two_earners_mult_jobs_wksht_table_1_married_joint_lookup(wages):
    #need a clever way to implement
    If(wages <= 5000):
        return 0
    Elif(wages <= 9500):
        return 1
    Elif(wages <= 19500):
        return 2
    Elif(wages <= 35000):
        return 3
    Elif(wages <= 40000):
        return 4
    Elif(wages <= 46000):
        return 5
    Elif(wages <= 55000):
        return 6
    Elif(wages <= 60000):
        return 7
    Elif(wages <= 70000):
        return 8
    Elif(wages <= 75000):
        return 9
    Elif(wages <= 85000):
        return 10
    Elif(wages <= 95000):
        return 11
    Elif(wages <= 125000):
        return 12
    Elif(wages <= 155000):
        return 13
    Elif(wages <= 165000):
        return 14
    Elif(wages <= 175000):
        return 15
    Elif(wages <= 180000):
        return 16
    Elif(wages <= 195000):
        return 17
    Elif(wages <= 205000):
        return 18
    Else:
        return 19


def two_earners_mult_jobs_wksht_table_1_all_others_lookup(wages):
    #need a clever way to implement
    If(wages <= 7000):
        return 0
    Elif(wages <= 13000):
        return 1
    Elif(wages <= 27500):
        return 2
    Elif(wages <= 32000):
        return 3
    Elif(wages <= 40000):
        return 4
    Elif(wages <= 60000):
        return 5
    Elif(wages <= 75000):
        return 6
    Elif(wages <= 85000):
        return 7
    Elif(wages <= 95000):
        return 8
    Elif(wages <= 100000):
        return 9
    Elif(wages <= 110000):
        return 10
    Elif(wages <= 115000):
        return 11
    Elif(wages <= 125000):
        return 12
    Elif(wages <= 135000):
        return 13
    Elif(wages <= 145000):
        return 14
    Elif(wages <= 160000):
        return 15
    Elif(wages <= 180000):
        return 16
    Else:
        return 17




############### base input rules ###############
# base level attributes? Can we make these "fall out"?
def is_married(person, spouse):
    return marital_status(person) == "Married"


def marital_status(p):
    return(In("str", "marital_status", p, None, "What is {0}'s marital status?"))


def tax_status(p):
    return In("str", "tax_status", p, None, "How does {0} plan to file taxes?")


def head_of_household(p):
    return(In("bool", "head_of_household", p, None, "Is {0} the head of their household?"))

# converting boolean to integer for summing, is there a better pattern to employ?


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


def has_other_credits(p):
    return In("bool", "has_other_credits_pub505", p, None, "Does {0} have other credits from Worksheet 1-6 of Pub. 505?")


def other_credits_pub505(p):
    return In("num", "other_credits_pub505", p, None, "How many other credits does {0} have from Worksheet 1-6 of Pub. 505?")

# temporal?
def itemized_deductions_2019(p):
    return In("num", "itemized_deductions_2019", p, None, "Please enter the an estimate of {0}'s 2019 itemized deductions. "
              + "These include qualifying home mortgage interest, "
              + "charitable contributions, state and local taxes (up to $10,000), and medical expenses in excess of 10% of "
              + "your income. See Pub. 505 for details")


def estimate_2019_adj_to_inc_qual_bus_inc_ded_addtl_std_ded(p):
    return In("num", "itemized_deductions_2019", p, None, "Enter an estimate of {0}'s 2019 adjustments to income, "
              + "qualified business income deduction, and any additional standard deduction for age or blindness "
              + "(see Pub. 505 for information about these items) . . ")


def estimate_2019_nonwage_inc_not_subj_to_withholding(p):
    return In("num", "itemized_deductions_2019", p, None, "Enter an estimate of {0}'s 2019 nonwage income not subject to withholding (such as dividends or interest)")

def highest_earning_job_wages(p):
    return In("num", "highest_earning_job_total_wages", p, None, "Enter the wages from {0}'s highest earning job.")

def plans_to_itemize_or_claim_adjustments(p):
    return In("bool", "plans_to_itemize_or_claim_adjustments", p, None, "Does {0} plan  to itemize or claim adjustments to income and want to reduce " 
        + "their withholding, or if do they have a large amount of nonwage income not subject to withholding and want to increase their withholding.")

def couple_both_work(p, s):
    return In("bool", "couple_both_work", p, s, "Do {0} and {1} both work?")