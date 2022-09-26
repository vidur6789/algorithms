

def reverse_string(string):
    '''
    simple algorithm could do it in O(n) complexity by iterating over the string and swapping or storing in a new string
    '''
    if len(string) == 1:
        return string
    elif len(string) == 2:
        return string[1] + string[0]
    mid = len(string) // 2 
    
    return ''.join([reverse_string(string[mid+1:]), string[mid], reverse_string(string[:mid])]) 


def sum_nonnegative_ints_n(n):
    if n <=1:
        return n
    return n + sum_nonnegative_ints_n(n-1)


def path_finder(n, m):
    '''
    find number of unique paths from top left to bottom right in nxm grid
    '''
    if n == 1 or m == 1:
        return 1
    return path_finder(n - 1, m) + path_finder(n, m-1)


def count_partitions(n, m):
    '''
    count number of partition of n objects in parts of upto m
    '''
    if m == 1:
        return 1
    elif n < 0: 
        return 0
    elif n == 0:
        return 1 # no partition, unconvincing
    # n, m-1 is obviously a subset of n, m. 
    # The rest of the difference seems to be using m objects. remove m and you have n-m, m
    return count_partitions(n, m-1) + count_partitions(n-m, m)

print(sum_nonnegative_ints_n(5))
print(reverse_string('abcdefg'))
print(reverse_string('abcd'))
print(path_finder(2,4))
print(path_finder(3,3))
print(count_partitions(7,4))