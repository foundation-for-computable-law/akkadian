from dsl.Value import *


# COMPARISON

# Internal, static >= function
# Output: Value
def internal_ge(a: Value, b: Value):
    return process_binary_val(operator.ge, a, b)


# Internal, static > function
# Output: Value
def internal_gt(a: Value, b: Value):
    return process_binary_val(operator.gt, a, b)


# Internal, static <= function
# Output: Value
def internal_le(a: Value, b: Value):
    return process_binary_val(operator.le, a, b)


# Internal, static < function
# Output: Value
def internal_lt(a: Value, b: Value):
    return process_binary_val(operator.lt, a, b)


# Internal, static == function
# Output: Value
def internal_eq(a: Value, b: Value):
    return process_binary_val(operator.eq, a, b)


# Internal, static != function
# Output: Value
def internal_ne(a: Value, b: Value):
    return process_binary_val(operator.ne, a, b)


# ARITHMETIC


# Internal, static + function
# Output: Value
def internal_add(a: Value, b: Value):
    return process_binary_val(operator.add, a, b)


# Internal, static * function
# Output: Value
def internal_mul(a: Value, b: Value):
    return process_binary_val(operator.mul, a, b)


# Internal, static - function
# Output: Value
def internal_sub(a: Value, b: Value):
    return process_binary_val(operator.sub, a, b)


# Internal, static / function
# Output: Value
def internal_div(a: Value, b: Value):
    return process_binary_val(operator.truediv, a, b)
