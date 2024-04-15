from datetime import date
from pyscript import document


def validate_day(month):
    if month == 0:
        error_change("day", True)

    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    day = document.querySelector("#day").value

    try:
        day = int(day)
    except ValueError:
        error_change("day", True)
        return (0, True)
    if day < 1 or day > days_in_month[month]:
        error_change("day", True)
        return (0, True)

    return (day, False)


def validate_month():
    month = document.querySelector("#month").value
    try:
        month = int(month)
    except ValueError:
        error_change("month", True)
        return (0, True)
    if month < 1 or month > 12:
        error_change("month", True)
        return (0, True)

    return (month, False)


def validate_year():
    year = document.querySelector("#year").value

    try:
        year = int(year)
    except ValueError:
        error_change("year", True)
        return (0, True)
    if year > date.today().year:
        error_change("year", True)
        return (0, True)

    return (year, False)


def validate_date(month, day, year):
    try:
        input_date = date(year, month, day)
    except ValueError:
        error_change("year", True)
        return (0, True)

    if input_date > date.today():
        error_change("year", True)
        return (0, True)
    return (input_date, False)


def error_change(id: str, error: bool):
    if id == "day":
        if error:
            document.querySelector("#day-label").classList.add("error-labels")
            document.querySelector("#day").className = "input-field-error"
            document.querySelector("#error-day").style.visibility = "visible"
        else:
            document.querySelector("#day-label").classList.remove("error-labels")
            document.querySelector("#day").className = "input-field"
            document.querySelector("#error-day").style.visibility = "hidden"

    if id == "month":
        if error:
            document.querySelector("#month-label").classList.add("error-labels")
            document.querySelector("#month").className = "input-field-error"
            document.querySelector("#error-month").style.visibility = "visible"
        else:
            document.querySelector("#month-label").classList.remove("error-labels")
            document.querySelector("#month").className = "input-field"
            document.querySelector("#error-month").style.visibility = "hidden"

    if id == "year":
        if error:
            document.querySelector("#year-label").classList.add("error-labels")
            document.querySelector("#year").className = "input-field-error"
            document.querySelector("#error-year").style.visibility = "visible"
        else:
            document.querySelector("#year-label").classList.remove("error-labels")
            document.querySelector("#year").className = "input-field"
            document.querySelector("#error-year").style.visibility = "hidden"
