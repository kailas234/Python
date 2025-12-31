reciept='''      My Book Store
The customer bought 2 items:
Book Title: {0} – {1}
Book Title: {2} – {3}
Total Price:\t {totalprice}
'''
Rate= reciept.format("Python Basics", 450,"Data Science Intro", 600,totalprice=450+600)
print(Rate.upper())
print("\nthank".upper() + "you".upper())