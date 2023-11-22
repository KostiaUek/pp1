from calendar import month_name


def month(n):
    if 1 < n < 12:
        return month_name[n]
    else:
        return "Wrong month number"
