l=eval(input("Enter List 1:"))
t=eval(input("Enter List 2:"))
s=[]
for i in l:
    for j in t:
        if i==j:
            s.append(i)
            break
print(s)
