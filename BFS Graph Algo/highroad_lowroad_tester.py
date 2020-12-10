from graph_util import *
from highroad_lowroad import *

tests = ['test1.txt', 'test2.txt', 'exponential_length5.txt', 'exponential_length10.txt', 'exponential_length30.txt', 'plateau.txt', 'four_layers10.txt', 'four_layers50.txt']

def read_input(filename):
    contents = open(filename).read().strip().split('\n')
    num_nodes = int(contents[0])
    num_edges = int(contents[1])
    elevations = {}
    for i in range(num_nodes):
        label, elevation = contents[2+i].strip().split()
        elevations[label] = int(elevation)
    roadmap = graph(elevations.keys())
    for row in contents[num_nodes+2:-2]:
        v, w = row.strip().split()
        roadmap.add_edge(v, w)
    start = contents[-2].strip().split()[0]
    end = contents[-1].strip().split()[0]
    return roadmap, elevations, start, end
    
    
    
def main():
    "Runs each of the test cases"
    for test_name in tests:
        print(test_name)
        roadmap, elevations, start, end = read_input(test_name)
        print("Length:", shortest(roadmap, elevations, start, end))
        print("Count:", num_shortest(roadmap, elevations, start, end))
        print()
    
main()
