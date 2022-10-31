
def find_in_sorted(nums, target, offset=0):
    '''
    offset needed only if you need to find index
    '''
    # print(offset)
    if len(nums) == 0:
        return False, -1
    
    mid = len(nums) // 2
    if nums[mid] == target:
        return True, offset + mid
    elif target > nums[mid]:
        return find_in_sorted(nums[mid+1:], target, offset+mid+1)
    else:
        return find_in_sorted(nums[:mid], target, offset)


def find_in_sorted_alt(nums, target, low, high):

    print(low, high)
    if len(nums) == 0 or low > high:
        return False, -1
    mid = ((high+low) // 2)
    if nums[mid] == target:
        return True, mid
    elif nums[mid] > target:
        return find_in_sorted_alt(nums, target, low, mid)
    else:
        return find_in_sorted_alt(nums, target, mid+1, high)
    

def frequency_in_sorted(nums, target):
    if len(nums) == 0:
        return 0
    mid = len(nums) // 2
    if nums[mid] == target:
        return 1 + frequency_in_sorted(nums[:mid], target) + frequency_in_sorted(nums[mid+1:], target)
    elif nums[mid] < target:
        return frequency_in_sorted(nums[mid+1:], target)
    else:
        return frequency_in_sorted(nums[:mid], target) 


def frequency_in_sorted_alt(nums, target, low ,high, n):
    '''
    find L -> leftmost target, separate binary search O(logN)
    find R -> rightmost target, separate binary search O(logN)
    return R - L + 1
    '''


def leftmost_index_target(nums, target, low, high):
    print(low, high)
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target and (nums[mid-1] < target or mid ==0):
        return mid
    elif nums[mid] < target:
        return leftmost_index_target(nums, target, mid+1, high)
    else: 
        return leftmost_index_target(nums, target, low, mid-1)


def rightmost_index_target(nums, target, low, high, n):
    print(low, high)
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target and (nums[mid+1] > target or mid == n-1):
        return mid
    elif nums[mid] > target:
        return rightmost_index_target(nums, target, low, mid-1, n)
    else:
        return rightmost_index_target(nums, target, mid+1, high, n)




def frequency_in_sorted(nums, target):
    l = leftmost_index_target(nums, target, 0, len(nums)-1)
    r = rightmost_index_target(nums, target, 0, len(nums)-1)


def find_peak(nums, offset=0):
    print(nums, offset)
    if len(nums) == 1:
        return offset
    elif len(nums) == 2:
        return offset if nums[0] > nums[1] else offset + 1
    mid = len(nums) // 2
    if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
        return offset + mid
    elif nums[mid] < nums[mid + 1]:
        return find_peak(nums[mid+1:], offset+mid+1)
    else:
        return find_peak(nums[:mid], offset)


def find_peak_alt(nums, low, high):
    print(low, high)
    if low == high:
        return 0
    elif high - low == 1:
        return low if nums[low] > nums[high] else high
    mid = (low + high) // 2
    if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        return mid
    elif nums[mid] > nums[mid+1]:
        return find_peak_alt(nums, low, mid)
    else:
        return find_peak_alt(nums, mid+1, high)


def middle_peak_in_shifted_sorted(nums, low, high, n):
    print(low, high)
    if low > high: 
        return -1
    mid = (low+high) // 2
    if nums[mid] > nums[mid+1]:
        return mid
    elif nums[n-1] > nums[mid]:
        return middle_peak_in_shifted_sorted(nums, low, mid-1, n)
    else: 
        return middle_peak_in_shifted_sorted(nums, mid+1, high, n)

def number_left_roations_sorted(nums):
    '''
    sorted array rotated left x times, find x
    Soln: left shift creates a peak. number of elements to the right of the peak will be equal to x 
    '''
    middle_peak = middle_peak_in_shifted_sorted(nums, 0, len(nums)-1, len(nums))
    n = len(nums)
    print(n, 'middle_peak', middle_peak)
    return n -1  - (middle_peak + 1) + 1

# print(find_in_sorted([1,2,3,4,5], 4))
# print(find_in_sorted_alt([1,2,3,4,5], 1, 0, 4))
# print(find_in_sorted(sorted(range(30)), 17))
# print(frequency_in_sorted([1,2,3,4,4,4,4,4,5,5,5,5,5,5,6], 5))
# print(find_peak([4,5,6,7,0,1,2,3]))
# print(find_peak_alt([4,5,6,7,0,1,2,3,3], 0, 8))
# print(middle_peak_in_shifted_sorted([4,5,6,7,0,1,2,3], 0, 7, 8))
print(number_left_roations_sorted([4,5,6,7,0,1,2,3]))
nums = [1,2,3,3,3,3,3,4,5]
# print(leftmost_index_target(nums,3,0,len(nums)-1))
# print(rightmost_index_target(nums,3,0,len(nums)-1, len(nums)))






