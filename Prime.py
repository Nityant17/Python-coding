n=int(input('Enter Number:'))
r=0
for i in range(2,n):
    if n%i==0:
        r=1
        break
    else:
        continue
if n<=1:
    print('wrong input')
elif r==1:
    print(n,'is not prime')
else:
    print(n,'is prime')
