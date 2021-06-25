import re

def validate_company_registration_number(company_registration_number):
    company_registration_number_form = re.compile('^([0-9]{10})$')
    return company_registration_number_form.match(company_registration_number)

def validate_investment_amount(investment_amount):
    investment_amount_form = re.compile('^([0-9])$')
    return investment_amount_form.match(investment_amount)