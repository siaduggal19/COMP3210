from sequential_search import sequential_task_one , sequential_task_two  
from bf_search import bf_search , bf_search_divide_conquer
from bbs_search import bbs_search , bbs_search_divide_conquer
from utilities import load_data, write_to_file

import time

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
    sequential_task_two(task2_data , query)
    total_runtime = time.time() - start
    print("Squential Skyline Total runtime in sec - " , total_runtime)
    print("Squential Skyline Average runtime per query in sec - " , total_runtime/len(query))
    #create r-tree
    #bf_search
    
    #create two r-trees based on selected criteria
    #bf_divide_conquer