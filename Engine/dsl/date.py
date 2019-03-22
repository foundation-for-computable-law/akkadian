from datetime import date


# A convenience function to make date construction less verbose
# TODO: Handle uncertainty and T values
def Date(y: int, m: int, d: int):
    return date(y, m, d)


# Returns the current date
Now = date.today()