
'''

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection
search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt
 within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to
 Problem 2 to compare!). Produce the same return value as you did in Problem 2.


'''

# Test
balance = 320000
annualInterestRate = 0.2


# Code
monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
guess = (upperBound + lowerBound) / 2.0

while True:
    updateBalance = balance
    for i in range(0, 12):
        monthlyUnpaidBalance = updateBalance - guess
        updateBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
    if updateBalance >= 0 and updateBalance <= 0.01:
        break
    else:
        if updateBalance > 0:
            lowerBound = guess
        else:
            upperBound = guess
    guess = (upperBound + lowerBound) / 2.0

print('Lowest payment: ', round(guess, 2))



# Code
monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
guess = (upperBound + lowerBound) / 2.0

while abs(updateBalance) > 0.01:
    updateBalance = balance
    for i in range(0, 12):
        monthlyUnpaidBalance = updateBalance - guess
        updateBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
        if updateBalance > 0:
            lowerBound = guess
        else:
            upperBound = guess
    guess = (upperBound + lowerBound) / 2.0

print('Lowest payment: ', round(guess, 2))
