
import heapq
import math

def bf_search(rtree , query_point):
    priority_queue = []
    heapq.heappush(priority_queue, (0, rtree.root))

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)
        
        if node.is_leaf():
            nearest_point = None
            min_distance = float('inf')
            for data_point in node.data_points:
                point_distance = math.sqrt((data_point['x'] - query_point['x']) ** 2 + (data_point['y'] - query_point['y']) ** 2)
                if point_distance < min_distance:
                    min_distance = point_distance
                    nearest_point = data_point
            return nearest_point, min_distance
        else:
            for child in node.child_nodes:
                # Proper calculation of MBR distance should be implemented here
                
                #child_distance = 0
                #heapq.heappush(priority_queue, (child_distance, child))
                distance = heuristic(child, query_point)
                heapq.heappush(priority_queue, (distance, child))


def heuristic(node, target):
    # Define a heuristic function. This is an example using Euclidean distance.
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