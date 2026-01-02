fruits=['apple','banana','orange']
vegetables=['tomato','carrot','onion']
beverages=['wine','water','juice']
fruits.append('grapes')
vegetables.insert(1,'brinjal')
beverages.pop()
inventory=[fruits,vegetables,beverages]
print(inventory)

twofruits=fruits[:2]
print(twofruits)

print(vegetables[-1])

fruitlen=[len(a) for a in fruits]
print(fruitlen)

print('water' in beverages)

tuple=[]
tuple.extend([fruits[0],vegetables[0],beverages[0]])
print(tuple)