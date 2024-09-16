l=eval(input("Enter Set 1:"))
t=eval(input("Enter Set 2:"))
s=[]
for i in l:
    for j in t:
        if i==j:
            s.append(i)
            break
print(s)
