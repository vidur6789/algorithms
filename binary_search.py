
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
    if len(nums) == 0:
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
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        return 0 if nums[0] > nums[1] else 1
    mid = (low + high) // 2
    if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        return mid
    elif nums[mid] > nums[mid+1]:
        return find_peak_alt(nums, low, mid)
    else:
        return find_peak_alt(nums, mid+1, high)

def number_left_roations_sorted(nums):
    '''
    sorted array rotated left x times, find x
    Soln: left shift creates a peak. number of elements to the right of the peak will be equal to x 
    '''
    return len(nums) - 1 - find_peak(nums)

# print(find_in_sorted([1,2,3,4,5], 4))
# print(find_in_sorted_alt([1,2,3,4,5], 5, 0, 5))
# print(find_in_sorted(sorted(range(30)), 17))
# print(frequency_in_sorted([1,2,3,4,4,4,4,4,5,5,5,5,5,5,6], 5))
# print(find_peak([4,5,6,7,0,1,2,3]))
print(find_peak_alt([4,5,6,7,0,1,2,3], 0, 8))
# print(number_left_roations_sorted([4,5,6,7,0,1,2,3]))




