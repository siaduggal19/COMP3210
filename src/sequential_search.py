from utilities import load_data, write_to_file , dominates_cord , revalidate_skyline
import time
def sequential_task_one(data , query) -> None :
    pass


def sequential_task_two(data) -> None :
    #sorting the data so finding the skyline point would be much easier
    start = time.time()
    skyline_result = []
    sorted_data = sorted(data , key= lambda x:x['x']) 
    

    
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

    #Revalidate Skyline point to ensure that any dorminated data is removed
    valid_skyline_points = revalidate_skyline(skyline_result)

    return valid_skyline_points
    
