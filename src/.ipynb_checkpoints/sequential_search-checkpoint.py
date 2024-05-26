from utilities import  dominates_cord , revalidate_skyline
import numpy as np
def sequential_scan_nearest_neighbor(query_point, data_points):
    """
    Find the nearest neighbor to a query point using the sequential scan method.
    
    Args:
    query_point (array): The query point coordinates.
    data_points (list of arrays): List of coordinates for each point in the dataset.
    
    Returns:
    tuple: The nearest point coordinates and the distance to it.
    """
    nearest_point = None
    min_distance = float('inf')  # Initialize with infinity
    #for q_point in query_point:
        
    for point in data_points:
        distance = euclidean_distance(query_point, point)
        if distance < min_distance:
            min_distance = distance
            nearest_point = point
        #print("query point", q_point, " nearest point ",nearest_point, "min distance", min_distance)        
    return nearest_point, min_distance ,query_point



def sequential_task_two(data) -> None :
    skyline_result = []
    #loop through every point in the data
    for x in range(0 , len(data)):
        is_dominated = False
        #compare every point with other points
        for y in range(0 , len(data)):
            #if the points are same point skip
            if x == y :
                continue
            #checking for dominance and if we find any point that dominates out current point
            #we break out of the loop and not check further to safe some time
            if dominates_cord(data[x], data[y]):
                is_dominated = True
                break
        #if we can find any point in the skyline that dominates our point the the whole data set then we found a skyline point
        if not is_dominated:
            result = {'id' : data[x]['id'] , 'x' : data[x]['x'] , 'y' : data[x]['y']}
            skyline_result.append(result)
    #this is just to keep the response well formatted and sorted by id    
    sorted_result = sorted(skyline_result , key = lambda x:x['id'])
   
    return sorted_result

def sequential_task_two_optimized(data : list) -> None :
    skyline_result = []
    #sorting the data based on x so finding the skyline point would be much easier at least the first point on x axis would be a skyline point
    sorted_data = sorted(data , key= lambda x:x['x']) 

    #looping over all the records
    for point in sorted_data:
        is_dominated = False
        #validating every point with skyline points to ensure that no possible skyline points found dominates the current point 
        for skyline_point in skyline_result:
            if dominates_cord(point, skyline_point):
                is_dominated = True
                break
        #if no point dominates the point we add the point to the skyline points
        if not is_dominated:
            result = {'id' : point['id'] , 'x' : point['x'] , 'y' : point['y']}
            skyline_result.append(result)

    #Since it is possible to wronly label a point found first as a skyline point there is need to Revalidate 
    #Skyline point to ensure that any dorminated data is removed
    valid_skyline_points = revalidate_skyline(skyline_result)
    return valid_skyline_points

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in n-dimensional space.
    
    Args:
    point1 (array): Coordinates of the first point.
    point2 (array): Coordinates of the second point.
    
    Returns:
    float: The Euclidean distance between the two points.
    """
    point1_array = np.array([float(point1['x']), float(point1['y'])])
    point2_array = np.array([float(point2['x']), float(point2['y'])])

    # Calculate the Euclidean distance
    distance = np.sqrt(np.sum((point1_array - point2_array) ** 2))
    return distance  
