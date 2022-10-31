message = "CiaonmdGe"
import math
size = int(math.sqrt(len(message)))



grid = [[""] * size for i in range(size)]

print(grid)

i = 0
for r in range(size):
    for c in range(size):
        print(r, c)
        grid[r][c] = message[i]
        i+=1
print(grid)

result = ""
for r in range(size):
    for c in range(size):
        print(r, c)
        result += grid[c][r]
        i+=1

print(result)


