import math
def prim(x): 
    if x<2: 
        return False
    for i in range(2,int(math.sqrt(x))+1): 
        if x%i==0: 
            return False 
    return True  

n=int(input("citeste n "))
n=n+1 
while not prim(n): 
    n=n+1 
print(n)
