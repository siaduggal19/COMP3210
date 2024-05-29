from math import sin, cos, sqrt, atan2, radians
import numpy as np
def load_data(file_path):
    points = []
    with open(file_path) as dataset:
        for data in dataset.readlines():
            splitData = data.split()
            points.append({'id':int(splitData[0].strip()) , 
                           'x':float(splitData[1].strip()) , 
                           'y':float(splitData[2].strip())
                           })
    return points

def load_query_points(file_path):
    """ Load query points from a text file. """
    with open(file_path, 'r') as file:
        queries = [{'id': int(line.split()[0]), 'x': float(line.split()[1]), 'y': float(line.split()[2])} for line in file]
    return queries

def Save_File_Location(path , data , programName , runtime , comment):
    write_data = ""
    point_string = ""
    for point in data:
        point_string += f"id : {point['id']} , x : {point['x']} ,'y': {point['y']} \n"
               
    write_data += f"{programName} Total runtime in sec - {runtime} \n"  
    write_data += "\n"
    write_data += point_string
    write_data += comment
    write_to_file(path , write_data)


def write_to_file(file_path , data):
    with open(file_path , 'w') as file:
        file.writelines(data)
        file.close()


def revalidate_skyline(skyline):
    new_skyline = []
    
    for x in range(0 , len(skyline)):
        is_dominated = False
        for y in range (0 , len(skyline)):
            if x == y:
                continue
            if dominates_cord(skyline[x] , skyline[y]):
                is_dominated = True
                break  
        if not is_dominated:
            new_skyline.append(skyline[x])

    new_skyline = sorted(new_skyline , key= lambda x:x['id'])
    return new_skyline



def dominates_cord(point1, point2):
    return point1['x'] >= point2['x'] and point1['y'] >= point2['y']

#will return the calculation of the lower part of the mbr
def mbrpriority(node):
    return node.MBR['x1'] + node.MBR['y2']

def calculate_time_difference(time1, time2):
    if time2 == 0:
        return 0 
    difference = time2 - time1
    timer_diff = (difference / time2) * 100
    return timer_diff


    
def divide_dataset(data_points, dimension='x'):
    # Sort data points based on the chosen dimension
    sorted_points = sorted(data_points, key=lambda k: k[dimension])
    # Divide into two subspaces
    mid_index = len(sorted_points) // 2
    return sorted_points[:mid_index], sorted_points[mid_index:]

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