import time
from drainage import *

filenames = ['sample.txt', 'small.txt', 'medium.txt', 'flat.txt', 'long.txt', 'big.txt']


def file_parse(filename):
    f = open(filename)
    rows= f.readline().strip() #first line should indicate number of rows/columns
    rows = int(rows)
    grid = []
    for line in f.readlines():
        row = line.strip().split()
        assert len(row) == rows, "number of items per row does not match number of columns"
        grid.append(list(map(int, row)))
    return grid

def testall():
    # backtracking disabled, timing enabled
    for f in filenames:
        print(f)
        grid = file_parse(f)
        t_before = time.perf_counter()
        longest = longest_drain(grid)
        t_after = time.perf_counter()
        print('Answer: ', longest_drain(grid))
        print('Time: ', t_after-t_before)
        print()
    # backtracking enabled, short cases only
    for f in filenames[:4]:
        print(f)
        grid = file_parse(f)
        longest = longest_drain(grid, True)
        print('Answer: ', longest_drain(grid))
        print()

testall()
        
        
