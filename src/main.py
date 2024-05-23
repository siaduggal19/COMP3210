from sequential_search import sequential_task_one , sequential_task_two  
from bf_search import bf_search , bf_search_divide_conquer
from bbs_search import bbs_search , bbs_search_divide_conquer , bbs_search
from utilities import load_data, Save_File_Location , calculate_time_difference
from tree import RTree
import asyncio
import time
import tqdm

if __name__ == "__main__":
    query = load_data('data/query_points.txt')
    #Load Task1 Data

    #sequential search

    #create r-tree
    #bf_search
    
    #create two r-trees based on selected criteria
    #bf_divide_conquer


     





    #task 2 load data
    task2_data = load_data('data/city1.txt')
    start = time.time()
    sequential_resp = sequential_task_two(task2_data)
    sequential_total_runtime = time.time() - start
   
    Save_File_Location('output_files/task_2_sequential.txt' , sequential_resp , "Sequential BBS Search" , sequential_total_runtime , "")
   
    print("Squential Skyline Total runtime in sec - " , sequential_total_runtime)

    rtree = RTree()
    print("build R-Tree: ")
    
    
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
        #Trying to split data into two equall propotion as much as possible
        if point['x'] <= 415 :
            rtree_dq_one.insert(rtree_dq_one.root, point)
        else:
            rtree_dq_two.insert(rtree_dq_two.root, point)
    start = time.time()
    bbs_dq_resp = asyncio.run( bbs_search_divide_conquer(rtree_dq_one , rtree_dq_two))
    bbs_dq_total_runtime = time.time() - start
    comment = f"Divide and conquer BBS search is {calculate_time_difference(bbs_dq_total_runtime ,bbs_total_runtime)} percent faster than normal bbs search"
    
    Save_File_Location('output_files/task_2_bbs_with_divide_and_conquer.txt' , bbs_dq_resp , "BBS Search" , bbs_total_runtime , comment)
    
    print("Divide and conquer BBS Skyline Total runtime in sec - " , bbs_dq_total_runtime)
