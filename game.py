# as seen on https://www.youtube.com/watch?v=o9pEzgHorH0 @ 19:30

import itertools


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


INITIAL_GLIDER = {(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)}
TWO_X_TWO = {(1, 0), (2, 0), (1, 1), (2, 1)}
