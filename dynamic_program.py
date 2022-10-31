from collections import deque
def longest_increasing_subsequence(arr):
    '''
    LIS(i) = 1 + max(L[k], where k < i and arr[k] < arr[i])
    '''
    lis = [1]*len(arr)
    prev = [-1] *len(arr)
    for i in range(1, len(arr)):
        subproblems = [(k, lis[k]) for k in range(i) if arr[k] < arr[i]]
        # print(i, subproblems)
        if len(subproblems) == 0:
            continue
        max_length_prev, max_length = max(subproblems, key= lambda l: l[1])
        prev[i] = max_length_prev
        lis[i] = 1 +max_length
        # print(i, lis, max_length_prev)

    
    start = 4
    path = deque()
    while start != -1:
        path.appendleft(arr[start])
        start = prev[start]
    print(path)
    return lis[-1], prev, path


def tallest_box_stack(boxes):
    '''
    list of tuples (L, W, H)
    find tallest stack of boxes such that,
    box on top always has lesser length and width
    subproblem -> tallest stack ending at box
    generalize -> max of subproblems/boxes that can be stacked above + height of current box
    implement by starting with smallest boxes to solve subproblems before other problems
    '''
    boxes = sorted(boxes, key= lambda b: b[0]) # sort boxes by length/width. either is fine, since stack condition requires both
    heights = {box: box[2] for box in boxes} # initialise with box height
    boxes_below = {box: None for box in boxes}
    print('sorted', boxes, heights)
    for i in range(1, len(boxes)): # starting from 1, since initialisation solved the problem for the smallest box already
        box = boxes[i]
        # identify subproblems that follow constraint
        subproblems = [(b, heights[b]) for b in boxes[:i] if ((b[0] < box[0]) and (b[1]<box[1]))]
        # solve and store subproblem 
        if len(subproblems) == 0:
            continue # alternatively set subproblem solution to some default/base value. in this case, already initialized
        box_below, height = max(subproblems, key=lambda b: b[1])
        boxes_below[box] = box_below
        heights[box] += height
        print(i, subproblems, box_below, height)
        print(boxes_below)
        print(heights)

    return max(heights.values()), boxes_below


# print(longest_increasing_subsequence([3,1,8,2,5]))
print(tallest_box_stack([(4,5,3), (3,6,2), (2,4,1), (2,3,2), (1,5,4), (1,2,2)]))

    