import turtle
pF = ["F","+","R","+","F","-","-","R","-","-","F","+","R","+","F"]
pR = "R"
p=["F","-","-","R","-","-","F","-","-","R","-","-"]
f=10
r=10
def step(p):
    np=[]
    for i in range (0,len(p)):
        if (p[i]=="+"):
            np+=p[i]
        elif (p[i]=="-"):
            np+=p[i]
        elif (p[i]=="R"):
            np+=pR
        elif (p[i]=="F"):
            np+=pF
        else:
            np+=step(p[i])
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
o.speed(10)
np=[]
for i in range(0,4):
    np=step(p)
    p=np
draw(p)
