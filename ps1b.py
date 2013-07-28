bal=float(raw_input('The outstand balance on the credit card:'))
int_rate=float(raw_input('Annual interest rate:'))
count=0
pmt=bal/((1-(1/(1+int_rate/12)**12))/(int_rate/12))


pmt_10=round(0.5+pmt/10.0)
pmt_round=pmt_10*10
while bal>0:
    bal=round(bal+bal*int_rate/12,0)
    bal=bal-pmt_round
    count=count+1



   
print('RESULT')
print('Monthly payment to pay off debt in 1 year: $')+str(pmt_round)
print('Number of months needed: ') + str(count)
print('Balance: ') + str(bal)

