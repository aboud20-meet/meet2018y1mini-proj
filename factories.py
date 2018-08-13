

num= 200
factors=[]
while num>1:
    if num % 2==0:
        num=num /2
        factors.append(2)
    if num % 3==0:
        num=num /3
        factors.append(3)
    if num % 5==0:
        num=num /5
        factors.append(5)
    
print(factors)
