
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



















