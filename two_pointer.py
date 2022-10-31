
from math import inf
from structs import Node


def two_sum_sorted(nums, target):
    start = 0
    end = len(nums) - 1
    while (end > start):
        cur_sum = nums[start] + nums[end]
        if cur_sum == target:
            return start, end
        elif cur_sum > target:
            end -= 1
        else:
            start+=1
    
    return -1, -1


def two_sum(nums, target):
    idx_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        print(i, nums[i], diff, idx_map)
        if diff in idx_map:
            return i, idx_map[diff]
        idx_map[nums[i]] = i

def check_palindrome(string):
    i = 0
    j = len(string) - 1
    while j > i:
        if string[j] != string[i]:
            return False
        j -= 1
        i += 1
    return True



def longest_palindrome_substr(string):
    # expand middle algorithm
    pass


def rotate_list_right(nums, k):
    '''
    [0,1,2,3,4,5,6,7], k=3 -> [5,6,7,0,1,2,3,4]
    n=8; j = i + (n-k)
    '''
    new_nums = []
    n = len(nums)
    start = n - k
    for i in range (n):
        j = (start + i) % n 
        new_nums.append(nums[j])
        print(new_nums)
    return new_nums
        

def rotate_list_left(nums, k):
    '''
    another way to do in place would be to visualise rotation as reversal of list around pivot
    eg: [1,2,3,4,5], k=2 -> [3,4,5,1,2] i.e. [1,2,3,4,5] -> [5,4,3,2,1] -> [5,4,3].reverse() + [2,1].reverse()
    '''
    new_nums = []
    n = len(nums)
    start = k
    for i in range (n):
        j = (start + i) % n 
        new_nums.append(nums[j])
        print(new_nums)
    return new_nums


def container_with_most_water(heights):
    start = 0
    end = len(heights) - 1
    max_area = 0
    c_i, c_j = -1, -1
    while end > start:
        area = (end - start) * min(heights[start], heights[end])
        max_area = max(area, max_area)
        print(start, end, area, max_area)
        if heights[start] <  heights[end]:
            start += 1
        else :
            end -= 1
    return max_area


def product_except_self(nums):
    n = len(nums)
    product = [1] * n

    cumsum = 1
    for i in range(1,n):
        product[i] *= cumsum
        cumsum *= nums[i] 
        print('left', product)

    cumsum = 1
    for i in range(n-1, -1, -1):
        print(i, cumsum)
        product[i] *= cumsum
        cumsum *= nums[i]
        print('right', product)
    return product


def reverse_linked_list(root: Node) -> Node:
    cur = root
    prev = None
    while cur:
        next = cur.next
        print(prev.value if prev else None, cur.value, next.value if next else None)
        cur.next = prev
        prev = cur
        cur = next

    return prev


def reverse_list(items):
    l, r = 0, len(items) - 1
    while l < r :
        items[l], items[r] = items[r], items[l]
        l += 1
        r -= 1
    
    return items


def sorted_squares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l, r = 0, n-1
        squared = []
        while l <= r:
            
            if abs(nums[l]) < abs(nums[r]):
                squared.append(nums[r]*nums[r])
                r -= 1
            else:
                squared.append(nums[l]*nums[l])
                l += 1
        
        return squared[::-1]


def move_zeroes(nums):
    '''
    move all zeroes to the start in place
    n = len(nums)
    i,j = n-1, n-1
    [0,1,0,3,0,12]
    the key thing to remember is that you don't care about orig 0 order, 
    so you had to start from reverse for things to maintain the order for things where order matters. 
    In other words, start from the end where you bunch up things whose order matters
    '''
    n = len(nums)
    i,j = n-1, n-1
    while i >= 0:
        print(i, j, nums)
        if nums[i] !=0:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i -= 1
    return  nums


def remove_duplicates(nums):
    '''
    in place without using sets in sorted array
    '''
    n = len(nums)
    end = 1
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[end] = nums[i]
            end += 1
    
    return nums[:end]


def max_profit(prices):
    # brute force is n squared. But intelligently update l to lowest till now, and search all r after that. 
    l = 0
    profit = -inf
    for r in range(1, len(prices)):
        # print(l, r)
        profit = max(prices[r] - prices[l], profit)
        if prices[r] < prices[l]:
            l = r
    
    return profit

def max_sum_subarray(nums):
    '''
    [-2,1,-3,4,-1,2,1,-5,4]
    if all pos, max length would be ans. 
    negative cumsum prefix arr can always be ignored 
    '''
    max_sum = -inf
    cur_sum = 0
    for num in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += num 
        max_sum = max(max_sum, cur_sum)
    return max_sum

def max_product_subarray(nums):
    '''[2,3,-2,-2,4]
    '''
    cur_min = 1
    cur_max = 1
    max_prod = -inf
    for num in nums:
        if num == 0:
            cur_min, cur_max = 1, 1
            continue
        tmp = num * cur_max
        cur_max = max(num*cur_min, num * cur_max, num)
        cur_min = min(num*cur_min, tmp, num)
        max_prod = max(cur_max, max_prod)
        print(num, cur_max, cur_min, max_prod)
    
    return max_prod



        

        






# print(two_sum([1,2,2,7], 9))
# print(two_sum_sorted([1,2,2,7], 9))
# print(check_palindrome('abcdecba'))
# print(rotate_list_right([1,2,3,4,5,6,7], 2))
# print(rotate_list_left([1,2,3,4,5,6,7], 2))
# print(container_with_most_water([1,8,6,2,5,4,8,3,7]))
# print(product_except_self([-1,1,0,-3,3]))
# print(reverse_linked_list(Node.from_list([1,2,3,4,5])).to_list())
# print(sorted_squares([-4,-1,0,3,10]))
# print(reverse_list([1,2,3,4,5,6,7]))
# print(move_zeroes([0,1,0,3,0,12]))
# print(remove_duplicates([1,1,1,1,2,2,2,3,4,5,5,5,6,7,8,9]))
# print(max_profit([7,1,5,3,6,4]))
# print(max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_product_subarray([2,3,-2,4]))

