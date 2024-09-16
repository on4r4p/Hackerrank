from collections import OrderedDict

n = int(input());stock = OrderedDict()

for _ in range(n):
    *item,price = input().split(" ") ;item = " ".join(item)
    if item in stock:
        stock[item] += int(price)
    else:
        stock[item] = int(price)        
for key,value in stock.items():
    print("%s %s"%(key,value))
