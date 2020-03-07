from algorithms.heap_sort import heap_sort
from algorithms.graph import Graph
from collections import defaultdict

def main():
    print "Following is Heap Sort"
    array = [1,4,7,9,22,44,54,7,8,999,0,33,4,534566,3,5,7,7]
    heap_sort(array)
    print (array)
    
    
    # Driver code 
    # Create a graph given in the above diagram 
    g = Graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    
    print "Following is Depth First Traversal"
    g.DFS() 

if __name__ == '__main__':
    main()