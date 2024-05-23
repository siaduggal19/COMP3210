import heapq
from concurrent.futures import ThreadPoolExecutor
from utilities import  revalidate_skyline, mbrpriority



def bbs_search(root):
    skyline = []
    #using a default lower mbr of 0
    heap = [(0, root)] 
    #converts the list to an heap
    heapq.heapify(heap)

    #while the heap is not empty
    while heap:
        #this would always take the node with the shortest lower bound and remove the item from the queue
        _, node = heapq.heappop(heap)
        #checking if the node is a leaf node meaning we have traversed the tree all the way down to the leaf
        if node.is_leaf():
            #checking all the data set in the node
            for point in node.data_points:
                if not is_dominated(point, skyline):
                    #add items to the skyline list
                    skyline.append(point)
        else:
            for child in node.child_nodes:
                #checking if the lower bound of the mbr of the child doesn't dominate any point in the skyline
                #if the skyline data doesn't dominate the lowerbound we assume that there might be some skyline point in the MBR  
                #and if the any of the skyline points dominates the lower bound of the rectangle we don't push the child to the sorted queue             
                if not is_dominated({'x' : child.MBR['x1'],'y' : child.MBR['y2']}, [point for point in skyline]):
                    #the lower bound is sumed so we can use that to order the heap
                    lowerBound = mbrpriority(child)
                    heapq.heappush(heap, (lowerBound, child))
    #the revalidation is to ensure that all skyline points are valid skyline and also to sort the skyline
    return revalidate_skyline(skyline)


async  def bbs_search_divide_conquer(tree_one , tree_two):
  with ThreadPoolExecutor() as executor:
    final_skyline = []

    #since we divided our data based on x <300 be can assume that the data in the first skyline that is lesser than x is fine for x axis
    #we need to compare if we have any point in skyline two where y did better than what we had in skyline one
    skyline_one = bbs_search(tree_one.root)
    skyline_two = bbs_search(tree_two.root)
    
    #skyline one ontains minimum on x axis so it is expected that the point from the first skyline should be valid. 
    #what we need to valided is the second skyline to find points in the second skyline that isnot dominated by data is the first skyline
    for point_one in skyline_two :
        is_dominated = False
        for point_two in skyline_one :
            if point_two['y'] < point_one['y']:
                is_dominated = True
                break
        if not is_dominated:
            skyline_one.append(point_one)  
    return revalidate_skyline(skyline_one)

def is_dominated(point, skyline):
    for sp in skyline:
        if sp['x'] <= point['x'] and sp['y'] <= point['y']:
            return True
    return False



