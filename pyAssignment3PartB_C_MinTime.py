import priority_dict
import pandas as pd
import re
from graph import *

#SOLUTION WILL DETERMINE  MINIMUM RANGER TRAVEL TIME!
# BRUTE FORCE VERSION WILL DETERMINE ACROSS ALL PATHS!


# locationList stores node data such as sightings
# this is 38 rows by 3 columns
# [nodeid][sightings][environment]
locationList = {}

# vistedList manages which nodes have been visited
# Requirement: Notify Rangers if they have visited this site/node before
vistedList  = []

# Dataframe crocDF holds data pertaining to each individual Search!
crocDF = pd.DataFrame(columns=['StartNode', 'EndNOde', 'Path', 'Sightings', 'Distance',
                               'CrocSpeed', 'RangerSpeed','RevisitedNodes', 'Notes', 'Cost'])



#cut down on printing as we store to a Dataframe now!


#initialise variables
boolVerbose=False
nodeId=0
x=0
y=0
enviro=0
sightings=0
timeTravel=0


def distanceCal(xnode1, xnode2):
    if xnode1 == 1:  px1, py1 = 3.5, 8.5
    if xnode1 == 2:  px1, py1 = 3.5, 7.5
    if xnode1 == 3:  px1, py1 = 4.5, 7.5
    if xnode1 == 4:  px1, py1 = 5.5, 7.5
    if xnode1 == 5:  px1, py1 = 6, 7.5
    if xnode1 == 6:  px1, py1 = 5.5, 6.5
    if xnode1 == 7:  px1, py1 = 5, 5.5
    if xnode1 == 8:  px1, py1 = 6.5, 5.5
    if xnode1 == 9:  px1, py1 = 7, 6
    if xnode1 == 10:  px1, py1 = 8.5, 6.5
    if xnode1 == 11:  px1, py1 = 9, 9
    if xnode1 == 12:  px1, py1 = 11, 8.5
    if xnode1 == 13:  px1, py1 = 8.5, 6
    if xnode1 == 14:  px1, py1 = 8, 5.5
    if xnode1 == 15:  px1, py1 = 7.5, 4.5
    if xnode1 == 16:  px1, py1 = 7.5, 4
    if xnode1 == 17:  px1, py1 = 8.5, 4
    if xnode1 == 18:  px1, py1 = 9, 4
    if xnode1 == 19:  px1, py1 = 9.2, 2.5
    if xnode1 == 20:  px1, py1 = 10.5, 3
    if xnode1 == 21:  px1, py1 = 11.5, 4.5
    if xnode1 == 22:  px1, py1 = 11, 5
    if xnode1 == 23:  px1, py1 = 10.5, 5.5
    if xnode1 == 24:  px1, py1 = 10.5, 7.5
    if xnode1 == 25:  px1, py1 = 11, 6.5
    if xnode1 == 26:  px1, py1 = 12, 6
    if xnode1 == 27:  px1, py1 = 7, 8.5
    if xnode1 == 28:  px1, py1 = 12.5, 3.5
    if xnode1 == 29:  px1, py1 = 15, 4
    if xnode1 == 30:  px1, py1 = 17.5, 4
    if xnode1 == 31:  px1, py1 = 15.5, 4.5
    if xnode1 == 32:  px1, py1 = 13, 5.5
    if xnode2 == 1:  px2, py2 = 3.5, 8.5
    if xnode2 == 2:  px2, py2 = 3.5, 7.5
    if xnode2 == 3:  px2, py2 = 4.5, 7.5
    if xnode2 == 4:  px2, py2 = 5.5, 7.5
    if xnode2 == 5:  px2, py2 = 6, 7.5
    if xnode2 == 6:  px2, py2 = 5.5, 6.5
    if xnode2 == 7:  px2, py2 = 5, 5.5
    if xnode2 == 8:  px2, py2 = 6.5, 5.5
    if xnode2 == 9:  px2, py2 = 7, 6
    if xnode2 == 10:  px2, py2 = 8.5, 6.5
    if xnode2 == 11:  px2, py2 = 9, 9
    if xnode2 == 12:  px2, py2 = 11, 8.5
    if xnode2 == 13:  px2, py2 = 8.5, 6
    if xnode2 == 14:  px2, py2 = 8, 5.5
    if xnode2 == 15:  px2, py2 = 7.5, 4.5
    if xnode2 == 16:  px2, py2 = 7.5, 4
    if xnode2 == 17:  px2, py2 = 8.5, 4
    if xnode2 == 18:  px2, py2 = 9, 4
    if xnode2 == 19:  px2, py2 = 9.2, 2.5
    if xnode2 == 20:  px2, py2 = 10.5, 3
    if xnode2 == 21:  px2, py2 = 11.5, 4.5
    if xnode2 == 22:  px2, py2 = 11, 5
    if xnode2 == 23:  px2, py2 = 10.5, 5.5
    if xnode2 == 24:  px2, py2 = 10.5, 7.5
    if xnode2 == 25:  px2, py2 = 11, 6.5
    if xnode2 == 26:  px2, py2 = 12, 6
    if xnode2 == 27:  px2, py2 = 7, 8.5
    if xnode2 == 28:  px2, py2 = 12.5, 3.5
    if xnode2 == 29:  px2, py2 = 15, 4
    if xnode2 == 30:  px2, py2 = 17.5, 4
    if xnode2 == 31:  px2, py2 = 15.5, 4.5
    if xnode2 == 32:  px2, py2 = 13, 5.5
    calc_the_dist = abs(px1 - px2) + abs(py1 - py2)
    if calc_the_dist<1:calc_the_dist=1 #failsafe a edge cannot be <1
    return abs(calc_the_dist)




def build_distance_table(graph, source):
    # A dictionary mapping from the vertex number to a tuple of
    # (distance from source, last vertex on path from source)
    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    # The distance to the source from itself is 0
    distance_table[source] = (0, source)

    # Holds mapping of vertex id to distance from source
    # Access the highest priority (lowest distance) item
    # first
    priority_queue = priority_dict.priority_dict()
    priority_queue[source] = 0

    while len(priority_queue.keys()) > 0:
        current_vertex = priority_queue.pop_smallest()

        # The distance of the current node from the source
        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + g.get_edge_weight(current_vertex, neighbor)

            # The last recorded distance of this neighbor from the source
            neighbor_distance = distance_table[neighbor][0]

            # If there is a currently recorded distance from the source and this is
            # greater than the distance of the new path found, update the current
            # distance from the source in the distance table
            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)

                priority_queue[neighbor] = distance

    return distance_table

def Add_sighting( location, water, qtySighted ):
    #effectively update the Array
    if water==true:
        locationList[location, 1, 1] = 1
    if qtySighted>0:
        locationList[location, 0, 1] = qtySighted

def markVisited(nodeid):
    vistedList.append(nodeid)

def haveIVisited(nodeid):
    exist_count=0
    exist_count = vistedList.count(nodeid)

    # checking if node is in Visitelist
    if exist_count > 0:
        return True
    else:
        return False

def Next_site(previous_site ):
    nextNodeHasCrocQuantity=-1
    nextNodeHasCrocQuantity=locationList[previous_site, 0, 1]
    return  nextNodeHasCrocQuantity

def shortest_path(graph, source, destination):
    global crocDF
    global boolVerbose
    travellingspeed=0
    crocspeed=0
    sightingsCount=0
    distanceCalc=0
    costCalc=0
    distance_table = build_distance_table(graph, source)
    timeTravel1=0 #CROC
    timeTravel2=0 #RANGER
    NodesVisited=0 #tracks how many nodes the journey revisited
    speacialComments='' #describes which nodes  the journey revisited
    densityCroc=0
    currentSightingValue = 0
    currentDistanceForThisNode = 0

    path = [destination]
    markVisited(source)
    i=0
    previous_vertex = distance_table[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        markVisited(previous_vertex)
        previous_vertex = distance_table[previous_vertex][1]

        #print("CURRENT node "+ str(locationList[previous_vertex, 0, 0]) +" ="+ str(locationList[ previous_vertex, 0, 1]) +" =" +  str(locationList[ previous_vertex,1, 1]))
        #print("CURRENT node "+ str(locationList[previous_vertex, 0, 0]) +" ="+ str(locationList[ previous_vertex, 0, 1]) +" =" +  str(locationList[ previous_vertex,1, 1]))
        currentSightingValue=int(locationList[ previous_vertex, 0, 1])
        currentDistanceForThisNode=int(distanceCal(previous_vertex, source))
        sightingsCount=sightingsCount+ int(locationList[ previous_vertex, 0, 1])
        if boolVerbose==True:
            print("the next node, which is "+str(previous_vertex)+ " has " + str(Next_site(previous_vertex)) + " historical sigtings ")

        if haveIVisited(previous_vertex)==True:
            NodesVisited=NodesVisited+1
            speacialComments=speacialComments+'Node '+str(locationList[ previous_vertex, 0,0])+ ' revsited;'

        #if on water speed is 16km per hour,land is 6km
        if locationList[previous_vertex, 0, 1]==1:
            crocspeed=16
        else:
            crocspeed=6

        distanceCalc=int(distanceCalc) + int(currentDistanceForThisNode)

        #Requirement 2c distance divied by crocodile speed based on terrain value of the current node!
        timeTravel1 = int(timeTravel1) + int(currentDistanceForThisNode)/int(crocspeed)
        timeTravel2 = int(timeTravel2) + int(currentDistanceForThisNode)/80 #80 kms per hour

        costCalc=int(costCalc)+ 40.48578947*int(timeTravel2) #$40.48 for a $80k Ranger working 38 hours a week!
        costCalc=int(costCalc)+ (int(distanceCalc)/100)*15*2 # $15l at $2 a litere per 100km travelled

        if currentSightingValue>0:
            densityCroc=densityCroc +int(currentDistanceForThisNode)/int(currentSightingValue)



    #the finale!
    if previous_vertex is None:
        print("There is no path from %d to %d" % (source, destination))

#        do not use below!Blank paths will stuff your Minimum KPI numbers system later
#        crocDF = crocDF.append({'StartNode': source, 'EndNOde': destination, 'Path': 'no path', 'Sightings': -1,
#                                'Distance': -1, 'Speed': -1, 'RevisitedNodes': -1,
#                                'Notes': 'There is no path '}, ignore_index=True)

    else:
        path = [source] + path

        if boolVerbose==True:
            print("Shortest path is: ", path)
            print("croc speed   is: ", timeTravel1)
            print("ranger speed   is: ", timeTravel2)
            print("crocodile sightings  on this path is: ", sightingsCount)
            print("speacialComments for this path   is: ", speacialComments)
            print("Revisited Nodes for this path   is: ", NodesVisited)
            print("COST for this path   is: ", costCalc)


    #append the Search data into a Dataframe for Search Comparison purposes
    crocDF=crocDF.append( {'StartNode': source, 'EndNOde': destination, 'Path': path,
                           'Sightings': sightingsCount, 'Distance': distanceCalc,'CrocSpeed': timeTravel1,
                           'RangerSpeed': timeTravel2,
                           'RevisitedNodes': NodesVisited, 'Notes': speacialComments,
                           'cost': costCalc}, ignore_index=True)

g = AdjacencyMatrixGraph(38, directed=False)

# load the croc DATA
df = pd.read_csv(r'C:\temp\CrocData.csv')
#loop through dataframe!
#x and y determine determine distance which has been done manually in a function!!
#
for index, row in df.iterrows():
	# print (index,row["Fee"], row["Courses"])
	nodeId = row['Node']
	x = row['x']
	y =row['y']
	enviro = row['environment']
	sightings =row['number_of_sightings']
	##	#populate the enviro and sightings#

	locationList[nodeId,0,0] = nodeId
	locationList[nodeId,0,1] = sightings
	locationList[nodeId,1,1] = enviro
    #print(" Adding node " + nodeId + "    sightings:" + sightings + "    enviro:" +enviro)


g.add_edge(1, 2, distanceCal(1, 2))
g.add_edge(2, 1, distanceCal(2, 1))
g.add_edge(2, 3, distanceCal(2, 3))
g.add_edge(3, 4, distanceCal(3, 4))

g.add_edge(4, 5, distanceCal(4, 5))
g.add_edge(3, 6, distanceCal(3, 6))
g.add_edge(6, 7, distanceCal(6, 7))
g.add_edge(7, 8, distanceCal(7, 8))
g.add_edge(8, 9, distanceCal(8, 9))

g.add_edge(9, 10, distanceCal(9, 10))
g.add_edge(10, 11, distanceCal(10, 11))
g.add_edge(11, 12, distanceCal(11, 12))
g.add_edge(12, 24, distanceCal(12, 24))
g.add_edge(24, 25, distanceCal(24, 25))
g.add_edge(25, 26, distanceCal(25, 26))
g.add_edge(24, 25, distanceCal(24, 25))
g.add_edge(25, 26, distanceCal(25, 26))
g.add_edge(26, 23, distanceCal(26, 23))
g.add_edge(23, 24, distanceCal(23, 24))

g.add_edge(8, 15, distanceCal(8, 15))
g.add_edge(15, 16, distanceCal(15, 16))
g.add_edge(16, 17, distanceCal(16, 17))
g.add_edge(17, 18, distanceCal(17, 18))
g.add_edge(18, 19, distanceCal(18, 19))
g.add_edge(19, 20, distanceCal(19, 20))
g.add_edge(20, 18, distanceCal(20, 18))

g.add_edge(20, 21, distanceCal(20, 21))
g.add_edge(21, 22, distanceCal(21, 22))
g.add_edge(22, 23, distanceCal(22, 23))

g.add_edge(21, 28, distanceCal(21, 28))
g.add_edge(28, 29, distanceCal(28, 29))
g.add_edge(29, 30, distanceCal(29, 30))
g.add_edge(30, 31, distanceCal(30, 31))
g.add_edge(31, 32, distanceCal(31, 32))
g.add_edge(32, 26, distanceCal(32, 26))

g.add_edge(15, 14, distanceCal(15, 14))
g.add_edge(14, 13, distanceCal(14, 13))
g.add_edge(14, 10, distanceCal(14, 10))

g.add_edge(5, 27, distanceCal(5, 27))
g.add_edge(27, 11, distanceCal(27, 11))


def MinTime(startNode, endNode):
    shortest_path(g, startNode, endNode)
    crocDF.sort_values(by=['RangerSpeed'], ascending=False)
    print("---RANGER SPEED MINIMUM---")
    print(crocDF.to_string())


def MinTimeBruteForce():
    countA = 32
    countB = 32
    while countA > 0 :
        countB = 32
        while countB > 0:
            if countA==countB:
                break
            shortest_path(g, countA, countB)
            if boolVerbose==True:
                print("Dataframe Contents ", crocDF, sep='\n')
            countB=countB-1

        countA=countA-1

    crocDF.sort_values(by=['RangerSpeed'], ascending=False)
    print("---RANGER SPEED MINIMUM---")
    print(crocDF.to_string())

#single Search implementation
MinTime(1, 32)


#exhaustive Search implementation
MinTimeBruteForce()
