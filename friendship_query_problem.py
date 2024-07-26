import collections

friendships = {
    "alice": ["bob", "charlie"],
    "bob": ["alice", "janice"],
    "charlie": ["alice"],
    "janice": ["bob"]
}

def find_friends(name):
    name = name.lower()
    return friendships.get(name, [])

def common_friends(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    friends1 = set(find_friends(name1))
    friends2 = set(find_friends(name2))
    return list(friends1.intersection(friends2))

def find_connection_degree(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    if name1 not in friendships or name2 not in friendships:
        return -1
    if name1 == name2:
        return 0
    
    visited = set()
    queue = collections.deque([(name1, 0)])
    
    while queue:
        current, degree = queue.popleft()
        
        if current in visited:
            continue
        visited.add(current)
        
        for friend in find_friends(current):
            if friend == name2:
                return degree + 1
            if friend not in visited:
                queue.append((friend, degree + 1))
    
    return -1

def main():
    while True:
        print("\nOptions:")
        print("1. Find friends")
        print("2. Find common friends")
        print("3. Find connection degree")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter the name: ")
            print(f"Friends of {name}: {find_friends(name)}")
        elif choice == '2':
            name1 = input("Enter the first name: ")
            name2 = input("Enter the second name: ")
            print(f"Common friends between {name1} and {name2}: {common_friends(name1, name2)}")
        elif choice == '3':
            name1 = input("Enter the first name: ")
            name2 = input("Enter the second name: ")
            print(f"Connection degree between {name1} and {name2}: {find_connection_degree(name1, name2)}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Time complexity analysis
# find_friends: O(1)
# common_friends: O(F) where F is the number of friends
# find_connection_degree: O(V + E) where V is the number of people and E is the number of connections