from utilities import load_data, write_to_file , get_distance_km

def sequential_task_one(data , query) -> None :
    pass


def sequential_task_two(data , query) -> None :
    write_data = ""
    for q in query:
        skyline_result = []
        for point in data:
            distance = get_distance_km(q['x'] , q['y'] , point['x'] , point['y'])

            is_dominated = False
            for skyline_point in skyline_result:
                if dominates_meters(distance, skyline_point):
                    is_dominated = True
                    break
            if not is_dominated:
                result = {'id' : point['id'] , 'x' : point['x'] , 'y' : point['y'] , 'km' : distance}
                skyline_result.append(result)
                skyline_result = sorted(skyline_result , key= lambda x:x['km'])
                
        write_data = write_data + f"Query ID - {q['id']} Best point - {skyline_result[0]['id']} with {skyline_result[0]['km']} km \n"
    write_to_file('output_files/task_2_sequential.txt' , write_data)   


def dominates_meters(distance, skyline_data):
    return distance >= skyline_data['km']

def dominates_cord(point1, point2):
    return point1.x >= point2.x and point1.y >= point2.y