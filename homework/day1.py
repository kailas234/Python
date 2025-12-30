riceperkg=45
sugarperkg=40
oilperkg=130
rice_sold,sugar_sold,oil_sold=3,2.5,1.8
print (float(rice_sold))
totalricesold=riceperkg*rice_sold
totalsugarsold=sugarperkg*sugar_sold
totaloilsold=oilperkg*oil_sold
totalamount=totalricesold+totalsugarsold+totaloilsold
print("totalricesold:",totalricesold)
print("totalsugarsold:",totalsugarsold)
print("totaloilsold:",totaloilsold)
print("totalamount:",totalamount)
print(int(totalamount))
print(str(totalamount))
import random
randomtax=random.randrange(5,10)
totalpricedc=totalamount+randomtax
print("totalpricedc:",totalpricedc)