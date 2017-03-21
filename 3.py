z = int(input('1 dlinna storoni:'))
x = int(input('2 dlinna storoni:'))
c = int(input('3 dlinna storoni:'))
if (z+x>c) and (z+c>x) and (x+c>z):
 print('treugolnik suwestvuet')
else:
 print('treugolnik ne sushestvuet')
