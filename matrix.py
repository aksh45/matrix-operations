
#code for matrix multiplication
a,b=map(int,input("No of rows and coloumns of matrix 1 ").split())
c,d=map(int,input("No of rows and coloumns of matrix 2 ").split())
if b==c:
   li1=[]
   li2=[]
   fl=[]
   for x in range(a):
      lis=[]
      for i in range(b):
         lis.append(int(input()))
      print()
      li1.append(lis)
   for x in range(c):
      lis1=[]
      for i in range(d):
         lis1.append(int(input()))
      print()
      li2.append(lis1)

   for x in range(a):
      l=0
      fll=[]
      for g in range(d):
         c=0
         for z in range(b):
            c+=li1[x][z]*li2[z][l]
         fll.append(c)
         l+=1
      fl.append(fll)  
   for x in range(len(fl)):
      for j in fl[x]:
         print(j,end=" ")
      print()
   print("order of matrix is "+str(a)+"X"+str(d))

