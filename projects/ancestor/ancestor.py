class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    
class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        
    def get_neighbors(self, vertex):
        return self.vertices[vertex]

    
    
# build a path like we did in search
def build_graph(ancestors):
    graph = Graph()
    for parent,child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
        
    return graph
    

def earliest_ancestor(ancestors, starting_node):
    # Nodes: people
    # Edges: when a child has a parent
    # Search: Depth First
    graph = build_graph(ancestors)
    
    s = Stack()
    visited = set()
    
    s.push([starting_node])
    
    longest_path = [starting_node]
    aged_one = -1
    
    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]
        
        # if path is longer, or path is equal but id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]
        
        if current_node not in visited:
            visited.add(current_node)
            
            parents = graph.get_neighbors(current_node)
            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    
    return aged_one
    
    
    # # keep track of current parents
    # parents = Stack()
    # parents.push([starting_node])
    # # keep track of oldest
    # oldest=[]
    
    # while parents.size() > 0:
    #     # get current node off of stack
    #     current_path = parents.pop()
    #     current_node = current_path[-1]
    #     currrent_parents = []
        
    #     # check if starting node has parents
    #     for parent,child in ancestors:
    #         # if it does, add to parents stack
    #         if child == current_node:
    #             # add to current node's parents
    #             currrent_parents.append(parent)
    #             # add to stack
    #             parents.push(current_path + [parent])
        
    #     # if it doesn't, it is oldest
    #     if not currrent_parents:
    #         # add node to oldest list
    #         oldest.append(current_path)
    
    
    # # if theres only one value, then starting node had no parents
    # if len(oldest[0]) == 1:
    #     return -1
    # else:
    #     ancestry = {}
    #     # build ancestry dictionary, last ancestor = length of path 
    #     for path in oldest:
    #         ancestry[path[-1]] = len(path)
            
    #     # sort by length of path first, then lowest ancestor ID
    #     sorted_ancestry = [v[0] for v in sorted(ancestry.items(), key=lambda kv: (-kv[1], kv[0]))]
    #     return sorted_ancestry[0]
    
    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 9))