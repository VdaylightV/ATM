number = input()
def fac(x):
    lst = []
    for i in range(1,x):
        if x % i ==0:
            lst.append(i)
    return lst

def MA(lst):
    sum = 0
    for item in lst:
        sum += int(item)
    return sum


for i in range(2, int(number)+1):
    if int(i)== MA(fac(i)):
       print(i)
