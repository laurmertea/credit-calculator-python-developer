# Description
# Finally, let's add to our calculator the capacity to compute the differentiated payment. 
# In such a kind of payment where the part for reducing the credit principal is constant. 
# Another part of the payment is for interest repayment and it reduces during the credit term. 
# It means that the payment is different each month. Let’s look at the formula:
# D(m) = P / n + i * (P - P * (m - 1) / n)
# 
# Where:
# D(m) = mth differentiated payment;
#
# P = the credit principal;
#
# i = nominal interest rate. 
# Usually, it’s 1/12 of the annual interest rate. 
# And usually, it’s a floating value, not a percentage. 
# For example, if we our annual interest rate = 12%, then i = 0.01.
# 
# n = Number of payments. 
# Usually, it’s the count of months.
# 
# m = current period.
#
# As you can see, the user has to input a lot of parameters. 
# So it might be convenient to use command-line arguments.
# Suppose you used to run your credit calculator via command line like this: `python credit_calc.py`
# Using command-line arguments you can run your program this way: 
# `python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10`
# In that case, your program can get different values and not ask the user to input them. 
# It can be useful when you are developing your program and trying to find a mistake 
# and want to run the program with the same parameters again and again. 
# Also, it's convenient if you made a mistake in a single parameter. 
# You don't have to input all other values again.
#
# Objectives
# At this stage, it is required to implement these features:
# - the calculation of differentiated payment. 
# To do this, the user may run the program specifying interest, count of periods and credit principal.
# - a capacity to calculate the same values as in the previous stage for annuity payment 
# (principal, count of periods and value of the payment). 
# A user specifies all known parameters with command-line arguments, 
# while a single parameter will be unknown. This is the value the user wants to calculate.
# - handling of invalid parameters. 
# It's a good idea to show an error message Incorrect parameters in case of invalid parameters 
# (they are discussed in detail below).
# 
# The final version of your program is supposed to work from the command line and parse the following parameters:
# `--type`, which indicates the type of payments: "annuity" or "diff" (differentiated). 
# If `--type` is specified neither as "annuity" nor as "diff", or it is not specified at all, show the error message.
# > python credit_calc.py --principal=1000000 --periods=60 --interest=10
# `Incorrect parameters`
# `--payment`, that is a monthly payment. 
# For --type=diff the payment is different each month, so we can't calculate periods or principal, 
# therefore, its combination with `--payment` is invalid, too:
# > python credit_calc.py --type=diff --principal=1000000 --interest=10 --payment=100000
# `Incorrect parameters`
# `--principal` is used for calculations of both types of payment. 
# You can get its value knowing the interest, annuity payment and periods.
# `--periods` parameter denotes the number of months and/or years needed to repay the credit. 
# It's calculated based on the interest, annuity payment and principal.
# `--interest` is specified without a percent sign. 
# Note that it may accept a floating-point value. Our credit calculator can't calculate the interest, 
# so these parameters are incorrect:
# > python credit_calc.py --type=annuity --principal=100000 --payment=10400 --periods=8
# `Incorrect parameters`
# Let's make a comment. You might have noticed that for differentiated payments 
# you will need 4 out of 5 parameters (excluding payment), 
# and the same is true for annuity payments (missing either periods, payment or principal). 
# Thus, when less than four parameters are given, you should display the error message too:
# > python credit_calc.py --type=annuity --principal=1000000 --payment=104000
# `Incorrect parameters`
# Another case when you should output this message is negative values. We can't work with these!
# > python credit_calc.py --type=diff --principal=30000 --periods=-14 --interest=10
# `Incorrect parameters`
# Finally, don't forget to compute the value of overpayment, 
# and you'll have your real credit calculator!
#
# Examples
# Let’s look at the first example. The greater-than symbol followed by space (> ) represents the user input.
# 
# Example 1: calculate differentiated payments
# > python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10
#
# Month 1: paid out 108334
# Month 2: paid out 107500
# Month 3: paid out 106667
# Month 4: paid out 105834
# Month 5: paid out 105000
# Month 6: paid out 104167
# Month 7: paid out 103334
# Month 8: paid out 102500
# Month 9: paid out 101667
# Month 10: paid out 100834
#
# Overpayment = 45837
# In this example, the user wants to take a credit with differentiated payments. 
# You know the principal, the count of periods and interest, 
# which are 1,000,000, 10 months and 10% respectively.
# Your credit calculator should output monthly payments for every month like at the first stage. 
# Also, round up all floating-point values.
# Finally, your credit calculator should add up all the payments 
# and subtract the credit principal so that you'll get the overpayment.
# 
# Example 2: find an annuity payment for the 60-month (or 5-year) credit with the principal 1,000,000 and 10% interest
# > python credit_calc.py --type=annuity --principal=1000000 --periods=60 --interest=10
# Your annuity payment = 21248!
# Overpayment = 274880
# 
# Example 3: less than four arguments are given
# > python credit_calc.py --type=diff --principal=1000000 --payment=104000
# `Incorrect parameters.`
# 
# Example 4: calculate differentiated payments given the principal 500,000, the period of 8 months and the interest rate 7.8%
# > python credit_calc.py --type=diff --principal=500000 --periods=8 --interest=7.8
# Month 1: paid out 65750
# Month 2: paid out 65344
# Month 3: paid out 64938
# Month 4: paid out 64532
# Month 5: paid out 64125
# Month 6: paid out 63719
# Month 7: paid out 63313
# Month 8: paid out 62907
# Overpayment = 14628
#
# Example 5: calculate the principal for a user paying 8,722 per month for 120 months (10 years) with the interest 5.6%
# > python credit_calc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Your credit principal = 800018!
# Overpayment = 246622
# 
# Example 6: figure out how much time a user needs to repay the credit with 500,000 principal, 23,000 monthly payment and 7.8% interest
# > python credit_calc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
# You need 2 years to repay this credit!
# Overpayment = 52000

import argparse
import sys
import math

min_args = 5
required_arg = 'interest'
allowed_types = ['annuity', 'diff']
allowed_types_msg = ", " . join(allowed_types)

def arguments():
    parser.add_argument("-t", "--type", help=f"the type of payments: {allowed_types_msg}")
    parser.add_argument("-p", "--payment", help=f"the monthly payment; this can't be used as an argument for the differentiated type")
    parser.add_argument("-prc", "--principal", help=f"the principal is used for calculations of both types of payment; you can get its value knowing the interest, annuity payment and periods.")
    parser.add_argument("-per", "--periods", help=f"the number of months and/or years needed to repay the credit; it's calculated based on the interest")
    parser.add_argument("-i", "--interest", help=f"floating-point value specified without the percent sign")

def exit():
    sys.exit("Incorrect parameters")

def has_type():
    return 'type' in args

def allowed(val, allowed):
    return val in allowed

def check_cmd_args_len():
    return min_args == len(arg_vals)

def missing(required_arg):
    arg_value = getattr(args, required_arg)
    return arg_value == None

def incorrect_combination():
    if args.type == 'diff' and args.payment != None:
        return True
    if args.type == 'annuity' and args.principal != None and args.payment != None and args.periods != None:
        return True
    return False

def negative_args():
    for arg in vars(args): 
        if arg != 'type' and getattr(args, arg) != None:
            if float(getattr(args, arg)) < 0:
                return True
    return False

def check_cmd_args():
    if not has_type():
        exit()
    else:
        if not allowed(args.type, allowed_types):
            exit()
        if not check_cmd_args_len():
            exit()
        else:
            if missing(required_arg):
                exit()
            if incorrect_combination():
                exit()
            if negative_args():
                exit()
            return True 

def nominal_interest_rate(interest):
    return interest / 100 / 12

def monthly_payment(nir, month):
    principal = int(args.principal)
    periods = int(args.periods)
    return math.ceil(principal / periods + nir * (principal - (principal * (month - 1)) / periods))

def diff():
    nir = nominal_interest_rate(float(args.interest))
    paid_sum = 0 
    for month in range(1, int(args.periods) + 1):
        current_payment = monthly_payment(nir, int(month))
        paid_sum += current_payment
        print(f"Month {month}: paid out {current_payment}")
    overpayment = paid_sum - int(args.principal)
    print(f"Overpayment = {overpayment}")

def payment():
    nir = nominal_interest_rate(float(args.interest))
    periods = int(args.periods)
    principal = int(args.principal)
    return math.ceil(principal * nir * (1 + nir) ** periods / ((1 + nir) ** periods -1))

def principal():
    nir = nominal_interest_rate(float(args.interest))
    return math.floor(int(args.payment) / ((nir * (1 + nir) ** int(args.periods)) / (((1 + nir) ** int(args.periods)) - 1)))

def periods_count():
    nir = nominal_interest_rate(float(args.interest))
    payment = int(args.payment)
    return math.ceil(math.log(payment / (payment - nir * int(args.principal)), 1 + nir))

def months_count():
    result = ''
    raw = periods_count()

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
    
    return result

def paid(annuity_payment, periods):
    return annuity_payment * periods

def overpaid(annuity_payment, credit_principal, periods):
    return paid(annuity_payment, periods) - credit_principal

def annuity():
    if args.payment == None:
        annuity_payment = payment()
        print(f'Your annuity payment = {annuity_payment}!')
    else:
        annuity_payment = int(args.payment)
    
    if args.principal == None:
        credit_principal = principal()
        print(f'Your credit principal = {credit_principal}!')
    else:
        credit_principal = int(args.principal)

    if args.periods == None:
        time_interval = months_count()
        periods = periods_count()
        print(f'You need {time_interval} to repay this credit!')
    else:
        periods = int(args.periods)
    
    overpayment = overpaid(annuity_payment, credit_principal, periods)
    print(f"Overpayment = {overpayment}")

arg_vals = sys.argv
parser = argparse.ArgumentParser(description="""
    calculates different parts (credit principal, annuity payment, period of time) for an annuity credit
    OR the monthly payment values for a differentiated payments credit
    AND the overpayment value for both credit types
""")
arguments()
args = parser.parse_args()

if check_cmd_args():
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(args.type)
    if not method:
        raise NotImplementedError(f"Method {args.type} is not implemented")
    method()