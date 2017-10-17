# as seen on https://www.youtube.com/watch?v=o9pEzgHorH0 @ 19:30

import itertools
import time


def neighbors(point: (int, int)) -> (int, int):
    '''Gets coords for the 8 neighbors of `point`'''
    x, y = point
    yield x + 1, y
    yield x - 1, y
    yield x + 1, y + 1
    yield x - 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y - 1
    yield x, y + 1
    yield x, y - 1


def advance(board: set) -> set:
    '''Returns new set representing the next state of the `board`'''
    next_board = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    for point in recalc:
        count = sum((neigh in board) for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            next_board.add(point)

    return next_board


def show(board: set) -> None:
    '''display a grid of the board'''
    get = lambda i, p: p[i]
    get_x = lambda p: get(0, p)
    get_y = lambda p: get(1, p)

    high = max(itertools.chain(*board))
    low = min(itertools.chain(*board))

    for y in range(low - 1, high + 2):
        for x in range(low - 1, high + 2):
            if (x, y) in board:
                print('#', end='')
            else:
                print('.', end='')
        print(' {}'.format(y))

    print('')  # blank line


def animate(board: set, iterations: int, pause: float=0.5) -> None:
    b = board.copy()
    for i in range(iterations):
        show(b)
        b = advance(b)
        time.sleep(pause)


GLIDER = {(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)}
TWO_BY_TWO = {(1, 0), (2, 0), (1, 1), (2, 1)}
BLINKER = {(0, 1), (1, 1), (2, 1)}
TOAD = {(1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)}
