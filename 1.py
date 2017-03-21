s = int(input('vvedite god:'))
if ((s % 4 == 0) and not (s % 100 == 0)) or (s % 400 == 0) :
 print('visokosniy')
else:
 print('ne visokosniy')
