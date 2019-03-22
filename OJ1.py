import math
def fac(x):
    lst = []
    for i in range(1,int(math.sqrt(x))+1):
        if x % i == 0:
            lst.append(int(i))
    for item in lst:
        if int(x)/int(item) not in lst:
            lst.append(int(x/item))
        else:
            pass
    lst.remove(x)
    return lst

def MA(lst):
     sum = 0
     for item in lst:
        sum += int(item)
     return sum

#print(fac(100))
number = int(input())

if number <= 1000:
    print("220-284")
else:
    for i in range(1, round(number/2)):
         for j in range(i+1, number+1):
              if (i != j and MA(fac(j)) == i and MA(fac(i))==j ):
                  print("{}-{}".format(i,j))
