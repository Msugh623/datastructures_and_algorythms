def bin_search(list,target):
    print('bin_search: finding %s in list...'%target)
    first=0
    last=len(list)-1
    trys=0
    # if list[first]==target:
    #         print('bin_search: %s times'%trys)
    #         return first
    while first<=last:
        trys+=1
        mid=(first+last)//2 
        
        if list[mid]==target:
            print('bin_search: %s times'%trys)
            return mid
        elif list[mid]<target:
            first=mid+1
        else:
            last=mid-1
    print('bin_search: tried %s times'%trys)
    return None

print('item found at index: %s' % bin_search(list(range(1,100)),1))