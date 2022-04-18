import os
import time
class Grid:
    def __init__(self, x_length, y_length, z_length=1):
        self.x_length = x_length
        self.y_length = y_length 
        self.z_length = z_length
        self.grid = self.create_grid()

    def create_grid(self):
        """
        Creating a grid with the design intent of accessing individual tiles with 
        grid[x][y][z] notation, similar to a standard cartesian coordinate system. 
        Ex. 2x2x2 grid : [ [[0,0],[0,0]] , [[0,0][0,0]] ]
        grid[1][1][1] = 5 : [ [[0,0],[0,0]] , [[0,0][0,5]] ]
        """
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
        """
        Prints the grid in a standard cartesian layout with 0,0,0 being the furthest
        bottom-left tile. Each z level is printed seperatly with the top being 0 and the
        bottom being the highest z level. I use the grid[x][y][z] notation established 
        in create_3d_grid() to print in this manner. 
        Ex.2x2x2 grid:
        00
        00
        --
        00
        00
        Since we want to print starting at the top left the first coordinate is always
        [0][num_columns-1][0] and then moves right in the x axis to [1][num_columns-1][0].
        We then decrease the y by 1 to move to the next row down and repeat above for the x.
        Finally we start all over after finishing the 1st z level and continue to the next
        by incrementing z by 1.
        """
        if self.z_length == 1:
            x = 0
            y = self.y_length - 1
            for i in range(self.y_length): 
                for j in range(self.x_length):
                    print(self.grid[x][y], end="") #start here
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
                        print(self.grid[x][y][z], end="") #start here
                        x += 1
                    print()
                    y -= 1
                    x = 0        
                print()
                x = 0
                y = self.y_length - 1
                z +=1

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
    def __init__(self,location):
        self.location = location
    def __repr__(self):
        return "@"
    def move(self,direction):
        if direction == 4:
            pass

def update(grid):
    os.system("cls")
    grid.plot()

def main():
    grid = Grid(5,5)
    grid.grid[2][2].occupants.append(Character((2,2)))
    update(grid)
    #time.sleep(2)

    #running = True
    #while running:
        #update()
if __name__ == '__main__':
    main()



