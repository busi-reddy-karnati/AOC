from functools import lru_cache

@lru_cache(maxsize=None)
def helper(x, y, remaining, xdir, ydir):
    if len(remaining) == 0:
        return 1
    ans = 0
    if x < 0 or x > len(data)-1 or y < 0 or y > len(data[0])-1 or data[x][y] != remaining[0]:
        return 0
    remaining = remaining[1:]
    ans += helper(x+xdir, y+ydir, remaining, xdir, ydir)
    return ans

def read_input():
    with open('input.txt', 'r') as file:
        # Read all lines and strip whitespace
        lines = [line.strip() for line in file.readlines()]
    return lines

def left_diag(x, y):
    if data[x-1][y-1] == 'M' and data[x+1][y+1] == 'S':
        return True
    if data[x-1][y-1] == 'S' and data[x+1][y+1] == 'M':
        return True
    return False

def right_diag(x, y):
    if data[x-1][y+1] == 'M' and data[x+1][y-1] == 'S':
        return True
    if data[x-1][y+1] == 'S' and data[x+1][y-1] == 'M':
        return True
    return False

data = read_input()
ans = 0
for i in range(1, len(data)-1):
    for j in range(1, len(data[0])-1):
        if data[i][j] == 'A':
            if left_diag(i, j) and right_diag(i, j):
                ans += 1
print(ans)

