# suve/core.py

def hello():
    return "Hello from suvepy!"

from datetime import datetime

def calculate_age(dob_str):
    # Parse the DOB string into a datetime object
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.today()
    
    # Calculate the difference in years, months, and days
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # Adjust for negative days or months
    if days < 0:
        months -= 1
        # Get the number of days in the previous month
        previous_month = (today.month - 1) if today.month > 1 else 12
        days += (dob.replace(year=today.year, month=previous_month, day=1) - dob.replace(year=today.year, month=previous_month - 1, day=1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days