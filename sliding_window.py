
# https://www.geeksforgeeks.org/window-sliding-technique/

# sliding window

### problem 1: finding max sum of the k size window
""" 
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

def maxSum(arr,k):
    # check for window length more than length of list
    if k > len(arr):
        pass

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for index in range(len(arr)-k):
        window_sum = window_sum - arr[index] + arr[index+k]
        max_sum = max(max_sum,window_sum)
    
    return max_sum

print(maxSum(arr, k))
""" 


### problem 2: finding min sum of the k size window
"""
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

def minSum(arr,k):
    # check for window length more than length of list
    if k > len(arr):
        pass

    window_sum = sum(arr[:k])
    min_sum = window_sum

    for index in range(len(arr)-k):
        window_sum = window_sum - arr[index] + arr[index+k]
        min_sum = min(min_sum,window_sum)
    
    return min_sum

print(minSum(arr, k))
""" 

### problem 3: First Negative Number in every Window of Size K

# naive or brute force

from operator import le


arr = [1,2,-1,4,-3,5,-7,8,2,1,8,-5,4]
k = 3
"""
def naive_first_negative_int(arr,k):
    n = len(arr)
    output = []
    for i in range(n-k+1):
        sub_arr = arr[i:i+k]
        flag = True # flag to trace all +ve integer

        for j in range(len(sub_arr)):
            if sub_arr[j] < 0:
                output.append(sub_arr[j])
                flag = False # if we get -ve then set flag to False
                break
        if flag:
            # if no negative found and flag remains true
            output.append(0)

    return output
"""

"""
def naive_first_negative_int(arr,k):
    # improved
    n = len(arr)
    output = []
    for i in range(n-k+1):
        flag = True # flag to trace all +ve integer

        for j in range(k):
            if arr[i+j] < 0:
                output.append(arr[i+j])
                flag = False # if we get -ve then set flag to False
                break
        if flag:
            # if no negative found and flag remains true
            output.append(0)

    return output

print(naive_first_negative_int(arr,k))
"""

# sliding window
arr = [1,2,-1,4,-3,5,-7,8,2,1,8,-5,4]
k = 3
def sliding_window_first_negative_int(arr,k):
    # k is window size
    n = len(arr)

    out_put = []
    i = 0 # first elem of arr
    j = 0 # last elem of arr
    negative_no_list = []

    while(i<n-k+1): # or i<=n-k
        if arr[j] < 0:
            negative_no_list.append(arr[j])
        
        if len(arr[i:j+1]) < k:
            j += 1
            continue
        
        if len(negative_no_list)==0:
            out_put.append(0)
        else:
            out_put.append(negative_no_list[0])

        if len(negative_no_list)!=0 and negative_no_list[0] == arr[i]:
            del negative_no_list[0]
            # negative_no_list.pop(0) or negative_no_list = negative_no_list[:1]
        
        i += 1
        j += 1
    
    return out_put

print(sliding_window_first_negative_int(arr,k))