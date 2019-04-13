from akkadian.temporal import *


# A convenience function to make date construction less verbose
# TODO: Handle uncertainty and V values
def Date(y: int, m: int, d: int):
    return str(y) + "-" + str(m).zfill(2) + "-" + str(d).zfill(2)


# Returns the current date
Now = Eternal(date.today().isoformat())
