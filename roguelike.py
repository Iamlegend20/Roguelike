import os
import time
from pynput import keyboard
class Grid:

    def __init__(self, x_length, y_length, z_length):
        self.x_length = x_length
        self.y_length = y_length 
        self.z_length = z_length
        self.grid = self.create_grid()

    def create_grid(self):
        grid=[]
        for i in range(self.x_length):
            grid.append([])
            for j in range(self.y_length):
                grid[i].append([])
                for k in range(self.z_length):
                    grid[i][j].append(Tile())
        return grid        
    
    def plot(self):    
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
            return repr(self.occupants[0]) #update for multiple occupants with id system
        if self.is_blocked:
            return "#"
        elif not self.is_blocked:
            return "."

class Character:

    def __init__(self, x_pos, y_pos, z_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
    
    def __repr__(self):
        return "@"

    def spawn(self, grid):
        grid.grid[self.x_pos][self.y_pos][self.z_pos].occupants.append(self)

    def move(self, grid, direction):
        current_tile = grid.grid[self.x_pos][self.y_pos][self.z_pos].occupants
        
        if direction == '<100>':
            grid.grid[self.x_pos-1][self.y_pos][self.z_pos].occupants.append(self)
            self.x_pos -= 1
        elif direction == '<102>':
            grid.grid[self.x_pos+1][self.y_pos][self.z_pos].occupants.append(self)
            self.x_pos += 1
        elif direction == '<104>':
            grid.grid[self.x_pos][self.y_pos+1][self.z_pos].occupants.append(self)
            self.y_pos += 1
        elif direction == '<98>':
            grid.grid[self.x_pos][self.y_pos-1][self.z_pos].occupants.append(self)
            self.y_pos -= 1
        elif direction == '<103>':
            grid.grid[self.x_pos-1][self.y_pos+1][self.z_pos].occupants.append(self)
            self.x_pos -= 1
            self.y_pos += 1
        elif direction == '<105>':
            grid.grid[self.x_pos+1][self.y_pos+1][self.z_pos].occupants.append(self)
            self.x_pos += 1
            self.y_pos += 1
        elif direction == '<97>':
            grid.grid[self.x_pos-1][self.y_pos-1][self.z_pos].occupants.append(self)
            self.x_pos -= 1
            self.y_pos -= 1
        elif direction == '<99>':
            grid.grid[self.x_pos+1][self.y_pos-1][self.z_pos].occupants.append(self)
            self.x_pos += 1
            self.y_pos -= 1
        elif direction == '<101>':
            return     

        for occupant in current_tile:
            if occupant == self:
                current_tile.remove(self)
                break   

def validate_input(player_input):
    global key_pressed
    accepted_input = ("<97>","<98>","<99>","<100>","<101>","<102>","<103>","<104>","<105>")
    if player_input not in accepted_input:
        return False

def on_press(key):
    global player_input
    global key_pressed
    player_input = str(key)
    key_pressed = True

player_input = None
key_pressed = False
def main():
    global player_input
    global key_pressed
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    grid = Grid(60,20,1)
    player = Character(2,2,0)
    player.spawn(grid)
    grid.update()
    
    while True:
        while key_pressed:
            if validate_input(player_input) == False : break
            player.move(grid, direction=player_input)
            grid.update()
            key_pressed = False

if __name__ == '__main__':
    main()



