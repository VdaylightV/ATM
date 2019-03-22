def DG(NM):
         int(NM)
         if NM == 2:
             pass
         if NM !=2:
            if NM % 2 == 0:
               print("{}/2={}".format(int(NM), int(NM/2)))
               NM = NM/2
               if NM == 2:
                  pass
               else:
                  DG(NM)
            else:
               print("{}*3+1={}".format(int(NM),int(NM*3+1)))
               NM = 3*NM +1
               if NM == 2:
                  pass
               else:
                  DG(NM)

         return "2/2=1"

x = int(input())
print(DG(x))
