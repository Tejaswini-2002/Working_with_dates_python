# Working_with_dates_python



I wrote a function called days_in_month that takes two integers: a year and a month. The function will return the number of days in that month.  I assumed that both inputs are valid (in other words, I assumed that the month input is a number between 1 and 12 and the year input is a number between datetime.MINYEAR and datetime.MAXYEAR).


I wrote a function called is_valid_date that takes three integers: a year, a month, and a day. The function will return True if that date is valid and False otherwise. This function will not assume that the inputs are valid. Rather, this function will check that all three inputs combine to form a valid date, with a year between datetime.MINYEAR and datetime.MAXYEAR, a month between 1 and 12, and a day between 1 and the number of days in the given month.


I wrote a function called days_between that takes six integers (year1, month1, day1, year2, month2, day2) and returns the number of days from an earlier date (year1-month1-day1) to a later date (year2-month2-day2). If either date is invalid, the function will return 0. I already wrote a function to determine if a date is valid or not. If the second date is earlier than the first date, the function will also return 0.


I wrote a function called age_in_days that takes three integers as input: the year, month, and day of a persons birthday. The function will return that person's age in days as of today. The function will return 0 if the input date is invalid. The function will also return 0 if the input date is in the future.
