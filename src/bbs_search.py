import heapq
import itertools
import asyncio
from concurrent.futures import ThreadPoolExecutor
from utilities import  revalidate_skyline

def bbs_search(root):
    skyline = []
    counter = itertools.count()
    heap = []
    #heapq.heappush(heap, (0, next(counter), root)
    heapq.heappush(heap, (0, next(counter), root))
    
    while heap:
        _,_, node = heapq.heappop(heap)
        
        if node.is_leaf():
            for point in node.data_points:
                if not is_dominated(point, skyline):
                    skyline.append(point)
                    #skyline = [p for p in skyline if not is_dominated(p, [point])]
        else:
            for child in node.child_nodes:                
                if not is_dominated({'x' : child.MBR['x1'],'y' : child.MBR['y1']}, [point for point in skyline]):
                    #heapq.heappush(heap, (child.MBR['x1'], next(counter), child))
                    heapq.heappush(heap, (child.MBR['x1'], next(counter), child))
    return revalidate_skyline(skyline)


async  def bbs_search_divide_conquer(tree_one , tree_two):
  with ThreadPoolExecutor() as executor:
    final_skyline = []

    #since we divided our data based on x <300 be can assume that the data in the first skyline that is lesser than x is fine for x axis
    #we need to compare if we have any point in skyline two where y did better than what we had in skyline one
    '''skyline_one = bbs_search(tree_one.root)
    skyline_two = bbs_search(tree_two.root)
 '''
    task_one = asyncio.create_task(bbs_search_async_caller( executor , tree_one.root))
    task_two = asyncio.create_task(bbs_search_async_caller(executor , tree_two.root))
        
    skyline_one, skyline_two = await asyncio.gather(task_one, task_two)


    for point_one in skyline_two :
        is_dominated = False
        for point_two in skyline_one :
            if point_two['y'] < point_one['y']:
                is_dominated = True
                break
        if not is_dominated:
            skyline_one.append(point_one)  
    return revalidate_skyline(final_skyline)


async def bbs_search_async_caller(executor, tree):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, bbs_search, tree)
    return result

def is_dominated(point, skyline):
    for sp in skyline:
        if sp['x'] <= point['x'] and sp['y'] <= point['y']:
            return True
    return False



