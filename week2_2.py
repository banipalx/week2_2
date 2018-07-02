# Problem 2

'''

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal


Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

'''
#

init_balance = balance  # enter balance here to check
minimumFixedMonthlyPayment = 0
monthlyInterestRate = annualInterestRate / 12

while balance > 0:
    for month in range(12):
        monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
    if balance > 0:
        minimumFixedMonthlyPayment += 10
        balance = init_balance
    else:
        break
print('Lowest payment: ' + str(minimumFixedMonthlyPayment))


# Another method without the if/else statements

# Test
balance = 87
annualInterestRate = 0.2

# Code
newBalance = balance  # enter balance here to check
monthlyInterestRate = annualInterestRate / 12
minimumFixedMonthlyPayment = monthlyInterestRate * balance // 10 * 10

while newBalance > 0:
    newBalance = balance
    monthlyUnpaidBalance = 0
    minimumFixedMonthlyPayment += 10
    for month in range(12):
        monthlyUnpaidBalance = newBalance - minimumFixedMonthlyPayment
        updateBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
        newBalance = updateBalance
print('Lowest payment: ', minimumFixedMonthlyPayment)
