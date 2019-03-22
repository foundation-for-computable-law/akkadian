from datetime import date
from dsl.facts import *
from dsl.T import *


# Generates an interactive interview to collect info to resolve a goal
def Investigate(goals: list, fs=[]):

    # Call the "apply rules" interface
    re = Apply_rules(goals, fs)

    # If all of the goals have been determined, present the results
    if re["complete"]:
        print(re["msg"])  # TODO

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
        return Stub()
    elif typ == "num":
        return float(val)
    elif typ == "date":
        return date.fromisoformat(val)
    elif typ == "str":
        return val
    elif typ == "bool":
        if val in ("true", "True", "T", "t", "yes", "y"):
            return True
        else:
            return False
    else:
        return val


# Applies substantive rules to a fact pattern
# Returns a determination or a list of needed information
# Each goal is entered as a string, for example: "module.fcn('jim')"
def Apply_rules(goals: list, fs=[]):

    # Load namespaces
    for goal in goals:
        exec("import " + goal[0:goal.find('.')]) # Note: causes the imported module to be reevaluated

    # Clear and reload data structures
    missing_info.clear()
    facts.clear()
    for item in fs:
        facts.append(item)

    # Evaluate goals (causing missing_info to be reloaded)
    results = list(map(eval, goals))

    # Estimate interview progress
    progress = len(facts) / max(len(facts) + len(missing_info), 1)

    # Have all of the goals been determined?
    complete = all(map(lambda x : x.value is not None, results))

    # For each result, format it as a dictionary
    # TODO: In each dictionary, include the function name that was being called
    result_blocks = list(map(lambda x : process_results(x), results))

    # Housekeeping
    facts.clear()

    # Mic drop
    return {
        "complete": complete,
        "progress": 1.0 if complete else round(progress, 2),
        "msg": results[0].pretty(),  # TODO: Generalize to multiple goals
        "results": result_blocks,
        "missing_info": [] if complete else missing_info
    }


# Gets the value for a fact
def In(typ: str, name: str, subj, obj, question=None):

    # See if the desired fact is in the "facts" data structure
    lookup = list(filter(lambda x: x.name == name and x.subject == subj and x.object == obj, facts))

    # If not, add it
    if lookup == []:

        # Prevent duplicates from being added
        if list(filter(lambda x: x[1] == name and x[2] == subj and x[3] == obj, missing_info)) == []:
            missing_info.append([typ, name, subj, obj, text_subst(subj, obj, question)])

        # Indicate lack of knowledge
        return T(None)

    # If the fact is known, return its value
    else:
        return T(lookup[0].value)


# Substitute the subject ({0}) and object ({1}) of a fact into the question text
def text_subst(sbj: str, obj: str, question: str):
    if obj is None:
        return question.format(sbj) + " "
    else:
        return question.format(sbj, obj) + " "


# Given a T object, format its values into a dictionary
def process_results(result : T):
    return {
        "result": result.value,
        "certainty": result.cf,
        "msg": result.pretty(),
        "complete": result.value is not None
    }