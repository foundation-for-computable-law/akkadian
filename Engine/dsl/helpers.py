import datetime


# DATE, STRING, AND ORDINAL CONVERSIONS

def ordinal_to_date(n):
    return datetime.datetime.fromordinal(n)


def date_to_ordinal(dt):
    return datetime.datetime.toordinal(dt)


def date_to_str(dt):
    return dt.date().isoformat()


def str_to_date(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d").date()


def str_date_to_ordinal(s):
    return date_to_ordinal(str_to_date(s))


def ordinal_to_str_date(n):
    return date_to_str(ordinal_to_date(n))