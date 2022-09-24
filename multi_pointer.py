

def two_sum(nums, target):
    idx_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        print(i, nums[i], diff, idx_map)
        if diff in idx_map:
            return i, idx_map[diff]
        idx_map[nums[i]] = i



print(two_sum([1,2,2,7], 9))