from datetime import date
from dateutil.relativedelta import relativedelta
from pyscript import document

from utils import (
    validate_date,
    validate_day,
    validate_month,
    validate_year,
    error_change,
)


def submit_button(event):

    # Validation
    month, month_error = validate_month()

    day, day_error = validate_day(month)

    year, year_error = validate_year()

    if month_error or day_error or year_error:
        return

    input_date, date_valid = validate_date(day=day, month=month, year=year)

    if date_valid:
        return

    now = date.today()

    age = relativedelta(now, input_date)

    years_diff = age.years
    months_diff = age.months
    days_diff = age.days

    document.querySelector("#output-day").innerText = days_diff
    document.querySelector("#output-month").innerText = months_diff
    document.querySelector("#output-year").innerText = years_diff


def click_day(event):
    error_change("day", False)


def click_month(event):
    error_change("month", False)


def click_year(event):
    error_change("year", False)
