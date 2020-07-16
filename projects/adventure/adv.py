from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from queue import Queue

class Graph:
    def __init__(self):
        self.rooms = {}
        
    def add_room(self, room):
        if room.id not in self.rooms:
            exits = room.get_exits()
            self.rooms[room.id] = {}
            
            for e in exits:
                self.rooms[room.id][e] = '?'
                
    def add_edge(self, r1, r2, direction):
        if direction == 'n':
            self.rooms[r1.id]['n'] = r2.id
            self.rooms[r2.id]['s'] = r1.id
        if direction == 's':
            self.rooms[r1.id]['s'] = r2.id
            self.rooms[r2.id]['n'] = r1.id
        if direction == 'e':
            self.rooms[r1.id]['e'] = r2.id
            self.rooms[r2.id]['w'] = r1.id
        if direction == 'w':
            self.rooms[r1.id]['w'] = r2.id
            self.rooms[r2.id]['e'] = r1.id
        
    def get_neighbors(self, room):
        return self.rooms[room.id].items()


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

## WRITE ALGORITHM TO FILL TRAVERSAL PATH WITH DIRECTIONS TO ALL ROOMS
# Hints:
## map is not a graph, you'll need to create own adjacency list, figure out whats in it
## add exits to value for each room key
## We want a list of directions, with minimum amount of steps
## When you hit a room with no unexplored exits, back track until you find a room with unexplored exits
## NEAREST NODE with unexplored exits (BFS)
## NOdes: Rooms
## Edges: exits to other rooms


# 1. Construct adjacency list
# ex.
## { 000: {'n': 001, 's': 005, 'e': 007, 'w': 003}, ... }
graph = Graph()
for r in world.rooms.values():
    graph.add_room(r)

q = Queue()
q.put(world.starting_room)
# enter a loop until queue is empty
while q.qsize() > 0:
    ## dequeue latest room node
    current_room = q.get()

    ## get neighbors for current room
    exits = graph.get_neighbors(current_room)
    ## check node for key,value (direction,room)
    for d,r in exits:    
        if r == '?':
            ### get that room's object/id
            dif_room = current_room.get_room_in_direction(d)
            ### fill in directions for both dif room and current
            graph.add_edge(current_room, dif_room, d)
            ### add that next room to the queue
            q.put(dif_room)

print(graph.rooms)

# 2. Enter a while loop 
traversal_path = []
visited = set()
prev_room = world.starting_room

while len(visited) < len(graph.rooms.keys()):
    # get exits from current room
    exits = graph.get_neighbors(player.current_room)
    
    # if you are at an end
    if len(exits) == 1:
        pass
        # TODO: retrace steps to unvisited exit using BFS
        # once a room is found, convert those rooms to cardinal directions, add to traversal_path
        # repeat until BFS returns an empty array
    
    else:
        # Choose a random direction
        dir_list = [d for d,r in exits if r != prev_room.id and r not in visited]
        random_dir = dir_list[random.randint(0,len(dir_list) - 1)]
        
        # log movement
        traversal_path.append(random_dir)
        visited.add(player.current_room.id)
        
        # adjust rooms
        prev_room = player.current_room
        player.travel(random_dir)
        
        



# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
