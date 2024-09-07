def req_bin_search(list,target):
    """recursive binary search

    Args:
        list (list): list to search
        target (Any): what to search for

    Returns:
        bool: boolean for wether the item exists or not
    """
    first=0
    last=len(list)
    mid=last//2
    if last==first:
        return False
    else:
        if list[mid]==target:
            return True
        elif list[mid]<target:
            new_list=list[mid+1:]
            return req_bin_search(new_list,target)
        else :
            new_list=list[:mid]
            return req_bin_search(new_list,target) 

print('item found index: %s' % req_bin_search(list(range(1,100)),60))