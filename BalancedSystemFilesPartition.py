#!/bin/env python3

def mostBalancedPartition(parent, files_size):
    n = len(parent)     
    total_sum = [0]*n # a list which will contain the sizes of all directories respectively
    """
    the for loop is used to go through the parent list.
    the while loop will stop when we are at the top of the tree ( temp == -1)
    this way we will increment the values of the total_sum list with the file sizes of each folder until we reach the root folder.
    Example: 
    Parent = [-1,0,0,1,1,2]
    files_size = [1,2,2,1,1,1]
    running the loop will give us the following values:
    total_sum[0] = 1 + 2 + 2 + 1 + 1 + 1 = 8
    total_sum[1] = 2 + 1 + 1 = 4
    total_sum[2] = 2 + 1 = 3
    total_sum[3] = 1
    total_sum[4] = 1
    total_sum[5] = 1
    total_sum = [8,4,3,1,1,1]
    """
    for i in range(0,n): 
        temp = i
        while(temp != -1):
            total_sum[temp] += files_size[i]
            temp = parent[temp]
    """
    we now compute the absolute difference absolute_diff between the first two consecutive 
    folders. if A is the size of the parent folder and B is the size of the child folder
    then the total_sum value of the parent folder will be 'A + B' and the total_sum value of the 
    child folder will be B. So the difference 'A - B' can be computed by: 
    total_sum[index of the parent] - 2 * total_sum[index of the child] = A + B - 2 * B = A - B

    """
    absolute_diff = abs(total_sum[0] - 2 * total_sum[1])
    """
    now we go through the list computing absolute_diff of each child folder with the root 
    until we find the smallest absoute value.
    """ 
    if absolute_diff == 0:
        return 0
    for i in range(2,n):
        if abs(total_sum[0] - 2 * total_sum[i]) == 0:
            return 0
        elif abs(total_sum[0] - 2 * total_sum[i]) < absolute_diff:
            absolute_diff = abs(total_sum[0] - 2 * total_sum[i])
    return absolute_diff 

if __name__ == "__main__":
    parent = [-1,0,0,1,1,2]
    files_size = [1,2,2,1,1,1]
    print(mostBalancedPartition(parent,files_size))
        

    parent = [-1,0,1,2] 
    files_size = [1,4,3,4] 
    print(mostBalancedPartition(parent,files_size))
 
    parent = [-1,0,0,0] 
    files_size = [10,11,10,10] 
    print(mostBalancedPartition(parent,files_size))

    parent = [ -1, 0, 1, 2, 1, 0, 5, 2, 0, 0 ] 
    files_size = [ 8475, 6038, 8072, 7298, 5363, 9732, 3786, 5521, 8295, 6186 ] 
    print(mostBalancedPartition(parent,files_size))
    

    parent = [ -1, 0, 0, 0, 0, 3, 4, 6, 0, 3 ]
    files_size = [ 298, 2187, 5054, 266, 1989, 6499, 5450, 2205, 5893, 8095 ] 
    print(mostBalancedPartition(parent,files_size))
                                                                              
