matrix = []
count = int(input())
for count in range(1, count+1):
   x = input()
   lst=x.split()
   count -= 1
   matrix.append(lst)

sum = 0
for item in matrix:
    for i in range(1, count+1):
        sum = sum + item[i-1][i-1] + item[i-1][count-(i-1)]






















# sTr = input()
# sTr2 = sTr.lower()
# lst=sTr2.split()
# Out = []
#
# #
# # #print(Out)
# A = ''.join(lst)
# #print(A)
#
# All = []
# Result = []
# for i in range(97,123):
#     All.append(chr(i))
#
# for item in All:
#     Result.append(A.count(item))
#
# print(Result)
