import datetime
def days_in_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif (month == 2):
        if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
            return 29
        else:
            return 28
    else:
        return 30


def is_valid_date(year, month, day):
    if 0 < year <= datetime.MAXYEAR:
        if 12 >= month >= 1:
            if days_in_month(year, month) >= day > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    if ((is_valid_date(year1, month1, day1) == 0) or (is_valid_date(year2, month2, day2) == 0)):
        return 0
    elif (
            year2 <= year1 and month2 <= month1 and day2 <= day1) or year2 < year1 or year1 <= 0 or month1 <= 0 or day1 <= 0 or year2 <= 0 or month2 <= 0 or day2 <= 0:
        return 0
    else:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        return (date2 - date1).days

def age_in_days(year, month, day):
    if is_valid_date(year, month, day) == 0:
        return 0

    elif (year >= datetime.date.today().year and month >= datetime.date.today().month and day >= datetime.date.today().day) or year > datetime.date.today().year or year <= 0 or month <= 0 or day <= 0:
        return 0
    else:
        date1 = datetime.date(year, month, day)
        date2 = datetime.date.today()
        return (date2 - date1).days