from dsl.T import *


# TODO: Refactor and simplify these functions


# Like Python's map function but which handles T objects
# as well as None and Stub values
# TODO: Implement CFs
def Map(f, a):
    if is_stub(a) or is_none(a):
        return a
    elif type(a) is list and list_contains_none(a):
        return T(None)
    elif type(a) is T and list_contains_none(a.value):
        return T(None)
    else:
        return T(list(map(f, get_val(a))))


# Returns true if any element is T(True) or True
def Any(a):
    if is_stub(a) or is_none(a):
        return a
    elif type(a) is T and list_any_true(a.value):
        return T(True)
    elif type(a) is not T and list_any_true(a):
        return T(True)
    elif type(a) is list and list_contains_stub(a):
        return Stub()
    elif type(a) is T and list_contains_stub(a.value):
        return Stub()
    elif type(a) is list and list_contains_none(a):
        return T(None)
    elif type(a) is T and list_contains_none(a.value):
        return T(None)
    elif type(a) is T:
        return T(list_any_true(a.value))
    else:
        return T(list_any_true(a))


# Returns true if all elements are T(True) or True
def All(a):
    if is_stub(a) or is_none(a):
        return a
    elif type(a) is T and list_any_false(a.value):
        return T(False)
    elif type(a) is not T and list_any_false(a):
        return T(False)
    elif type(a) is list and list_contains_stub(a):
        return Stub()
    elif type(a) is T and list_contains_stub(a.value):
        return Stub()
    elif type(a) is list and list_contains_none(a):
        return T(None)
    elif type(a) is T and list_contains_none(a.value):
        return T(None)
    elif type(a) is T:
        return T(list_all_true(a.value))
    else:
        return T(list_all_true(a))


def Exists(f, a):
    return Any(Map(f, a))


def ForAll(f, a):
    return All(Map(f, a))


# SUPPORTING FUNCTIONS


# Does a list contain T(None)?
def list_contains_none(a: list):
    for x in a:
        if is_none(x):
            return True
    return False


# Does a list contain Stub()?
def list_contains_stub(a: list):
    for x in a:
        if is_stub(x):
            return True
    return False


# Does a list contain T(None)?
def list_any_true(a: list):
    for x in a:
        if get_val(x) is True:
            return True
    return False


# Does a list contain T(False)?
def list_any_false(a: list):
    for x in a:
        if get_val(x) is False:
            return True
    return False


# Does a list contain only T(None)'s?
def list_all_true(a: list):
    for x in a:
        if get_val(x) is not True:
            return False
    return True
