from akkadian.date import *
from akkadian.facts import *
from akkadian.temporal import *


# INVESTIGATE


# Generates an interactive interview in a Python console to collect info to resolve a goal
def Investigate(goals: list, fs=[]):

    traversal_list.clear()

    # Call the "apply rules" interface
    re = ApplyRules(goals, fs)

    # If all of the goals have been determined, present the results
    if re["complete"]:
        # print(re["msg"])
        print("\n")
        print(proof_tree_str(traversal_list))

    # Otherwise, ask the next question...
    else:
        # Find out what the next question is
        nxt = re["missing_info"][0]

        # Ask it
        new = input(nxt[4])

        # Add the newly acquired fact to the fact list
        fs.append(Fact(nxt[1], nxt[2], nxt[3], convert_input(nxt[0], new)))

        # Go to step 1
        Investigate(goals, fs)


# Convert inputs from the terminal to the desired type
# Assumes dates are entered as yyyy-mm-dd
def convert_input(typ: str, val: str):
    if val in ("Stub", "stub"):
        return Stub
    elif typ == "num":
        return float(val)
    elif typ == "date":
        return val
    elif typ == "str":
        return val
    elif typ == "bool":
        if val in ("true", "True", "V", "t", "yes", "y"):
            return True
        else:
            return False
    else:
        return val


# APPLY_RULES


# Applies substantive rules to a fact pattern
# Returns a determination or a list of needed information
# Each goal is entered as a tuple containing the function name and arguments
# For example: (is_eligible, "Bertie") or (is_qualifying_relative, "Jim", "Lucy")
def ApplyRules(goals: list, fs=[]):

    # Clear and reload data structures
    missing_info.clear()
    facts.clear()
    for item in fs:
        facts.append(item)

    # Evaluate goals (causing missing_info to be reloaded)
    # results = list(map(eval, goals))
    results = list(map(execute_fcn, goals))

    # Estimate interview progress
    progress = len(facts) / max(len(facts) + len(missing_info), 1)

    # Have all of the goals been determined?
    complete = all(map(lambda x: goal_is_determined(x), results))

    # For each result, format it as a dictionary
    # TODO: In each dictionary, include the function name that was being called
    result_blocks = list(map(lambda x: process_results(x), results))

    # Housekeeping
    facts.clear()

    # Mic drop
    return {
        "complete": complete,
        "progress": 1.0 if complete else round(progress, 2),
        "msg": Pretty(results[0]),  # TODO: Generalize to multiple goals
        "results": result_blocks,
        "missing_info": [] if complete else missing_info
    }


# Execute the function, given a list of its name and arguments
def execute_fcn(i):
    if len(i) == 3:
        return i[0](i[1], i[2])
    else:
        return i[0](i[1])


# Determines whether a goal has been determined such that the interview can stop
def goal_is_determined(goal: TimeSeries):
    return not any([x.value == "Null" for x in goal.dict.values()])


# IN


# Gets the value for a fact
def In(typ: str, name: str, subj, obj, question=None, options=None, help=None):

    # See if the desired fact is in the "facts" data structure
    lookup = list(filter(lambda x: x.name == name and x.subject == subj and x.object == obj, facts))

    # If not, add it
    if lookup == []:

        # Prevent duplicates from being added
        if list(filter(lambda x: x[1] == name and x[2] == subj and x[3] == obj, missing_info)) == []:
            missing_info.append([typ, name, subj, obj, text_subst(subj, obj, question), options, help])

        # Indicate lack of knowledge
        return Eternal(Null)

    # If the fact is known, return its value
    else:
        result = Eternal(lookup[0].value)
        if subj is None and obj is None:
            f = name + "()"
        elif obj is None:
            f = name + "(" + subj + ")"
        else:
            f = name + "(" + subj + ", " + obj + ")"
        traversal_list.append([1, f])
        traversal_list.append([-1, f, result])
        return result


# Substitute the subject ({0}) and object ({1}) of a fact into the question text
def text_subst(sbj: str, obj: str, question: str):
    if obj is None:
        return question.format(sbj) + " "
    else:
        return question.format(sbj, obj) + " "


# Format results into a dictionary
def process_results(result: TimeSeries):
    return {
        # "result": result.value,
        # "certainty": result.cf,
        "msg": Pretty(result),
        "complete": result is not Null
    }


# PROOF TREES


# Holds the node traversal list
traversal_list = []


# Given a tuple containing (name, *args), create a string e.g. "f(jim)"
def fcn_tuple_to_str(tup):
    return str(tup[0]) + str(tup[1:]).replace(",)", ")").replace("'", "")


# A decorator that builds a data structure of the traversal of the function graph during rule execution
def explain(func):
    def wrapper(*args):
        f = fcn_tuple_to_str((func.__name__, *args))
        traversal_list.append([1, f])
        result = func(*args)
        traversal_list.append([-1, f, result])
        return result
    return wrapper


# Given a function name and the list of traversed nodes, this function looks up the value of the named function
def get_fcn_value_from_traversal_list(f_name, t_list):
    for i in t_list:
        if i[0] == -1 and i[1] == f_name:
            return i[2]


# Cleans up the traversal list, returning a new list in which each element has the form
# e.g. [1, f(a,b), 6]
def traverse_list_clean(traverse_list):
    result = []
    lev = -1

    for i in traverse_list:

        # Increment/decrement indentation level based on traversal data
        lev += i[0]

        if i[0] == 1:
            # Indicate level by indentation
            spc = " " * lev * 2
            val = get_fcn_value_from_traversal_list(i[1], traverse_list)

            # Print the function name and its value, with the appropriate indentation
            result.append([lev, i[1], val])

    return result


# Create an adjacency list of function calls, from a traversal list
# Items in the resulting list are of the form: [1, 'f(1, 6)', 'g(1)', '6.35']
def proof_tree_data(t_list):
    t_clean = traverse_list_clean(t_list)
    first = t_clean[0]
    parents = [first[1]]
    last_lev = 0
    results = [[first[0], -1, first[1], first[2]]]

    for i in t_clean[1:]:

        lev = i[0]

        # Going back up the tree
        if lev < last_lev:
            for m in range(last_lev-lev):
                parents.pop()

        # Going down the tree
        elif lev > last_lev:
            parents.append(i[1])

        results.append([lev, parents[-2], i[1], i[2]])

        last_lev = lev

    # Remove duplicates
    deduped = []
    for i in results:
        if i not in deduped:
            deduped.append(i)

    return deduped


# Generates a proof tree, or explanation for a conclusion, from a list of the functions traversed during
# rule execution
def proof_tree_str(t_list):

    adj_list = proof_tree_data(t_list)

    result = ""

    for i in adj_list:

        # Indicate level by indentation
        spc = " " * i[0] * 2

        # Print the function name and its value, with the appropriate indentation
        result += spc + i[2] + " = " + str(ToScalar(AsOf(Now, i[3]))) + "\n"

    return result
