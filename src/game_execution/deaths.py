black_deaths = []
white_deaths = []


def add_death(piece):
    if piece[1] == 'B':
        black_deaths.append(piece[0])
    else:
        white_deaths.append(piece[0])