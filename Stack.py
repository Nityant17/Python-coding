s=[]
def push(d):
    s.append(d)
def pop():
    s.pop()
def Check_if_Empty():
    if s!=[]:
        return "False"
    else:
        return "True"
push(5)
push(10)
pop()
c=Check_if_Empty()
print("Stack after operation:",s)
print("Is stack empty:",c)
