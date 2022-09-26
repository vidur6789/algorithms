from cmath import inf
from collections import defaultdict


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
    find smallest subarray with given i.e. greater than equal to sum
    '''
    min_window_size = inf
    start = 0
    current_sum = 0
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum >= target:
            # end + 1 is the end index as end position is included in the window
            min_window_size = min(min_window_size, end + 1 - start)
            current_sum -= nums[start]
            start +=1
             
    return current_sum, min_window_size

def longest_substring_k_distinctchars(string, k):
    max_length = 0
    start = 0
    distinct_chars = defaultdict(int)
    for end in range(len(string)):
        distinct_chars[string[end]] += 1
        print('Expand', string[start:end+1], distinct_chars, len(distinct_chars), max_length)
        while len(distinct_chars) > k :
            distinct_chars[string[start]] -= 1
            if distinct_chars[string[start]] == 0 :
                distinct_chars.pop(string[start])
            start += 1
            print('Shrink', string[start:end +1])
        max_length = max(max_length, end + 1 - start)
    return max_length

def string_permuations():
    return

# print(max_consecutive_sum([100,200,900,300,400], 2))
# print(max_consecutive_sum([4,2,1,7,8,1,2,8,1,0], 3))

# print(smallest_subarray_greater_equal([4,2,2,7,8,1,2,8,10], 18))
print(longest_substring_k_distinctchars('AAAHHIBC',3))


