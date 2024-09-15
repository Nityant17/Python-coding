n=int(input("Enter no. of terms:"))
x=float(input("Enter x of Sin(x) in radians:"))
sum=0
for i in range(1,n+1):
    fact=1
    k=(2*i)-1
    for j in range(1,k+1):
        fact*=j
    pw=x**k
    if (i%2==0):
        pw*=(-1)
    sum+=(pw/fact)
print(sum)
