# Description
# Let's compute all the parameters of the credit. 
# There are at least two kinds of credit: 
# those with annuity payment and with differentiated payment. 
# At this stage, you're going to calculate only the annuity payment 
# which is fixed during the whole credit term.

# This is the formula:
# A[ordinary\_annuity] = P * (i * (1+i)^n)/((1+i)^n-1)
# where:
# A = ordinary_annuity

# P = credit principal 
 
# i = nominal (monthly) interest rate. 
# Usually, it’s 1/12 of the annual interest rate. 
# And usually, it’s a floating value, not a percentage. 
# For example, if you have annual interest rate = 12%, then i = 0.01.
 
# n = Number of payments. 
# Usually, it’s the count of months.

# You are interested in four values: 
# the count of periods to repay the credit, monthly payment, 
# credit principal and credit interest. 
# Each of these values can be calculated if others are known:

# Credit principal:
# P = A / ((i * (1 + i)^n) / (1 + i)^n - 1)

# A number of payments:
# n = log[i+1](A / A - i * P)

# Objectives
# At this stage, you should add new behavior to the calculator:
# First, you should ask the user which parameter they want to calculate. 
# The calculator should be able to calculate the count of periods, 
# monthly payment and credit principal.
# Then you need to ask them to input the remaining values.
# Finally, compute and output the value that they wanted.
# Note that users input interest rate as a percentage, 
# for example, 11.7, so you should divide this value by 100 to use in the formula above.
# Please be accurate when converting "X months" to "Y years and Z months". 
# Avoid writing "0 years and 11 months" (output "11 months" instead) 
# and "1 years and 0 months" (output "1 year" instead).
# Note that at this stage you have to ask the user 
# to input parameters in a determined order which is provided below. 
# Simply disregard the value the user wants to calculate from this order and follow it. 
# For example, it can be monthly payment if the user typed “a” 
# for the question “What do you want to calculate?”. 
# Here is the order:
# The first is the credit principal. 
# The second is a monthly payment. 
# The next is the count of the period.
# The last is the credit interest.

# Examples
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that it's not the part of the input.

# Example 1:
# What do you want to calculate? 
# type "n" - for count of months, 
# type "a" - for annuity monthly payment,
# type "p" - for credit principal: 
# > n
# Enter credit principal: 
# > 1000000
# Enter monthly payment: 
# > 15000
# Enter credit interest:
# > 10
# You need 8 years and 2 months to repay this credit!

# Let’s take a closer look at Example 1.
# You know the credit principal, the credit interest and want to calculate the count of months. 
# What shall you do?
# 1) You need to know the nominal interest rate. It is calculated like this:
# i = 10% / 12 * 100% = 0.008333...
# 2) Now you can calculate the count of periods:
# n = log[1 + 0.008333...] (15000 / (15000 - 0.008333... * 1000000)) = 97.71...
# 3) You need integer count of periods, so let’s round it up. 
# Notice that the user will pay a monthly payment for 97 months, 
# and for 98th month the user will pay 0.71... of the monthly payment. 
# So, there are 98 months to pay.
# n = 98
# 4) Finally, you need to convert “98 months” to “8 years and 2 months”, 
# so it is more readable and understandable for the user.

# Consider other examples:

# Example 2:
# What do you want to calculate? 
# type "n" - for count of months, 
# type "a" - for annuity monthly payment,
# type "p" - for credit principal: 
# > a
# Enter credit principal: 
# > 1000000
# Enter count of periods:
# > 60
# Enter credit interest:
# > 10
# Your annuity payment = 21248!

# Example 3:
# What do you want to calculate? 
# type "n" - for count of months, 
# type "a" - for annuity monthly payment,
# type "p" - for credit principal: 
# > p
# Enter monthly payment: 
# > 8721.8
# Enter count of periods:
# > 120
# Enter credit interest:
# > 5.6
# Your credit principal = 800000!

import math

def check_input():
    allowed = ["n", "a", "p"]

    parameter = input("""What do you want to calculate?
        type "n" - for count of months,
        type "a" - for annuity monthly payment, 
        type "p" - for credit principal: \n""")

    if parameter not in allowed :
        check_input()
    else:
        return parameter

def nominal_interest_rate(interest):
    return interest / 100 / 12

def periods_count(monthly_payment, interest, credit):
    nir = nominal_interest_rate(interest)
    return math.log(monthly_payment / (monthly_payment - nir * credit), 1 + nir)

def raw_months_count(monthly_payment, interest, credit):
    return math.ceil(periods_count(monthly_payment, interest, credit))

def months_count(monthly_payment, interest, credit):
    result = ''
    raw = raw_months_count(monthly_payment, interest, credit)

    if raw // 12 > 0:
        result += str(raw // 12) + ' year'
        if raw // 12 > 1:
            result += 's'

    if raw % 12 > 0:
        if result != '':
            result += ' and '
        result += str(raw % 12) + ' month'
        if raw % 12 > 1:
            result += 's'
    
    print(result)

def annuity_payment(periods_count, interest, credit):
    nir = nominal_interest_rate(interest)
    annuity_payment = math.ceil(credit * nir * (1 + nir) ** periods_count / ((1 + nir) ** periods_count -1))
    print(f'Your annuity payment = {annuity_payment}!')

def credit_principal(monthly_payment, periods_count, interest):
    nir = nominal_interest_rate(interest)
    credit_principal = round(monthly_payment / ((nir * (1 + nir) ** periods_count) / (((1 + nir) ** periods_count) - 1)))
    print(f'Your credit principal = {credit_principal}!')
    
parameter = check_input()

if parameter == "n":
    credit = int(input('Enter the credit principal: '))
    monthly_payment = float(input('Enter monthly payment: '))
    interest = float(input('Enter credit interest: '))
    months_count(monthly_payment, interest, credit)
elif parameter == "a":
    credit = int(input('Enter the credit principal: '))
    periods_count = int(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: '))
    annuity_payment(periods_count, interest, credit)
else:
    monthly_payment = float(input('Enter monthly payment: '))
    periods_count = int(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: '))
    credit_principal(monthly_payment, periods_count, interest)