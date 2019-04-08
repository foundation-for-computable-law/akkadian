#
#
#
# # TODO: Refactor and simplify these functions
#
#
# # Like Python's map function but which handles V objects
# # as well as None and Stub values
# # TODO: Implement CFs
# def Map(f, a):
#     if is_stub(a) or is_none(a):
#         return a
#     elif type(a) is list and list_contains_none(a):
#         return V(None)
#     elif type(a) is V and list_contains_none(a.value):
#         return V(None)
#     else:
#         return V(list(map(f, get_val(a))))
#
#
# # Returns true if any element is V(True) or True
# def Any(a):
#     if is_stub(a) or is_none(a):
#         return a
#     elif type(a) is V and list_any_true(a.value):
#         return V(True)
#     elif type(a) is not V and list_any_true(a):
#         return V(True)
#     elif type(a) is list and list_contains_stub(a):
#         return Stub()
#     elif type(a) is V and list_contains_stub(a.value):
#         return Stub()
#     elif type(a) is list and list_contains_none(a):
#         return V(None)
#     elif type(a) is V and list_contains_none(a.value):
#         return V(None)
#     elif type(a) is V:
#         return V(list_any_true(a.value))
#     else:
#         return V(list_any_true(a))
#
#
# # Returns true if all elements are V(True) or True
# def All(a):
#     if is_stub(a) or is_none(a):
#         return a
#     elif type(a) is V and list_any_false(a.value):
#         return V(False)
#     elif type(a) is not V and list_any_false(a):
#         return V(False)
#     elif type(a) is list and list_contains_stub(a):
#         return Stub()
#     elif type(a) is V and list_contains_stub(a.value):
#         return Stub()
#     elif type(a) is list and list_contains_none(a):
#         return V(None)
#     elif type(a) is V and list_contains_none(a.value):
#         return V(None)
#     elif type(a) is V:
#         return V(list_all_true(a.value))
#     else:
#         return V(list_all_true(a))
#
#
# def Exists(f, a):
#     return Any(Map(f, a))
#
#
# def ForAll(f, a):
#     return All(Map(f, a))
#
#
# # SUPPORTING FUNCTIONS
#
#
# # Does a list contain V(None)?
# def list_contains_none(a: list):
#     for x in a:
#         if is_none(x):
#             return True
#     return False
#
#
# # Does a list contain Stub()?
# def list_contains_stub(a: list):
#     for x in a:
#         if is_stub(x):
#             return True
#     return False
#
#
# # Does a list contain V(None)?
# def list_any_true(a: list):
#     for x in a:
#         if get_val(x) is True:
#             return True
#     return False
#
#
# # Does a list contain V(False)?
# def list_any_false(a: list):
#     for x in a:
#         if get_val(x) is False:
#             return True
#     return False
#
#
# # Does a list contain only V(None)'s?
# def list_all_true(a: list):
#     for x in a:
#         if get_val(x) is not True:
#             return False
#     return True
