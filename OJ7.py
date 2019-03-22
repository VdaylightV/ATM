sTr = input()
sTr1 = sTr.split()
lst = []
dict = {}

for item in sTr1:
    if item[-1] in ",.\'\"":
        item = item[:-1]
    dict[item]=dict.get(item, 0) + 1

print(dict)
dict =  sorted(dict.items(), key= lambda x:x[1])
print(dict)
