n=int(input('Enter A Number: '))
result=n%2
if n in range(1,101):
    if result!=0:
        print('Weird')
    elif (result==0) and (result in range(2,6)):
        print('Not Weird')
    elif (result==0) and (result in range(6,21)):
        print('Not Weird')
    elif (result==0) and (n>20):
        print('Not Weird')
