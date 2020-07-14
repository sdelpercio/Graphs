from util import Stack

def earliest_ancestor(ancestors, starting_node):
    
    # keep track of current parents
    parents = Stack()
    parents.push([starting_node])
    # keep track of oldest
    oldest=[]
    
    while parents.size() > 0:
        # get current node off of stack
        current_path = parents.pop()
        current_node = current_path[-1]
        currrent_parents = []
        
        # check if starting node has parents
        for parent,child in ancestors:
            # if it does, add to parents stack
            if child == current_node:
                # add to current node's parents
                currrent_parents.append(parent)
                # add to stack
                parents.push(current_path + [parent])
        
        # if it doesn't, it is oldest
        if not currrent_parents:
            # add node to oldest list
            oldest.append(current_path)
    
    
    # if theres only one value, then starting node had no parents
    if len(oldest[0]) == 1:
        return -1
    else:
        ancestry = {}
        # build ancestry dictionary, last ancestor = length of path 
        for path in oldest:
            ancestry[path[-1]] = len(path)
            
        # sort by length of path first, then lowest ancestor ID
        sorted_ancestry = [v[0] for v in sorted(ancestry.items(), key=lambda kv: (-kv[1], kv[0]))]
        return sorted_ancestry[0]
    
    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 9))