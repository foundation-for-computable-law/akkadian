from dsl.timeseries import *


# COMPARISON

# Internal, static >= function
# Output: Value
def internal_ge(a: Value, b: Value):
    return internal_process_binary(operator.ge, a, b)


# Internal, static > function
# Output: Value
def internal_gt(a: Value, b: Value):
    return internal_process_binary(operator.gt, a, b)


# Internal, static <= function
# Output: Value
def internal_le(a: Value, b: Value):
    return internal_process_binary(operator.le, a, b)


# Internal, static < function
# Output: Value
def internal_lt(a: Value, b: Value):
    return internal_process_binary(operator.lt, a, b)


# Internal, static == function
# Output: Value
def internal_eq(a: Value, b: Value):
    return internal_process_binary(operator.eq, a, b)


# Internal, static != function
# Output: Value
def internal_ne(a: Value, b: Value):
    return internal_process_binary(operator.ne, a, b)


# ARITHMETIC


# Internal, static + function
# Output: Value
def internal_add(a: Value, b: Value):
    return internal_process_binary(operator.add, a, b)


# Internal, static * function
# Output: Value
def internal_mul(a: Value, b: Value):
    return internal_process_binary(operator.mul, a, b)


# Internal, static - function
# Output: Value
def internal_sub(a: Value, b: Value):
    return internal_process_binary(operator.sub, a, b)


# Internal, static / function
# Output: Value
def internal_div(a: Value, b: Value):
    return internal_process_binary(operator.truediv, a, b)
