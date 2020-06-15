import math

# Description
# If you found the previous stage too easy, let's add something interesting. 
# The best credits are probably those with a 0% interest: 
# such credits are called installments.
# Let's make some calculations for installments. 
# The user might know the count of periods and want to calculate the monthly payment. 
# Or, the user might know the value of the monthly payment 
# and wonder how many periods it would take to repay the installments. 
# At this stage, it is required to ask the user to input the credit principal. 
# Then, the user should tell what needs to be calculated 
# (the monthly payment or the count of periods) 
# and enter the necessary parameter. 
# After that, the credit calculator should output the value that the user wants.
# Also, let’s assume we don't care about the digits after the dot. 
# So if you get a floating-point expression as a result of the calculation, 
# you’ll have to do additional actions. 
# Take a look at Example 4. In that example, you need to calculate the monthly payment. 
# You know that the credit principal is 1000 and want to pay fit in 9 months. 
# The real value of payment can be calculated as:
# payment = principal / months = 1000 / 9 = 111.11111...
# Of course, you can’t pay that amount of money. 
# You have to round up this value and make it 112. 
# Remember that no payment can be more than a monthly payment. 
# If you make a monthly payment of 111, the last payment will be 112, 
# and if you make a monthly payment of 112, the last payment will be 104, 
# which is appropriate by the rules. You can calculate the last payment just by:
# lastpayment = principal − (periods−1) ∗ payment = 1000−8∗112 = 104
# At this stage, you need to count the number of months or the monthly payment. 
# If the last payment differs from the rest, 
# the program should display the monthly payment and the last payment.

# Objectives
# The behavior of your program should look like this:
# Prompt a user to enter their credit principal and choose one of the two parameters, 
# i.e. the count of periods or the monthly payment.
# To perform further calculations, you'll also have to ask for the lacking value.
# Finally, inform the user of your results.

# Examples
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that it's not the part of the input.

# Example 1:
# Enter the credit principal:
# > 1000
# What do you want to calculate? 
# type "m" - for count of months, 
# type "p" - for monthly payment:
# > m
# Enter monthly payment:
# > 150
# It takes 7 months to repay the credit

# Example 2:
# Enter the credit principal:
# > 1000
# What do you want to calculate? 
# type "m" - for count of months, 
# type "p" - for monthly payment:
# > m
# Enter monthly payment:
# > 1000
# It takes 1 month to repay the credit

# Example 3:
# Enter the credit principal:
# > 1000
# What do you want to calculate? 
# type "m" - for count of months, 
# type "p" - for monthly payment:
# > p
# Enter count of months:
# > 10 
# Your monthly payment = 100

# Example 4:
# Enter the credit principal:
# > 1000
# What do you want to calculate? 
# type "m" - for count of months, 
# type "p" - for monthly payment
# > p
# Enter count of months:
# > 9 
# Your monthly payment = 112 with last month payment = 104.

def check_input():
    parameter = input("""What do you want to calculate?
        type "m" - for count of months, 
        type "p" - for monthly payment: \n""")
        
    if parameter != "m" and parameter != "p":
        check_input()
    else:
        return parameter

def calc_payments(credit):
    payment = int(input('Enter monthly payment: '))
    remaining_period = math.ceil(credit / payment)
    period_message = str(remaining_period) + ' month'

    if remaining_period > 1:
        period_message += 's'
    
    print(f'It takes {period_message} to repay the credit')

def calc_period(credit):
    count = int(input('Enter count of months: '))
    payment = credit / count
    payments_message = 'Your monthly payment = ' + str(math.ceil(payment))
    
    if credit % count != 0:
        payments_message += " with last payment = " + str(credit - math.ceil(payment) * (count - 1))

    print(payments_message)


credit = int(input('Enter the credit principal: '))
parameter = check_input()

if parameter == "m":
    calc_payments(credit)
else:
    calc_period(credit)
