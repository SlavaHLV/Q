A = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
b=bool()
for i in range(len(A)-2):
 if ((A[i])==(A[i+1]))>0:
   b=1
if b:
 print('est chisla s odinakovymi znakami')
else:
 print('net takyh chisel')
