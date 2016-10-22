def answer(entrances, exits, path):
    mask = [list(p) for p in path]

    for room in path:


    return sum([sum(path[e]) for e in exits])


entrances = [0, 1]
exits = [4, 5]
path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(answer(entrances, exits, path))