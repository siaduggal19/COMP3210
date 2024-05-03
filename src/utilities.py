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

def write_to_file(file_path , data):
    with open(file_path , 'w') as file:
        file.writelines(data)
        file.close()




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
