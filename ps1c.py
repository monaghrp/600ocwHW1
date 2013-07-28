bal=float(raw_input('The outstand balance on the credit card:'))
int_rate=float(raw_input('Annual interest rate:'))
count=0

min_pay=bal/12.0
max_pay=(bal*(1.0+(int_rate/12.0))**12.0)/12.0
pmt=round((min_pay+max_pay)/2.0,2)
done=0

while done!=1:
    bal_temp=round(bal,2)
    for count in range (1,13):
              bal_temp=round(bal_temp+bal_temp*int_rate/12.0,2)
              bal_temp=round(bal_temp-pmt,2)
    if abs(bal_temp)<.1:
        done=1
    if bal_temp<0:
        ##make payment smaller
        ##set new upper bound
   
        max_pay=round(pmt,2)
        pmt=round((min_pay+max_pay)/2.0,2)
        ##pmt=pmt-(pmt-min_pay)/2.0
    else:
        ##make payment bigger
        ##set new lower bound
   
        min_pay=round(pmt,2)
        pmt=round((min_pay+max_pay)/2.0,2)
        ##pmt=pmt+(pmt-max_pay)/2.0
    
              
    
print('RESULT')
print('Monthly payment to pay off debt in 1 year: $')+str(pmt)
print('Number of months needed: ') + str(count)
print('Balance: ') + str(bal_temp)

