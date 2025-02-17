# %%
# Given a set of activities, along with the starting and finishing time of each activity, find  
# the maximum number of activities performed by a single person assuming that a person  
# can only work on a single activity at a time.
def eff_activities(act):
    act = sorted(act,key =lambda x:x[1])
    lst = [act[0]]
    for i in range(1,len(act)): 
        if lst[-1][1]<act[i][0]: 
            lst.append(act[i])
    return lst

print(eff_activities([(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]))
 
# %%
#6. Write a program to implement inversion count. 


#Naive Approach

def inv_count(arr): 
    c= 0
    for i in range(len(arr)-1): 
        for j in range(i+1,len(arr)): 
            if arr[i]>arr[j]: 
                c+=1
    return c


inv_count([4,3,2,1])


#Merge Sort Approach 


def merge(l_array,r_array):
    sorted_array = [] 
  
    n1 = len(l_array)
    n2 = len(r_array)
    
    i,j=0,0
    c=0
    while i<n1 and j<n2:
        if l_array[i]<r_array[j]: 
            sorted_array.append(l_array[i])
            i+=1
        else:
            sorted_array.append(r_array[j])
            c+=1
            j+=1
    sorted_array.extend(l_array[i::])
    sorted_array.extend(r_array[j::])
    
    print(c)
    return (sorted_array,c)


def merge_sort(arr,left,right):
    if left == right:
        return [arr[left]]

    mid = (left+right)//2
    count = 0 
    
    l=merge_sort(arr,left,mid)
    r=merge_sort(arr,mid+1,right)
    return merge(l,r)

print(merge_sort([4, 3, 2, 1],0,3)[1])

        

