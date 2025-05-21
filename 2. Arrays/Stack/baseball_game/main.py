from typing import List

def calPoints(operations: List[str]) -> int:
    k = 0
    ops_arr = []

    for op in operations:
        match op:
            case '+':
                ops_arr.append(int(ops_arr[k-1] + ops_arr[k-2]))
                k += 1
            case 'D':
                ops_arr.append(int(ops_arr[k-1] * 2))
                k += 1
            case 'C':
                ops_arr.pop()
                k -= 1
            case _:
                ops_arr.append(int(op))
                k += 1
    
    return sum(ops_arr)
    
        

ops = ["1","C"]

calPoints(ops)