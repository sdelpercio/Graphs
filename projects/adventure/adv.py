from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Graph:
    def __init__(self):
        self.rooms = {}
        
    def add_room(self, room.id):
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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

## WRITE ALGORITHM TO FILL TRAVERSAL PATH WITH DIRECTIONS TO ALL ROOMS
traversal_path = []

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

# start a dictionary
# start a Queue
# add starting room to queue

# enter a loop until queue is empty
## dequeue latest room node
## set dequeued room to current

## get neighbors for current room
## check node for key,value (direction,status)
## if any status == '?', 
### get that room's object/id
### set current_node's value for that direction
### add that next room to the queue



# 2. Enter a while loop 

# Choose a random direction
# Travel down that direction until there are no more exits unvisited
# Use Breadth First Search to retrace steps until a room with unvisited exits is found
# once a room is found, convert those rooms to cardinal directions, add to traversal_path

# repeat until BFS returns an empty array


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
