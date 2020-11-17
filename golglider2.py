from microbit import *

oldWorld = Image("09000:"
                 "00900:"
                 "99900:"
                 "00000:"
                 "00000:")

newWorld = Image()

def getneighbors(x,y):
    n=0
    for i in range(-1,2):
        for j in  range(-1,2):
            n += oldWorld.get_pixel((i+x+5)%5,(j+y+5)%5)

    n-=oldWorld.get_pixel(x,y)
    return n

while True:
    display.show(oldWorld)
    for x in range(0,5):
        for y in range(0,5):
            print("x",x,"y",y,oldWorld.get_pixel(x,y))
            neigh = getneighbors(x,y)
            print(x,y,neigh)
            if oldWorld.get_pixel(x,y)==9 and neigh < 2*9:
                newWorld.set_pixel(x,y,0)
            elif oldWorld.get_pixel(x,y)==9 and neigh > 3*9:
                newWorld.set_pixel(x,y,0)
            elif oldWorld.get_pixel(x,y)==0 and neigh==3*9:
                newWorld.set_pixel(x,y,9)
            else:
                newWorld.set_pixel(x,y,oldWorld.get_pixel(x,y))

    sleep(500)
    display.clear()
    display.show(newWorld)
    oldWorld = newWorld.copy()
    newWorld.fill(0)