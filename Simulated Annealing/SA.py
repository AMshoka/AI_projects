
import math
import random



def calcus(x,y):
    return -0.0001*((
        math.fabs(
            math.sin(x)*math.sin(y)*math.exp(
                math.fabs(
                    100 - math.sqrt(x**2+y**2)/math.pi
                )
            )
        )+1
                    )**0.1)

def generator():
    range = 5
    return random.randint(-6,6)


def amir():
    print()



def amir12():
    print()


def SA():

    x=[]
    y=[]




    cuurentX=random.random()*10
    currentY = random.random()*10

    temperature = 100
    iteration = 1
    while 1:
        current_state = calcus(cuurentX,currentY)

        tempX = cuurentX +generator()
        tempY = currentY+generator()
        next_state = calcus(tempX,tempY)

        if next_state < current_state:
            currentY = tempY
            cuurentX = tempX
        else:
            probablity =math.exp(-1*(next_state-current_state)/temperature)
            if random.random() <= probablity:
                currentY = tempY
                cuurentX = tempX

        iteration = iteration+1
        temperature = temperature *0.9

        if iteration > 1000:
            if current_state < next_state:
                next_state = current_state
            return cuurentX,currentY,next_state

answer = SA()
print (answer)