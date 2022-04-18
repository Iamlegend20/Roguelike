import os
import time
class Grid:
    def __init__(self, x_length, y_length, z_length=1):
        self.x_length = x_length
        self.y_length = y_length 
        self.z_length = z_length
        self.grid = self.create_grid()

    def create_grid(self):
        grid=[]
        if self.z_length == 1:
            for i in range(self.x_length):
                grid.append([])
                for j in range(self.y_length):
                    grid[i].append(Tile())
            return grid
        
        elif self.z_length > 1:
            for i in range(self.x_length):
                grid.append([])
                for j in range(self.y_length):
                    grid[i].append([])
                    for k in range(self.z_length):
                        grid[i][j].append(Tile())
            return grid        
    
    def plot(self):
        if self.z_length == 1:
            x = 0
            y = self.y_length - 1
            for i in range(self.y_length): 
                for j in range(self.x_length):
                    print(self.grid[x][y], end="")
                    x += 1
                print()
                y -= 1
                x = 0        
        elif self.z_length > 1:    
            x = 0
            y = self.y_length - 1
            z = 0
            for i in range(self.z_length):
                for i in range(self.y_length): 
                    for i in range(self.x_length):
                        print(self.grid[x][y][z], end="")
                        x += 1
                    print()
                    y -= 1
                    x = 0        
                print()
                x = 0
                y = self.y_length - 1
                z +=1
    
    def update(self):
        os.system("cls")
        self.plot()                

class Tile:
    def __init__(self, is_blocked=False, is_lookable=False):
        self.occupants = []
        self.is_blocked = is_blocked
        self.is_lookable = is_lookable
    def __repr__(self):
        if len(self.occupants) > 0:
            return repr(self.occupants[0])
        if self.is_blocked:
            return "#"
        if not self.is_blocked:
            return "."

class Character:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "@"
    def move(self,grid,direction):
        x,y = self.location[0],self.
        if direction == 4:
            pass


def main():
    grid = Grid(5,5,2)
    grid.grid[2][2].occupants.append(Character([2,2]))
    grid.update()
    grid.grid[1][2].occupants.append(Character([1,2]))
    time.sleep(2)
    grid.grid[2][2].occupants.pop()
    grid.update()

    #grid.grid[1][2].occupants.append(Character((1,2)))


    #running = True
    #while running:
        #update()
if __name__ == '__main__':
    main()



