import random
import sys

file=open("datacor.txt","a")

def printgrid(grid,gridsize):
    for i in range(gridsize):
        towrite=""
        for x in grid[i]:
            towrite+=str(x)+" "
        towrite+="\n"
        sys.stdout.write(towrite)

def printrombus(grid,gridsize,a,b,rombus_size):
    for i in range(gridsize):
        towrite=""
        for j in range(gridsize):
            if abs(i-a)+abs(j-b)<=rombus_size:
                towrite+=str(grid[i][j])+"!"
            else:
                towrite+=str(grid[i][j])+" "
        towrite+="\n"
        sys.stdout.write(towrite)

gridsize=40
number_people=50
siml=100000
movements=[[1,0],[-1,0],[0,1],[0,-1]]
rombus_size=3
people_limit=5
number_of_sim=2000


for sim in range(number_of_sim):
    print(sim)
    grid=[0]*gridsize
    for i in range(gridsize):
        grid[i]=["."]*gridsize
        if i==0 or i==gridsize-1:
            grid[i]=["#"]*gridsize
        grid[i][0]="#"
        grid[i][gridsize-1]="#"
    #for i in range(gridsize):
        #print(*grid[i])
    people_names="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    people=[]
    for i in range(number_people):
        x=random.randint(1,gridsize-2)
        y=random.randint(1,gridsize-2)
        while grid[x][y]!=".":
            x=random.randint(1,gridsize-2)
            y=random.randint(1,gridsize-2)
        people.append([x,y])
        grid[x][y]=people_names[i]
    #printgrid(grid,gridsize)


    output=[]
    for step in range(siml):
        continue_simulation=True
        for person in people:
            movement=random.choice(movements)
            newx=person[0]+movement[0]
            newy=person[1]+movement[1]
            free=True
            if newx>=gridsize-1 or newx==0 or newy>=gridsize-1 or newy==0:
                free=False
            if grid[newx][newy]!=".":
                free=False
            if free:
                name=grid[person[0]][person[1]]
                grid[person[0]][person[1]]="."
                grid[newx][newy]=name
                person[0]=newx
                person[1]=newy
        #printgrid(grid,gridsize)
        number_of_clusters=[0]*6
        for i in range(1,gridsize-1):
            for j in range(1,gridsize-1):
                number_people2=0
                for line in range(i-rombus_size,i+rombus_size+1):
                    if line>0 and line<gridsize-1:
                        dist=abs(line-i)
                        width=rombus_size-dist
                        for column in range(j-width,j+width+1):
                            if column>0 and column<gridsize-1 and grid[line][column]!=".":
                                number_people2+=1
                if number_people2>people_limit:
                    print("illegal gathering")
                    print(i,j)
                    #printrombus(grid,gridsize,i,j,rombus_size)
                    continue_simulation=False
                    
                else:
                    number_of_clusters[number_people2]+=1
            if not continue_simulation:
                break
        if not continue_simulation:
            break
        output.append(number_of_clusters)
        
    print(len(output))
    #for i in range(len(output)):
        #print(len(output)-i,output[i])
    if len(output)>9 and len(output)<siml-1:
        file.write(str(len(output))+"\n")
        for i in range(len(output)):
            file.write(str(len(output)-i)+" ")
            for value in output[i]:
                file.write(str(value)+" ")
            file.write("\n")
        file.write("££\n")
file.close()
