# design an algorithm that analyzes a matrix of ones and zeroes where any connected group of ones is a river.
# a river is a group of connected ones that are all surrounded by zeros.
# the algorithm should return a list of the sizes of all rivers in the matrix.
#
# input:
# [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
#   1, 0, 0, 0, 1, 1, 1, 1, 0, 0
#  0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
# output:
# [1, 2, 1]

def river_sizes(matrix):
    sizes = []
    visited = [[False for col in row] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and not visited[row][col]:
                sizes.append(bfs(matrix, visited, row, col))
    return sizes

def bfs(matrix, visited, row, col):
    queue = [(row, col)]
    visited[row][col] = True
    size = 0
    while queue:
        row, col = queue.pop(0)
        size += 1
        for r, c in get_neighbors(matrix, row, col):
            if matrix[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                queue.append((r, c))
    return size

def get_neighbors(matrix, row, col):
    neighbors = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]):
                if r != row or c != col:
                    neighbors.append((r, c))
    return neighbors

def main():
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
    ]
    print(river_sizes(matrix))

# test_matrix = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
# ]
# print(river_sizes(test_matrix))

if __name__ == "__main__":
    main()