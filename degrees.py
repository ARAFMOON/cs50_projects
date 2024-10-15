import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # Keep track of number of states explored
    num_explored = 0
   
    # Initialize frontier to just the starting position
    start = Node(state=source, parent=None, action=None)
    frontier = StackFrontier()
    frontier.add(start)
        
        # Initialize an empty explored set
    explored = set()
            
        # Keep looping until solution found
    while True:

                # If nothing left in frontier, then no path
                 if frontier.empty():
                    raise Exception("no solution")
   
                # Choose a node from the frontier                                                                                                                                                                                                                                                                                       node = frontier.remove()
                    num_explored += 1

                # Mark node as explored
    num_explored.add(node.state)

    # Add neighbors to frontier
    for action, state in neighbors_for_person(node.state):
                        if not frontier.contains_state(person_id) and person_id not in explored:
                            child = Node(state=person_id, parent=node, action=movie_id)

                            # If node is the goal, then we have a solution
                        if child.state == target:
                            movies = []
                            people = []
                            solution = []
                            while child.parent is not None:
                                movies.append(child.action)
                                people.append(child.state)
                                child = child.parent
                            movies.reverse()
                            people.reverse()
                            x = zip(movies,people)
                            for movie, person in x:
                                solution.append((movie,person))
                            return solution   
                        
                        
                        frontier.add(child)



def person_id_for_name(name):
   """
   Returns the TMDB id for a person's name
 