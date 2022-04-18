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
    
    def spawn(self, thing, x_pos, y_pos, z_pos=0):
        self.grid[x_pos][y_pos][z_pos].occupants.append(thing([2,2]))  #working on. delete 2d grid code.

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
            return repr(self.occupants[0]) #update for multiple occupants with id system
        if self.is_blocked:
            return "#"
        if not self.is_blocked:
            return "."

class Character:
    id = 1
    def __init__(self, x_pos, y_pos, z_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.id = id
        id += 1
        #self.tile_location = grid.grid[x_pos][y_pos][z_pos].occupants[0]
    def __repr__(self):
        return "@"
    def move(self, grid, direction):
        me = grid.grid[x_pos][y_pos][z_pos].occupants[0] #working on adding a way to identify where self is. id system
        if direction == 4:
            grid.grid[x_pos-1][y_pos][z_pos].occupants.append(me)
            


def main():
    grid = Grid(5,5)
    grid.grid[2][2].occupants.append(Character([2,2]))
    grid.update()
    grid.grid[1][2].occupants.append(Character([1,2]))
    time.sleep(2)
    grid.grid[2][2].occupants.pop()
    grid.update()

    #running = True
    #while running:
        #update()
if __name__ == '__main__':
    main()



