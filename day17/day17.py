

def min_path_cost(grid):
    m, n = len(grid), len(grid[0])
    dp = [[[[float('inf')]*4 for _ in range(4)]
           for _ in range(n)] for _ in range(m)]
    prev = [[[[None]*4 for _ in range(4)] for _ in range(n)] for _ in range(m)]
    dp[0][0][0][1] = grid[0][0]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

    for i in range(m):
        for j in range(n):
            for k in range(4):
                for d in range(4):
                    if dp[i][j][k][d] < float('inf'):
                        if k < 3:  # Move forward
                            ni, nj = i + dirs[d][0], j + dirs[d][1]
                            if 0 <= ni < m and 0 <= nj < n:
                                cost = dp[i][j][k][d] + grid[ni][nj]
                                if cost < dp[ni][nj][k+1][d]:
                                    dp[ni][nj][k+1][d] = cost
                                    prev[ni][nj][k+1][d] = (i, j, k, d)
                        # Turn left or right
                        for nd in [(d-1) % 4, (d+1) % 4]:
                            ni, nj = i + dirs[nd][0], j + dirs[nd][1]
                            if 0 <= ni < m and 0 <= nj < n:
                                cost = dp[i][j][k][d] + grid[ni][nj]
                                if cost < dp[ni][nj][1][nd]:
                                    dp[ni][nj][1][nd] = cost
                                    prev[ni][nj][1][nd] = (i, j, k, d)

    print_path(dp, prev, dirs, grid)
    return min(min(dp[m-1][n-1]))


def print_path(dp, prev, dirs, grid):
    m, n, k, d = len(dp), len(dp[0]), 0, 0
    for i in range(4):
        for j in range(4):
            if dp[m-1][n-1][i][j] < dp[m-1][n-1][k][d]:
                k, d = i, j

    path = [(m-1, n-1)]
    while path[-1] != (0, 0):
        i, j, k, d = prev[path[-1][0]][path[-1][1]][k][d]
        path.append((i, j))

    path.reverse()
    for i, j in path:
        grid[i][j] = '#'

    for row in grid:
        print(''.join(str(cell) for cell in row))


def print_array(array):
    for line in array:
        print(''.join(line))


def load_file(input):
    _map = []
    with open(input, 'r') as file:
        _map = [list(map(int, line.strip())) for line in file.readlines()]
    return _map


def part1(input='day17/input.txt'):
    print('')
    grid = load_file(input)
    return min_path_cost(grid)


if __name__ == '__main__':
    print(part1())
