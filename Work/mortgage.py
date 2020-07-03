# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input('Start Month: '))
extra_payment_end_month = int(input('End Month: '))
extra_payment = int(input('Payment Extra: '))

while principal > 0:
    if month >= extra_payment_start_month and month < extra_payment_end_month:
        extra = extra_payment
    else:
        extra = 0
    principal = (principal * (1+rate/12) - payment) - extra
    total_paid = (total_paid + payment) + extra
    month += 1
    print(round(month, 2), round(total_paid, 2), 
          round(principal, 2) if principal > 0 else 0)

print()
print(f'Total paid: {total_paid:0.2f}')
print(f'Months: {month:>7d}')
