#6.1
# You need only 2 steps

#6.2
# You need to go through cat and then bat will come.

#NOTE IN PYTHON DICT ARE USED TO IMPLEMENT GRAPHS
graph = {}
graph["bhuvan"] = ["sai","adithya","masarapu"]
graph["sai"] = ["rahul","krishna"]
graph["adithya"] = ["chowdary"]
graph["masarapu"] = []
graph["rahul"] = []
graph["krishna"] = []
graph["chowdary"] = []


#Implementing search 
def search(name):
    #Implmenting queue in python 
    from collections import deque
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    def target_person(name):
        return name[-1] == "y"

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if target_person(person) :
                print(f"{person} is the target, We found him")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False
    
search("bhuvan")


#6.3
''' A is unvalid bcoz u cannot eat breakfast until you brush your teeth 
    B is valid 
    C is unvalid bcoz u cannot shower before you wake up
'''

#6.4 
# You can get many variations
''' wake-up --> pack lunch --> brush teeth --> breakfast 
    --> exercise --> shower --> get dressed
'''

#6.5
# A and C are trees bcoz the edge always points to the same direction in the whole graph

#NOTE A TREE IS ALWAYS A GRAPH BUT A GRAPH IS NOT ALWAYS A TREE