/*
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

*/

rows = int (input ("Enter no. of rows : "))

for i in range (1,rows+1):
  num = 1
  for j in range (i):
    print(num,end= " ")
    num+=1
  print()
    
    
    
