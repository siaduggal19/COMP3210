from sequential_search import sequential_scan_nearest_neighbor , sequential_task_two  
from bf_search import bf_search , bf_search_divide_conquer
from bbs_search import bbs_search , bbs_search_divide_conquer
from utilities import load_data,load_query_points, Save_File_Location , calculate_time_difference,divide_dataset
from tree import RTree
import asyncio
import time
import tqdm

if __name__ == "__main__":
    #Load Task1 Data
    data_points = load_data("data/parking_dataset.txt")
    print("data loaded")
    
    # Load query points
    query_points = load_query_points("data/query_points.txt")
    print("Query points loaded.")
    

#sequential search
print("start sequential search")
start_time= time.time()
result2=[]
for q_point in tqdm.tqdm(query_points):
    nearest_point, distance = sequential_scan_nearest_neighbor(q_point, data_points)
    # print("he",nearest_point)
    result2.append(f"id={nearest_point['id']}, x={nearest_point['x']}, y={nearest_point['y']}, query id ={q_point['id']} ")
    
seq_time= time.time()- start_time
average_time = seq_time / len(query_points)
print("Sequential search time: %.4fsec" % seq_time)
output_file = "output_files/task1_sequential_search.txt"
with open(output_file, 'w') as file:
    for result in result2:
        file.write(result + '\n')
    file.write(f"Total running time: {seq_time:.2f} seconds\n")
    file.write(f"Average time per query: {average_time:.4f} seconds\n")   
    

    #create r-tree
    rtree = RTree()  
    print("Building r-tree for bf search")
    for point in tqdm.tqdm(data_points):
        #rtree.insert(rtree.root, {'x': point['x'], 'y': point['y']})
        rtree.insert(rtree.root, {'id': point['id'], 'x': point['x'], 'y': point['y']})
        
    #bf_search
    

    start_time = time.time()
    results = []
    for query in tqdm.tqdm(query_points):
        nearest,dist = bf_search(rtree, {'x': query['x'], 'y': query['y']})
        results.append(f"id={nearest['id']}, x={nearest['x']}, y={nearest['y']}, for query {query['id']}")

    total_time = time.time() - start_time
    average_time = total_time / len(query_points)
    print(f"Total running time: {total_time:.2f} seconds")
    print(f"Average time per query: {average_time:.4f} seconds")

    #Save_File_Location("output_files/task1_BF_search.txt" , results , bf_search , total_time , "")
    #print("succesfully completed bestfirst search")
    output_file = "output_files/task1_BF_search.txt"
    with open(output_file, 'w') as file:
        for result in results:
            file.write(result + '\n')
        file.write(f"Total running time: {total_time:.2f} seconds\n")
        file.write(f"Average time per query: {average_time:.4f} seconds\n")

    print("Results saved to", output_file)
    
    #create two r-trees based on selected criteria
    subspace1, subspace2 = divide_dataset(data_points, dimension='x')
    rtree1 = RTree()
    rtree2 = RTree()
    print("building two r-tree for bf divide and conquer")
    for point in tqdm.tqdm(subspace1):
        rtree1.insert(rtree1.root, point)

    for point in tqdm.tqdm(subspace2):
        rtree2.insert(rtree2.root, point)
    #bf_divide_conquer

    start_time = time.time()
    result2=[]
    for query in query_points:
        
        final_nearest,dist=bf_search_divide_conquer(rtree1 , rtree2, query)
            
        result2.append(f"id={final_nearest['id']}, x={final_nearest['x']}, y={final_nearest['y']}, for query {query['id']}")
        
            
    total_time = time.time() - start_time
    average_time = total_time / len(query_points)
    print(f"Total running time: {total_time:.2f} seconds")
    print(f"Average time per query: {average_time:.4f} seconds")

    output_file = "output_files/task1_bf_search_with_Divide_conquer.txt"
    with open(output_file, 'w') as file:
        for result in result2:
            file.write(result + '\n')
        file.write(f"Total running time: {total_time:.2f} seconds\n")
        file.write(f"Average time per query: {average_time:.4f} seconds\n")

    print("End of BF Seacrh")

    #task 2 load data
    print("start skyline search")
    task2_data = load_data('data/city1.txt')
    start = time.time()
    
    sequential_resp = tqdm.tqdm(sequential_task_two(task2_data))
    sequential_total_runtime = time.time() - start
    
    Save_File_Location('output_files/task_2_sequential.txt' , sequential_resp , "Sequential BBS Search" , sequential_total_runtime , "")
   
    print("Squential Skyline Total runtime in sec - " , sequential_total_runtime)

    rtree = RTree()
    print("build R-Tree for BBS: ")
    
    
    for point in tqdm.tqdm(task2_data):
        rtree.insert(rtree.root, point)
    
    start = time.time()
    bbs_resp = bbs_search(rtree.root)
    bbs_total_runtime = time.time() - start
    comment = f"BBS search is {calculate_time_difference(bbs_total_runtime , sequential_total_runtime )} percent faster than sequential search"

    Save_File_Location('output_files/task_2_bbs.txt' , bbs_resp , "BBS Search" , bbs_total_runtime , comment)

    print("BBS Skyline Total runtime in sec - " , bbs_total_runtime)
 
    #create two r-trees based on selected criteria
    print("Divide and conquer bbs search")
    rtree_dq_one = RTree()
    rtree_dq_two = RTree()
    print("build Two R-Tree: ")
    for point in tqdm.tqdm(task2_data):
        #Trying to split data into two equal propotion as much as possible
        if point['x'] <= 415 :
            rtree_dq_one.insert(rtree_dq_one.root, point)
        else:
            rtree_dq_two.insert(rtree_dq_two.root, point)
    start = time.time()
    bbs_dq_resp = asyncio.run( bbs_search_divide_conquer(rtree_dq_one , rtree_dq_two))
    bbs_dq_total_runtime = time.time() - start
    comment = f"Divide and conquer BBS search is {calculate_time_difference(bbs_dq_total_runtime ,bbs_total_runtime)} percent faster than normal bbs search"
    
    Save_File_Location('output_files/task_2_bbs_with_divide_and_conquer.txt' , bbs_dq_resp , "BBS Search" , bbs_dq_total_runtime , comment)
    
    print("Divide and conquer BBS Skyline Total runtime in sec - " , bbs_dq_total_runtime)
