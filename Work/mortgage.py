# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)


# Exercise 1.8
print("--------1.8----------")
principal = 500_000
rate = 0.05
payment = 2684.11
total_paid = 0
month = 0
overpayment = 1_000
overpayment_months = 12


while principal > 0:
    if month < overpayment_months:
        additional_payment = overpayment
    else:
        additional_payment = 0

    principal = principal * (1+rate/12) - (payment + additional_payment)
    total_paid += (payment + additional_payment)
    month += 1

print(f"Total paid: ${total_paid:,.2f}")
print(f"Months: {month}")

# Exercise 1.9
print("\n\n--------1.9----------")

principal = 500_000
rate = 0.05
payment = 2684.11
total_paid = 0
month = 0
extra_payment = 1_000
extra_payment_start_month = 61
extra_payment_end_month = 108


while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        additional_payment = extra_payment
    else:
        additional_payment = 0

    if payment + additional_payment > principal * (1+rate/12):
        total_paid += principal * (1+rate/12) + additional_payment
        principal = 0
    else:
        principal = principal * (1+rate/12) - (payment + additional_payment)
        total_paid += (payment + additional_payment)
    month += 1

    print(f"{month:>3} {total_paid:>10,.2f} {principal:>10,.2f}")

print(f"Total paid: ${total_paid:,.2f}")
print(f"Months: {month}")