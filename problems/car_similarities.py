
def check_similarity(car1, car2):
    diff_count = 0
    for i in range(len(car1)):
        if car1[i] != car2[i]:
            diff_count += 1
        if diff_count > 1:
            return False
    return True

def solution(cars):
    # write your code in Python 3.8.10
    n = len(cars)
    similarities = [[False] *n for i in range(n)]
    
    for i in range(n -1):
        for j in range(i+1, n):
            similarity = check_similarity(cars[i], cars[j])
            similarities[i][j] = similarity
            similarities[j][i] = similarity
    return [sum(s) for s in similarities]


print(solution(cars=['00', '01', '10', '11']))
print(solution(cars=['100', '110', '010', '011', '100']))

    