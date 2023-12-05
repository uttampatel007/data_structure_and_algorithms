
tests = [{
    "input": {
        "cards":[12,11,10,4,3,2,1],
        "query": 10
    },
    "output": 2
},{
    "input": {
        "cards":[12,11,10,4,3,2,1],
        "query": 12
    },
    "output": 0
},{
    "input": {
        "cards":[12,11,10,4,3,2,1],
        "query": 1
    },
    "output": 6
},
{
    "input": {
        "cards":[12,11,10,4,3,2,1],
        "query": 13
    },
    "output": -1
}]


def binary_search(cards, query):
    lo, hi = 0, len(cards)-1
    
    while lo <= hi:
        # find the mid position
        mid = (lo + hi) // 2
        mid_num = cards[mid]

        if mid_num == query:
            return mid
            
        elif mid_num > query:
            lo = mid + 1
        
        elif mid_num < query:
            hi = mid - 1
    
    return -1


for test in tests:
    result = binary_search(**test["input"])
        
    print(result, test['output'])
    
    assert test['output'] == result


# rotating list 

nums = [6,7,8,9,10,11,1,2,3,4,5]
output = 6

# def count_rotation_linear(nums):
#     position = 0
    
#     while position < len(nums):
#         if position > 0 and nums[position] < nums[position-1]:
#             return position
            
#         position += 1 
        
#     return 0


def count_rotation_binary(nums):
  lo = 0
  hi = len(nums) - 1
  
  while hi >= lo:
    mid = (hi+lo)//2
    mid_num = nums[mid]
    
    if mid > 0 and mid_num < nums[mid-1]:
      return mid
    
    elif mid_num > nums[hi]:
      lo = mid + 1
      
    elif mid_num < nums[hi]:
      hi = mid - 1
      
  return 0
  
    
  
    
# result = count_rotation_linear(nums)
result = count_rotation_binary(nums)
print(result)
assert result == output
















