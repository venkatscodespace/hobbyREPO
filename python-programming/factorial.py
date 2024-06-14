N=int(input('Enter a number (between 1 and 10) to calculate factorial: '))
if N in range(1,11):
    c=1
    for i in range(1,N+1):
        c=c*i
    print(c)
else:
  print('Number is greater than 10 (or) lesser than 1. ')
