from random import *
import math

#hamilton cycle for even,even or even,odd

def HamilotoniEEorEO(Row, Column):
    i = 0
    k = 1
    flag = True
    for j in range(Column):
        flag = not flag
        if (j == 0):
            while i < Row:
                route.append(Column * i + j)

                i = i + 1
                k = k + 1


        else:
            if (flag):
                i = Row - 1;
                while i > 0:
                    route.append(Column * i + j)
                    i = i - 1
                    k = k + 1



            else:
                i = 1
                while i < Row:
                    route.append(Column * i + j)
                    i = i + 1
                    k = k + 1

    i = 0
    j = Column - 1
    while (j > 0):
        route.append(Column * i + j)
        k = k + 1
        j = j - 1


# function for hamiltoni cycle for Odd to even


def HamiltoniOE(Row, Column):
    j = 0
    k = 1
    flag = True
    for i in range(Row):
        flag = not flag
        if (i == 0):
            while j < Column:
                route.append(Column * i + j)

                j = j + 1
                k = k + 1


        else:
            if (flag):
                j = Column - 1;
                while j > 0:
                    route.append(Column * i + j)
                    j = j - 1
                    k = k + 1



            else:
                j = 1
                while j < Column:
                    route.append(Column * i + j)
                    j = j + 1
                    k = k + 1

    j = 0
    i = Row - 1
    while (i > 0):
        route.append(Column * i + j)

        k = k + 1
        i = i - 1


# function for enviroment

def Enviroment(rc, cc, Action, w):
    if Action == "up":


        w += 1#w is the number of cost

        return [rc - 1, cc, Env[rc - 1][cc], w]

    if Action == "down":

        w += 1
        return [rc + 1, cc, Env[rc + 1][cc], w]

    if Action == "left":

        w += 1
        return [rc, cc - 1, Env[rc][cc - 1], w]

    if Action == "right":

        w += 1
        return [rc, cc + 1, Env[rc][cc + 1], w]

    if Action == "suck":


        Env[rc][cc] = 0
        return [rc, cc, Env[rc][cc], w]

    if Action == "NoOp":
        return [rc, cc, Env[rc][cc], w]



#function for Agent
def Agent(rc, cc, status, count, index, index1, route):
    while True:
        if Env[rc][cc] == 1:
            route1.append("suck")

        index = index + 1
        if (index < len(route)):
            count += 1;
            current = route[index]

            for i in range(Row):
                for j in range(Column):
                    if (current == hamiltomap[i][j]):
                        if (i == rc and cc + 1 == j):
                            cc += 1
                            route1.append("right")

                        elif (i == rc and cc - 1 == j):
                            cc -= 1
                            route1.append("left")

                        elif (cc == j and rc + 1 == i):
                            rc += 1
                            route1.append("down")

                        elif (cc == j and rc - 1 == i):
                            rc -= 1
                            route1.append("up")





        else:
            if count < len(route):
                current = route[index1]
                index1 += 1
                count += 1;
                for i in range(Row):
                    for j in range(Column):
                        if (current == hamiltomap[i][j]):
                            if (i == rc and cc + 1 == j):
                                cc += 1
                                route1.append("right")

                            elif (i == rc and cc - 1 == j):
                                cc -= 1
                                route1.append("left")

                            elif (cc == j and rc + 1 == i):
                                rc += 1
                                route1.append("down")

                            elif (cc == j and rc - 1 == i):
                                rc -= 1
                                route1.append("up")

            else:
                route1.append("NoOp")
                break


# -------------------------------------------------main------------------------------------

#get input
Row = int(input("Please enter the rows of your Enviroment(Matrix):"))
Column = int(input("Please enter the columns of your Enviroment(Matrix):"))

#create Env matrix and hamiltomap martrix
hamiltomap = [[0] * Column for i in range(Row)]
Env = [[0] * Column for i in range(Row)]


# insert random number in enviroment for dirty and clean
for i in range(Row):
    for j in range(Column):
        Env[i][j] = randint(0, 1)
#print Enviroment before cleaning
print("Enviroment before vacume is:")
for i in Env:
  print(' '.join([str(j) for j in i]))
count = 0;
route = []
route1 = []
distance=[0.0,0.0,0.0,0.0]
routeodd=[]
# random place
r = randint(0, Row - 1)
c = randint(0, Column - 1)

print("Agent is inserted in Row:"+str(r)+"  "+"Column:"+str(c))
# insert hamiltonmap
for i in range(Row):
    for j in range(Column):
        hamiltomap[i][j] = count
        count += 1




#if dimension of matrix is odd odd
if Row%2!=0 and Column%2!=0:
    distance[0] = math.sqrt((0 - r) ** 2 + (0 - c) ** 2)
    distance[1] = math.sqrt((0 - r) ** 2 + (Column - 1 - c) ** 2)
    distance[2] = math.sqrt((Row - 1 - r) ** 2 + (0 - c) ** 2)
    distance[3] = math.sqrt((Row - 1 - r) ** 2 + (Column - 1 - c) ** 2)
    mini = distance[0]
    flag = 0
    for i in range(4):
        if (distance[i] < mini):
            mini = distance[i]
            flag = i

    if (flag == 0):
        i = r
        j = c
        while j != 0:
            routeodd.append("left")
            j -= 1

        while i != 0:
            routeodd.append("up")
            i -= 1

        flag1 = 0

        for i in range(Row):
            for j in range(Column - 1):
                if flag1 == 0:
                    routeodd.append("right")
                if flag1 == 1:
                    routeodd.append("left")

            if (i != Row - 1):
                routeodd.append("down")
                flag1 = not flag1

    if (flag == 1):
        i = r
        j = c
        while j != Column - 1:
            routeodd.append("right")
            j += 1

        while i != 0:
            routeodd.append("up")
            i -= 1
        flag1 = 0
        j = Column - 1
        for i in range(Row):
            while j > 0:
                if flag1 == 0:
                    routeodd.append("left")
                if flag1 == 1:
                    routeodd.append("right")
                j -= 1

            if (i != Row - 1):
                routeodd.append("down")
                flag1 = not flag1
            j = Column - 1

    if (flag == 2):
        i = r
        j = c
        while j != 0:
            routeodd.append("left")
            j -= 1

        while i != Row - 1:
            routeodd.append("down")
            i += 1

        flag1 = 0
        i = Row - 1

        while i >= 0:
            for j in range(Column - 1):
                if flag1 == 0:
                    routeodd.append("right")
                if flag1 == 1:
                    routeodd.append("left")

            if (i != 0):
                routeodd.append("up")
                flag1 = not flag1
            i -= 1

    if (flag == 3):
        i = r
        j = c
        while j != Column - 1:
            routeodd.append("right")
            j += 1

        while i != Row - 1:
            routeodd.append("down")
            i += 1
        flag1 = 0
        i = Row - 1
        j = Column - 1
        while i >= 0:

            while j != 0:
                if flag1 == 0:
                    routeodd.append("left")
                if flag1 == 1:
                    routeodd.append("right")
                j -= 1

            if (i != 0):
                routeodd.append("up")
                flag1 = not flag1
            j = Column - 1
            i -= 1

    count = 1
    current = hamiltomap[r][c]
    percept = [r, c, Env[r][c], 0.0]


    l = 0

    while l < len(routeodd):
        cost = percept[3]
        if(Env[percept[0]][percept[1]]==1):
            percept=Enviroment(percept[0], percept[1], "suck", cost)
        percept = Enviroment(percept[0], percept[1], routeodd[l], cost)
        if (Env[percept[0]][percept[1]] == 1):
            percept = Enviroment(percept[0], percept[1], "suck", cost)

        l += 1




    print("Scrolled track :"+str(routeodd))

    print("Enviroment after vacume is:")
    for i in Env:
        print(' '.join([str(j) for j in i]))

    print("cost is:" +str( len(routeodd)))


else:

    #if dimension of matrix is even,even or even,odd

    if (Row % 2 != 0):
        HamilotoniEEorEO(Row, Column)
    #if dimension of matrix is odd,even
    else:
        HamiltoniOE(Row, Column)

    print(route)

    count = 1
    current = hamiltomap[r][c]
    percept = [r, c, Env[r][c], 0.0]
    print(percept)
    for k in range(len(route)):
        if (current == route[k]):
            current = route[k]
            index = k


    index1 = 0;

#call Agent
    Agent(r, c, 12, count, index, index1, route)

    l = 0


#call Enviroment
    while l < len(route1):
        cost = percept[3]
        percept = Enviroment(percept[0], percept[1], route1[l], cost)

        l += 1



    print("Scrolled track:"+str(route1))
    print("Enviroment after vacume is:")
    for i in Env:
        print(' '.join([str(j) for j in i]))

    print("cost is:"+str(cost))









