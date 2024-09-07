num_list=list(range(10))

def linear_search(num_list ,target): 
    """ returns index of found item

    Args:
        num_list (list): an array
        target (list): an array

    Returns:
        int: index of found items
    """
    global index
    index=None
    for i in range(len(num_list)):
        # print('check', i)
        if i==target:
           index=i  
    return index
        
print(linear_search(num_list,20))