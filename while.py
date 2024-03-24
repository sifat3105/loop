cash = 1000
target_cash = 10000
interest = 0.10

year = 0

while cash < target_cash:
    year+=1
    cash += cash * interest
    
print("it take to {} year to get balance {}".format(year,target_cash))