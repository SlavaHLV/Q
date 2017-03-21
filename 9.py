A = [ input() for i in range(int(input()))]
i = 0
max = A[i]
while i < len(A):
 if A[i] > max:
    max = A[i]
 i = i + 1;
print (max)
