# Description
# Let's think about what credit calculator should be able to do. 
# In general, it takes several parameters like a credit principal 
# and a credit interest, calculates the needed values 
# (for example, monthly payment or overpayment) and outputs them.

# Not familiar with these concepts?
# Don't worry, we will explain them to you in simple terms. 
# The principal is the original amount of money you get on credit. 
# And the interest is a charge for borrowed money, 
# usually calculated as a percentage of such a loan.

# Objective
# Let's start by imitating this behavior. 
# There are some prepared variables in source code that are ready for use: 
# these are text messages that our credit calculator could output. 
# At this stage, all you need to do is output them in the right order.

# Example
# Output:

# Credit principal: 1000
# Month 1: paid out 250
# Month 2: paid out 250
# Month 3: paid out 500
# The credit has been repaid!

credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

print(credit_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)
