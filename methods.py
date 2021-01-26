from datetime import date, timedelta, datetime
import re, calendar

def is_valid_card_number(sequence):
    """Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6 
    - must only consist of digits (0-9) or hyphens '-',
    - may have digits in groups of 4, separated by one hyphen "-". 
    - must NOT use any other separator like ' ' , '_',
    - must NOT have 4 or more consecutive repeated digits.

    """

    PATTERN='^([3456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
    match = re.match(PATTERN,sequence)
    isValid = True
    if match == None:
        isValid = False
    else:
        for group in match.groups():
            if group[0] * 4 == group:
                isValid = False
    print("Valid Credit Card", isValid)
    return isValid

def is_valid_expiry_date(given_date):
    '''
        Expected Date Format YYYY-MM
        Validates the date and return True or False
        If the date format is invalid or the date is of past than current returns False
        If the date is valid and is of future date then returns true.
    '''

    try:
        # print(given_date)
        given_date = datetime.strptime(given_date, '%Y-%m')
        given_date.replace(day=calendar.monthrange(given_date.year, given_date.month)[1])
    except:
        isValid = False
    else:
        days_diff = given_date.date() - datetime.now().date() 
        isValid = days_diff.days > 0
    print("Valid expiry date", isValid)
    return isValid

def is_valid_security_code(code):
    '''
        Expected security code is 3 digits
        Validates the security code and return True or False based on it
    '''

    isValid = isinstance(code, str) and len(code) == 3
    print("Valid Security Code", isValid)
    return isValid

def is_valid_amount(amt):
    '''
        Expected amount is to be float / int value and non-negative / non-zero.
        Validates the given amount value and return True or False based on it
    '''    
    try:
        amt = float(amt)
    except:
        isValid = False
    else:
        isValid =  amt > 0
    print("Valid Amount", isValid)
    return isValid

def is_valid_card_holder_name(CardHolder):
    '''
        Expected card holder name to be of String type only and does not contain numbers or special characters.
        Validates the given card holder name and return True or False based on it
    '''    

    if isinstance(CardHolder, str) and CardHolder.replace(' ','').isalpha():
        isValid = True
    else:
        isValid = False
    print("Valid Card holder name", isValid)
    return isValid