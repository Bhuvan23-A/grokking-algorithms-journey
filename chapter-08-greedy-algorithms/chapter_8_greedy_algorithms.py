'''
8.1
Greedy strategy:- Of all the boxes,pick the with the biggest size
and put it in the truck, repeat this process until you fill the truck 
or there is no more space in the truck to put a box.

The greedy solution will not give optimal soln, there might be a way 
where not the biggest box but most boxes can be filled in the truck with
minimal waste in space.

8.2
Greedy Strategy:- Pick the activity with the highest point value 
that you can do in the remaining time, repeat this until time is over or 
there is no activity you can do in the remaining time.

Greedy solution will not give u optimal solution, bcoz there might 
be a way where you can do to multiple tasks in smaller or same time.
'''

#Approximation Algo for Set Covering Problem 
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


def my_set_covering(states, stations):
    final_stations = set()
    while states:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states & states_for_station
            if len(covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = covered
        if best_station is not None:
            states -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
        else:
            return None
    return final_stations

print(my_set_covering(states_needed, stations))

'''
8.3.No. In Quicksort you select a pivot which is either the left most or middle element not the best element
8.4.Yes. In BFS,you choose the path which has smallest weight
8.5.Yes. In Dijkstra's algo also you choose the smallest path


8.6.Yes.This can be restated as travelling salesman prblm, so this is definitely 
a NP Complete problem.

8.7.Yes.This can be restated as set covering problem, so this is definitely a 
NP Complete problem.

8.8.Yes.This can be restated as set covering problem, so this is definitely a 
NP Complete problem.You have to calculate all combinations of colors n states.

'''

