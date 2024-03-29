import numpy as np
from collections import Counter

def hatFunc(size: int) -> int: # Function that mimics the hat game and returns the final value
    nums = [(i+1) for i in range(size)]
    np.random.shuffle(nums) # Shuffles the numbers
    
    for i in range(size -1):
        temp = abs(nums[0] - nums[1])
        nums = nums[2:] # Takes and removes the first two
        nums.insert(np.random.randint(0, len(nums) + 1), temp)
        
    return nums[0]

if __name__ == "__main__":
    hatSize = 2024
    samples = 100
    
    results = []
    for i in range(samples):
        results.append(hatFunc(hatSize))

    x = Counter(results)
    sortedX = dict(sorted(x.items())) # Arranges the results into a dictionary
    print(sortedX)