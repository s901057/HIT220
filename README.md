
NOTE
crocData.csv, CrocDataLatest.xlsx are hardcoded into C:/temp/ folder

pyAssign3_SectionA_Part1_Next_site.py
#SOLUTION WILL DETERMINE THE PATH FOR THE MAXIMUM # of SIGHTINGS!
# sightingsCount=sightingsCount+ {array of sightings})

 

pyASSIGNMENT3_PARTB_SECTION_B_CROC_BARRIER.py
#SOLUTION WILL DETERMINE THE PATH FOR THE MAXIMUM SIGHTINGS ON LAND for Barrier planning purposes!
#I understand crocs can swim around water based barriers!
#LandTravelCalc is the sightings on land counter!
#Answer is a Dataframe which should show LandTravelCalc ordered highest to lowest for Path Selection!

pyAssignment3PartB_C_MinTime.py
#SOLUTION WILL DETERMINE  MINIMUM RANGER TRAVEL TIME!
# BRUTE FORCE VERSION WILL DETERMINE ACROSS ALL PATHS!


pyAssignment3PartB_C_Point_no_pass.py
#SOLUTION WILL DETERMINE THE PATH FOR THE MAXIMUM # of CROC DENSITY!
#WHICH IS CALCULATED  BY DIVIDING DISTANCE BY QTY OF CROC SIGHTINGS!
#            densityCroc=densityCroc +int(currentDistanceForThisNode)/int(currentSightingValue)
#Path 1 to 32 has highest croc density

pyAssignmentPartc_PartB_CYCLE.py
# USING A DFS to roughly detect if the graph has a CYCLE!
# Does not tell me where the cycle is but by manually removing each node I could determine most of the cycles



PYcyclegraph_boyermoore_aTTEMPT.py
#This is a extra solution to detect CYCLES where I look for last 5 nodes in the path in the total path pattern 
 to locate a reoccurindg cycle!
#I could not get the boyer moore lgorithm to work so I resorted to a simple FIND text function!
# This solution is built on the other assignment question solutions so has dataframe and counting code!
#Will HALT Execution when it determines a repeated CYCLE path!



pyAssignmentPartC_A_Route_exists.py
#SOLUTION WILL DETERMINE IF A  PATH EXISTS! Does not take into account CYCLES
#def Route_exists(graph, source, destination):
#    path = [destination]
#    bPathFound= False
#    distance_table = build_distance_table(graph, source)
#    previous_vertex = distance_table[destination][1]
#    while previous_vertex is not None and previous_vertex is not source:
#        path = [previous_vertex] + path
#        markVisited(previous_vertex)
#        previous_vertex = distance_table[previous_vertex][1]

    # the finale!
#    if previous_vertex is None:
#        return False
#
#    else:
#        return True



pyAssignmentC_SectionC_Scheduled_Points.py
#SOLUTION WILL list paths between 2 points with a CYCLE FREE dataset!
#CYCLE FREE dataset was determined by DFS in pyAssignmentPartc_PartB_CYCLE.py
