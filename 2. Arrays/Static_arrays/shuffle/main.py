from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    arr_x = nums[:n]
    arr_y = nums[n:]
    
    x = 0
    y = 0

    for i in range(n*2):
        if i % 2 == 0:
            nums[i] = arr_x[x]
            x += 1
        else:
            nums[i] = arr_y[y]
            y += 1

    print(nums)

nums = [2,5,1,3,4,7]
n = 3

shuffle(nums, n)