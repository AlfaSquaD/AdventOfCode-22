WIN_POINT = 6
DRAW_POINT = 3
LOSE_POINT = 0

ROCK_EXTRA = 1
PAPER_EXTRA = 2
SCISSORS_EXTRA = 3

'''
A - X = Rock

B - Y = Paper

C - Z = Scissors

'''

LOGIC_DICT = {
    'A': {
        'X': DRAW_POINT + ROCK_EXTRA,
        'Y': WIN_POINT + PAPER_EXTRA,
        'Z': LOSE_POINT + SCISSORS_EXTRA
    },
    'B': {
        'X': LOSE_POINT + ROCK_EXTRA,
        'Y': DRAW_POINT + PAPER_EXTRA,
        'Z': WIN_POINT + SCISSORS_EXTRA
    },
    'C': {
        'X': WIN_POINT + ROCK_EXTRA,
        'Y': LOSE_POINT + PAPER_EXTRA,
        'Z': DRAW_POINT + SCISSORS_EXTRA
    }
}

def main():
    totalPoints = 0
    with open('input.txt') as f:
        lines = f.readlines()
        while len(lines) > 0:
            actions = lines.pop(0).split()
            totalPoints += LOGIC_DICT[actions[0]][actions[1]]
    print(totalPoints)

if __name__ == '__main__':
    main()

            
