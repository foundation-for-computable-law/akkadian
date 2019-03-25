from datetime import date


# A convenience function to make date construction less verbose
# TODO: Handle uncertainty and T values
def Date(y: int, m: int, d: int):
    return str(y) + "-" + str(m).zfill(2) + "-" + str(d).zfill(2)


# Returns the current date
Now = date.today().isoformat()
