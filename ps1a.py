bal=float(raw_input('The outstand balance on the credit card:'))
int_rate=float(raw_input('Annual interest rate:'))
min_pay=float(raw_input('Minimum monthly payment rate:'))
total_pay=0.0

for x in range(1, 13):
    print 'Month: '+str(x)
    payment=round(bal*min_pay,2)
    total_pay=total_pay+payment
    print 'Minimum monthly payment: $' + str(payment)
    interest_paid=round(bal*int_rate/12,2)
    princ_paid=round(payment-interest_paid,2)
    print 'Principal paid: $' + str(princ_paid)
    bal=round(bal-princ_paid,2)
    print 'Remaning balance: $' + str(bal)
print('RESULT')
print('Total amount paid: $')+str(total_pay)
print 'Remaning balance: $' + str(bal)

