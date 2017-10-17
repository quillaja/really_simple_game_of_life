# A simple implementation of Conway's Game of Life
# as seen on https://www.youtube.com/watch?v=o9pEzgHorH0 @ 19:30.
# The game itself is `advance()` and `neighbors()`. Other methods
# are for display.

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

    # all points to examine, live ones + their neighbors
    recalc = board | set(itertools.chain(*map(neighbors, board)))

    # build next board iteration
    for point in recalc:
        count = sum((neigh in board) for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            next_board.add(point)

    return next_board


def show(board: set) -> None:
    '''display a grid of the board'''

    # get board sizes
    xs, ys = zip(*board)
    x_high, x_low = max(xs), min(xs)
    y_high, y_low = max(ys), min(ys)

    # draw board, plus 1 char 'margin' on each side
    print('\033[2J\033[0;0H', end='') # clear screen & move cursor to 0,0

    output = '' # faster than multiple calls to print
    for y in range(y_low - 1, y_high + 2):
        for x in range(x_low - 1, x_high + 2):
            if (x, y) in board:
                output += '\u2588'
            else:
                output += '\u2591'
        output += ' {}\n'.format(y)  # display the y-coord on end of line

    print(output)  # show output at once w/ blank line


def animate(board: set, iterations: int, pause: float = 0.5) -> None:
    '''Run through some `iterations` of `board`, printing the board to
    screen each time and pausing `pause` seconds before advancing.
    Does not modify `board`.'''

    b = board.copy()
    for _ in range(iterations):
        show(b)
        b = advance(b)
        time.sleep(pause)


def cls():
    print('\033[2J')


GLIDER = {(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)}
TWO_BY_TWO = {(1, 0), (2, 0), (1, 1), (2, 1)}
BLINKER = {(0, 1), (1, 1), (2, 1)}
TOAD = {(1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)}

RPENTOMINO={
          (1,0),(2,0),
    (0,1),(1,1),
          (1,2)
}

ACORN = {
        (1,0),
                     (3,1),
    (0,2),(1,2),           (4,2),(5,2),(6,2)
}

FIVE_BY_FIVE = {
    (0,0),(1,0),(2,0),      (4,0),
    (0,1),
                      (3,2),(4,2),
          (1,3),(2,3),      (4,3),
    (0,4),      (2,4),      (4,4)
}
