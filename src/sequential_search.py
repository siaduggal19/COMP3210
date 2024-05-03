from utilities import load_data, write_to_file , get_distance_km
import time
def sequential_task_one(data , query) -> None :
    pass


def sequential_task_two(data) -> None :
    #sorting the data so finding the skyline point would be much easier
    start = time.time()
    skyline_result = []
    sorted_data = sorted(data , key= lambda x:x['x']) 
    write_data = ""
    point_string = ""
    write_data += "-------Sequential Skyline Search---------------\n"

    
    skyline_result = []
    for point in sorted_data:
        is_dominated = False
        for skyline_point in skyline_result:
            if dominates_cord(point, skyline_point):
                is_dominated = True
                break
        if not is_dominated:
            result = {'id' : point['id'] , 'x' : point['x'] , 'y' : point['y']}
            skyline_result.append(result)
            point_string += f"id : {point['id']} , x : {point['x']} ,'y': {point['y']} \n"
    total_runtime = time.time() - start    
    write_data += f"Squential Skyline Total runtime in sec - {total_runtime} \n"  
    write_data += "\n"
    write_data += point_string
    write_to_file('output_files/task_2_sequential.txt' , write_data)   


def dominates_meters(distance, skyline_data):
    return distance >= skyline_data['km']

def dominates_cord(point1, point2):
    return point1['x'] >= point2['x'] and point1['y'] >= point2['y']