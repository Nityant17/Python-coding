key=eval(input("Enter List of Keys:"))
val=eval(input("Enter List of Values:"))
d={}
for i in range(len(key)):
    d[key[i]]=val[i]
print(d)
