from math import sin, cos, sqrt, atan2, radians

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

def calculate_time_difference(time1, time2):
    difference = time2 - time1
    timer_diff = (difference / time2) * 100
    return timer_diff

def get_distance_km(lat_one , lon_one , lat_two , lon_two):
    R = 6373.0

    lat1 = radians(lat_one)
    lon1 = radians(lon_one)
    lat2 = radians(lat_two)
    lon2 = radians(lon_two)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
