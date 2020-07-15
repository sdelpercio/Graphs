import random
from queue import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        
    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        ## use num_users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        ### Example:
        # 5 users
        # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
        ## make a list with all possible friendships
        ## since friends are mutual, we dont need copies for each friend
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)
        
        ## shuffle the list
        self.fisher_yates_shuffle(friendships)
        
        ## Take as many relationships as we need
        total_friendships = num_users * avg_friendships
        
        random_friendships = friendships[:total_friendships//2]        
        
        # add to self.friendships
        for frienship in random_friendships:
            self.add_friendship(frienship[0], frienship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # key = visited user, value = path
        # !!!! IMPLEMENT ME
        # ex.
        # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        # to
        #{1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
        
        # start queue, add starting id and path to queue
        q = Queue()
        path = [user_id]
        q.put(path)
        
        # go through all possible connections
        while q.qsize() > 0:
        ## pop off first in queue
            current_path = q.get()
        ## get last node in path (current node)
            current_node = current_path[-1]
        
        ## check to see if the current node has an entry in visited dictionary
            if current_node not in visited:
            ### add the current node with it's path to visited
                visited[current_node] = current_path
            ### go through that node's relationships, add their path to queue
                friends = self.friendships[current_node]
                for friend in friends:
                    q.put(current_path + [friend])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(30, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('')
    print(connections)
