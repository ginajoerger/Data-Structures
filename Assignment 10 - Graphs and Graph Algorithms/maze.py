import copy 

def maze_solver(maze):
    ''' return a list of moves showing the correct steps to solve the given maze 
        @maze: list of list, representing the maze

        return: list of correct moves to solve the maze.
    '''
    # To do  
    s = []
    d = []
    
    def find_s(maze):
        rows = -1
                
        for i in maze:
            rows += 1
            columns = -1
            for x in i:
                columns += 1
                if x == 's':
                    return rows, columns
    
    x, y = find_s(maze)
    
    maze[x][y] = '.'
    
    while maze[x][y] != 'e':
        if (maze[x][y + 1] == 'e' or maze[x][y + 1] == '.') and (len(s) == 0 or (x, y + 1) not in s):
            s.append((x, y))
            d.append('right')
            x, y = x, y + 1
    
        elif (maze[x][y - 1] == 'e' or maze[x][y - 1] == '.') and (len(s) == 0 or (x, y - 1) not in s):
            s.append((x, y))
            d.append('left')
            x, y = x, y - 1
        
        elif maze[x + 1][y] == 'e' or maze[x + 1][y] == '.' and (len(s) == 0 or (x + 1, y) not in s):
            s.append((x, y))
            d.append('down')
            x, y = x + 1, y
    
        elif (maze[x - 1][y] == 'e' or maze[x - 1][y] == '.') and (len(s) == 0 or (x - 1, y) not in s):
            d.append('up')
            s.append((x, y))
            x, y = x - 1, y
            
        elif len(s) != 0:    
            my_x, my_y = x, y
            x, y = s.pop()
            d.pop()
            s.insert(0, (my_x, my_y))
    
    return d

def main():
    file = open("maze.txt", 'r') 
    maze = []
    for line in file:       # Read input maze, store into a 2-D list
        maze.append([])
        stripped = line.strip()
        for character in stripped:
            maze[-1].append(character)
    
    print(maze_solver(maze))
    '''
    Result should be something like this, not unique solution though.
    ['right', 'down', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'down', 
    'down', 'down', 'right', 'up', 'right', 'up', 'up', 'right', 'right', 'right', 'down', 
    'down', 'down', 'down', 'right', 'up', 'right', 'up', 'up', 'up', 'right', 'right', 'right']
    '''


#main()
    
