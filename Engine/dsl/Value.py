import operator


class Value:
    def __init__(self, value, cf=1, stub=False, null=False, units=None):

        # Substantive content of the object
        self.value = value

        # Certainty factor
        self.cf = cf

        # Units of measure
        self.units = units

        # Stub indicator
        self.is_stub = stub

        # Null indicator
        self.is_null = null

    def pretty(self):
        return str(self.value) + " (" + str(round(self.cf * 100)) + "% certain)"


# Indicates whether two Values are equivalent for purposes of trimming a TimeSeries
def values_are_equivalent(v1: Value, v2: Value):
    return v1.cf == v2.cf and \
           ((v1.is_stub and v2.is_stub) or (v1.is_null and v2.is_null) or (v1.value == v2.value))


# If item is a Value object, return it; otherwise convert it to a Value object
# Output: Value
def try_converting_to_val(a):
    if isinstance(a, Value):
        return a
    else:
        return Value(a)


# Value used to represent null (no value)
Null = Value("Null", null=True)

# Value used to represent a rule stub
Stub = Value("Stub", stub=True)


# Internal, static processing of most binary operators
def internal_process_binary(f, a_in: Value, b_in: Value):

    # Ensure that inputs are Value objects
    a = try_converting_to_val(a_in)
    b = try_converting_to_val(b_in)

    # Short-circuit for multiplication by 0
    if f is operator.mul and (a.value is 0 or b.value is 0):
        if a.value is 0 and b.value is 0:
            return Value(0, cf=max(a.cf, b.cf))
        elif a.value is 0:
            return a
        else:
            return b

    # Otherwise, compute the result, based on the object types
    elif a.is_stub and b.is_stub:
        return Value("Stub", cf=max(a.cf, b.cf), stub=True)
    elif a.is_stub:
        return a
    elif b.is_stub:
        return b
    elif a.is_null and b.is_null:
        return Value("Null", cf=max(a.cf, b.cf), null=True)
    elif a.is_null:
        return a
    elif b.is_null:
        return b
    else:
        return Value(f(a.value, b.value), cf=min(a.cf, b.cf))
