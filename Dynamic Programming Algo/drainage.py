# Hasan Mukati
# Algorithms 4102
# Dynamic Programming

# Goal: Using a DP Algo implement backtracking for path length

elevation_map = []  # Input grid
drain_map = []  # grid to keep track of subproblems' solutions
best = []

def backtrack(start_x, start_y):
    """
    After running longest_drain, Backtracking can be used to reconstruct 
    the longest path found using the DP memory (drain_map in this case).
    
    Backtracking will begin from a given location (start_x, start_y).
    We know that drain_map[start_x][start_y] contains the length of
    the longest river that ends at location (start_x, start_y), call this
    value "length". To reconstruct that longest river, we know that the 
    second-from-last location must be adjacent to (start_x, start_y) and
    contain value "length - 1". The third-from-last location must be
    adjacent to the second-from-last location and contain the value
    "length - 2", etc. 
    
    TODO: Implement the function as described above to use drain_map to 
    reconstruct the longest path ending at (start_x, start_y). The
    return value of this function should be the list of elevations in
    order from highest to lowest.
    """
    path = []
    path.append(elevation_map[start_x][start_y])
    x=start_x
    y=start_y
    n = len(drain_map)
    for iteratorr in range (drain_map[start_x][start_y]-1):
        if ((x>0) and (drain_map[x-1][y]==drain_map[x][y]-1)):
            x-=1
        elif ((y>0) and (drain_map[x][y-1]==drain_map[x][y]-1)):
            y-=1
        elif ((y<n-1) and (drain_map[x][y+1]==drain_map[x][y]-1)):
            y+=1
        elif ((x<n-1) and drain_map[x+1][y]==drain_map[x][y]-1):
            x+=1
        
        path.append(elevation_map[x][y])
        
    path.reverse()
    #path = []
    return path

def find_drain(x, y):
    """
    This function will be used to find the longest river that ends at
    location (x,y). This function is where we will be making use of
    the dynamic programming paradigm. Think about how to the value of 
    drain_map[x][y] relates to the drain_map values of its neighbors.
    
    In the opinion of the course staff, this particular function is 
    much easier to implement as "top-down".
    
    TODO: Implement, using dynamic programming, this function that
    will return the length of the longest path through the 
    elevation map that ends at location (x, y). Use drain_map to
    keep track of the solutions to your subproblems.
    """
    n = len(elevation_map)
    if (x<0 or y<0 or x>=n or y>= n): 
        return 0
    if (drain_map[x][y] != -1):  
        return drain_map[x][y] 
    above = -1
    below = -1 
    left = -1 
    right = -1
    
    if ((x>0) and (elevation_map[x][y] < elevation_map[x-1][y])): 
        left = 1 + find_drain(x-1, y) 
        
    if ((y<n-1) and (elevation_map[x][y] < elevation_map[x][y + 1])): 
        above = 1 + find_drain(x, y + 1) 
  
    if ((y>0) and (elevation_map[x][y] < elevation_map[x][y-1])):  
        below = 1 + find_drain(x, y-1) 
  
    if ((x<n-1) and (elevation_map[x][y] < elevation_map[x + 1][y])): 
        right = 1 + find_drain(x + 1, y) 
  
    # If none of the adjacent fours is one greater we will take 1 
    # otherwise we will pick maximum from all the four directions 
    drain_map[x][y] = max(left, max(below, max(above, max(right, 1)))) 
    return drain_map[x][y] 

def longest_drain(grid, backtracking=False):
    """
    Invoke this function to find the longest path. The way this works
    is that it will invoke find_drain on every location in the
    elevation_map to find the longest drain ending there, saving the
    longest seen.
    
    If backtracking is enabled (i.e. the function is invoked with the
    optional parameter "backtracking" assigned the value True), then 
    this function will reconstruct and print the path of the flow as a
    sequence of elevations.
    
    There is nothing for you to implement here.
    """
    global elevation_map, drain_map
    elevation_map = grid
    size = len(elevation_map)
    drain_map = [[-1 for i in range(size)] for j in range(size)]  # initialize drain_map
    longest = -1
    for x in range(size):
        for y in range(size):
            longest = max(longest, find_drain(x, y))  # find longest drain ending at each location, keep the max
    if backtracking:
        for x in range(size):
            for y in range(size):
                if drain_map[x][y] == longest:
                    path = backtrack(x, y)  # if backtracking is enabled, print the sequence of elevations
                    print("Path:", end=" ")
                    for elevation in path:
                        print(elevation, end=" ")
                    print()
                    return longest
    return longest  



