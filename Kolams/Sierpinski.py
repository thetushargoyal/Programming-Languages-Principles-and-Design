import turtle
# F = + R - F - R
# F = f
# R = - F + R + F
# R = r
pF = ["+", "R", "-", "F", "-", "R"]
pR = ["-", "F", "+", "R", "+", "F"]
f=5
r=5
def step(p):
    np=[]
    print(p)
    for i in range (0,len(p)):
        if (p[i]=="+"):
            np+=p[i]
        elif (p[i]=="-"):
            np+=p[i]
        elif (p[i]=="R"):
            np+=pR
            np+="-"
        elif (p[i]=="F"):
            np+=pF
            np+="+"
        else:
            np+=step(p[i])
        print(p[i])
        print(np)
    return(np)

def draw(p):
    for i in range (0,len(p)):
        if (p[i]=="+"):
            o.left(45)
        elif (p[i]=="-"):
            o.right(45)
        elif (p[i]=="R"):
            o.forward(r)
        elif (p[i]=="F"):
            o.forward(f)
        else:
            draw(p[i])

o=turtle.Turtle()
p=pF
np=[]
for i in range(0,4):
    np=step(p)
    print(np)
    p=np
draw(p)
