from random import sample

board = [
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 7, 0, 0, 0, 5],
    [0, 0, 8, 0, 0, 0, 0, 4, 0],
    [2, 0, 0, 9, 0, 0, 0, 0, 8],
    [9, 7, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 7],
    [3, 0, 0, 7, 0, 0, 0, 8, 0],
    [0, 0, 9, 3, 0, 0, 0, 0, 0],
    [0, 0, 2, 8, 0, 0, 0, 0, 0]
]

example_board = [
    [0, 0, 6, 0, 0, 0, 0, 5, 4],
    [0, 7, 2, 0, 4, 0, 0, 9, 8],
    [9, 1, 4, 0, 2, 5, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 4, 0, 0],
    [0, 5, 1, 0, 8, 0, 3, 6, 0],
    [0, 0, 3, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 1, 9, 0, 7, 3, 6],
    [2, 6, 0, 0, 3, 0, 9, 8, 0],
    [1, 3, 0, 0, 0, 0, 5, 0, 0]
]


def generate_board(num):
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return sample(s, len(s))

    # randomize rows, col, num
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # randomized baseline
    board_tmp = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # print full board
    # for line in board_tmp:
    #     print(line)

    # remove nums
    squares = side * side
    if num == 0:
        empties = squares * 3 // 4
    else:
        empties = 81 - num
    for p in sample(range(squares), empties):
        board_tmp[p // side][p % side] = 0

    # printing start
    #
    # numSize = len(str(side))
    # for line in board_tmp:
    #     print("[" + "  ".join(f"{n or '.':{numSize}}" for n in line) + "]")
    #
    # printing end

    return board_tmp


"""
This solution works, but it cold create boards that are not possible.

def generate_board(num):
    bo = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            bo[i][j] = 0

    for i in range(num):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)

        while not possible(bo, (row, col), num) or bo[row][col] != 0:
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        bo[row][col] = num

    return bo
"""


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def possible(bo, pos, num):
    # rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # square
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):  # row
        for j in range(box_x * 3, box_x * 3 + 3):  # col
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def next_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col


def solve(bo):
    slot = next_empty(bo)
    if not slot:
        return True
    else:
        row, col = slot

    for i in range(1, 10):
        if possible(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


# board = generate_board(0)
print_board(board)
solve(board)
print("=========================")
print_board(board)


"""
Special boards:

solition took long:
0 9 0  | 0 0 0  | 0 0 0
0 2 0  | 0 7 0  | 0 0 5
0 0 8  | 0 0 0  | 0 4 0
- - - - - - - - - - - - -
2 0 0  | 9 0 0  | 0 0 8
9 7 0  | 0 0 0  | 0 2 0
0 0 0  | 0 0 3  | 0 0 7
- - - - - - - - - - - - -
3 0 0  | 7 0 0  | 0 8 0
0 0 9  | 3 0 0  | 0 0 0
0 0 2  | 8 0 0  | 0 0 0
board = [
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 7, 0, 0, 0, 5],
    [0, 0, 8, 0, 0, 0, 0, 4, 0],
    [2, 0, 0, 9, 0, 0, 0, 0, 8],
    [9, 7, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 7],
    [3, 0, 0, 7, 0, 0, 0, 8, 0],
    [0, 0, 9, 3, 0, 0, 0, 0, 0],
    [0, 0, 2, 8, 0, 0, 0, 0, 0]
]

"""
