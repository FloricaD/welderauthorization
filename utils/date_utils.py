def read_date(text):
  """
    read from user's input a date in the specified format

    Arguments:
      text: str -- the text to show the user
    Return:
      result: tuple -- a tuple containing the day, month, year as int
  """
  expiration_date = input(f"{text} (format: day/month/year) :")
  day, month, year = expiration_date.split("/")
  return int(day), int(month), int(year)

def date_difference(today_date, expiration_date):
  today_day, today_month, today_year  = today_date
  exp_day, exp_month, exp_year = expiration_date
  if exp_year > today_year: # exp_year 2025 today_year 2024
    if exp_year - today_year > 2:
      return False
    if exp_year - today_year == 1:
      return ((12 - today_year) + exp_month) <=3
  elif exp_year < today_year:
    # the authorization already expired
    return False
  else: # exp_year == today_year
    return (exp_month - today_month) <= 3