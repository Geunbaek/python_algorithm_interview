def zero_one_knapsack(cargo, capacity):
    pack = []

    for y in range(len(cargo) + 1):
        pack.append([])
        for x in range(capacity + 1):
            if y == 0 or x == 0:
                pack[y].append(0)
            elif cargo[y-1][1] <= x:
                pack[y].append(
                    max(cargo[y-1][0] + pack[y-1][x - cargo[y-1][1]], pack[y-1][x])
                )
            else:
                pack[y].append(pack[y-1][x])
    return pack[-1][-1]




print(zero_one_knapsack([(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)], 15))


"""
input
cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]
"""