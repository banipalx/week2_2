# Problem 1

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12
num = 1

while num <= 12:
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyUnpaidBalance*monthlyInterestRate
    remainingBalance = balance
    num += 1

print(round(remainingBalance, 2))
