apple=15.5
orange=20
grape=10.25
l="liter"

totalvolume=apple+orange+grape
print(totalvolume,"L")

totalvolume=int(totalvolume)
print(totalvolume,"L")    

totalvolume=str(totalvolume)
print("total liters sold:", totalvolume,"L")

import random
randomliter=random.randrange(5,10)

totallitervolume=int(totalvolume)+randomliter
print("Final total liters available:", totallitervolume,"L")