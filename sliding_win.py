from cmath import inf


def max_consecutive_sum(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(len(nums)-k):
        current_sum = current_sum - nums[i] + nums[i+k]
        print(nums[i+1:i+k+1], current_sum)
        max_sum = max(max_sum, current_sum)
    return max_sum

def longest_substring_without_repeat_chars():
    return

def smallest_subarray_greater_equal(nums, target):
    '''
    find smallest subarray with given sum
    '''
    min_window_size = inf
    start = 0
    current_sum = 0
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum >= target:
            min_window_size = min(min_window_size, end - start) 
            current_sum -= nums[start]
            start +=1
             



    return current_sum, min_window_size

def longest_substring_less_than_k_distinctchars():
    return

def string_permuations():
    return

# print(max_consecutive_sum([100,200,900,300,400], 2))
# print(max_consecutive_sum([4,2,1,7,8,1,2,8,1,0], 3))

print(smallest_subarray_greater_equal([4,2,2,7,8,1,2,8,10], 8))


