
import heapq
import math
import numpy as np
from utilities import euclidean_distance
def bf_search(rtree , query_point):
    priority_queue = []
    heapq.heappush(priority_queue, (0, rtree.root))
    min_distance = float('inf')
    nearest_point = None
    min_distance = float('inf')


    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        if node.is_leaf():
            
            for data_point in node.data_points:
                #point_distance = math.sqrt((data_point['x'] - query_point['x']) ** 2 + (data_point['y'] - query_point['y']) ** 2)
                point_distance = euclidean_distance(data_point , query_point)
                if point_distance < min_distance:
                    min_distance = point_distance
                    nearest_point = data_point

        else:
            for child in node.child_nodes:
                # Proper calculation of MBR distance should be implemented here
                
                #child_distance = 0
                #heapq.heappush(priority_queue, (child_distance, child))
                #distance = heuristic(child, query_point)
                distance =point_to_mbr_distance(query_point, child)
                if distance < min_distance:
                    heapq.heappush(priority_queue, (distance, child))
    return nearest_point, min_distance

def heuristic(node, target):
    # Define a heuristic functiheuristicon. This is an example using Euclidean distance.
    # Modify as needed for your specific use case.
    x_center = (node.MBR['x1'] + node.MBR['x2']) / 2
    
    y_center = (node.MBR['y1'] + node.MBR['y2']) / 2
    
    return math.sqrt((x_center - target['x'])**2 + (y_center - target['y'])**2) 

"""def divide_dataset(data_points, dimension='x'):
    # Sort data points based on the chosen dimension
    sorted_points = sorted(data_points, key=lambda k: k[dimension])
    # Divide into two subspaces
    mid_index = len(sorted_points) // 2
    return sorted_points[:mid_index], sorted_points[mid_index:]"""

def bf_search_divide_conquer(tree_one , tree_two , query):
    
    nearest1, dist1 = bf_search(tree_one, query)
    nearest2, dist2 = bf_search(tree_two, query)

    # Determine the closer of the two nearest neighbors
    if dist1 <= dist2:
        final_nearest = nearest1
        final_distance = dist1
    else:
        final_nearest = nearest2
        final_distance = dist2

    return final_nearest,final_distance

    print(f"Final nearest for query {query['id']}: id={final_nearest['id']}, x={final_nearest['x']}, y={final_nearest['y']}, distance={final_distance}")

def point_to_mbr_distance(query, MBR):
    """
    Calculate the shortest distance from a query point to the MBR.

    Args:
    query (dict): The query point with 'x' and 'y' coordinates.
    MBR (dict): The Minimum Bounding Rectangle with 'min_x', 'max_x', 'min_y', 'max_y' coordinates.

    Returns:
    float: The shortest distance from the query point to the MBR.
    """
    qx, qy = query['x'], query['y']
    min_x, max_x, min_y, max_y = MBR.MBR['x1'], MBR.MBR['x2'], MBR.MBR['y1'], MBR.MBR['y2']
    
    # Calculate distance to the nearest edge or corner
    if qx < min_x:
        if qy < min_y:
            # Bottom-left corner
            return np.sqrt((min_x - qx) ** 2 + (min_y - qy) ** 2)
        elif qy > max_y:
            # Top-left corner
            return np.sqrt((min_x - qx) ** 2 + (qy - max_y) ** 2)
        else:
            # Left edge
            return min_x - qx
    elif qx > max_x:
        if qy < min_y:
            # Bottom-right corner
            return np.sqrt((qx - max_x) ** 2 + (min_y - qy) ** 2)
        elif qy > max_y:
            # Top-right corner
            return np.sqrt((qx - max_x) ** 2 + (qy - max_y) ** 2)
        else:
            # Right edge
            return qx - max_x
    else:
        if qy < min_y:
            # Bottom edge
            return min_y - qy
        elif qy > max_y:
            # Top edge
            return qy - max_y
        else:
            # Inside the MBR
            return 0.0

# Example usage
query = {'x': 5, 'y': 5}
MBR = {'min_x': 2, 'max_x': 8, 'min_y': 3, 'max_y': 7}

#distance = point_to_mbr_distance(query, MBR)
#print("Distance from query point to MBR:", distance)
