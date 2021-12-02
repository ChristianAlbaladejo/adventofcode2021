f = open("input.txt", "r")


def part_1():
    d = {}
    for s in f:
        key, value = s.split()
        d[key] = d.get(key, 0) + int(value)
    f.close()
    print(d['forward'] * (d['down'] - d['up']))


def part_2():
    results = {
        'horizontal': 0,
        'depth': 0,
        'aim': 0
    }
    data = []
    for x in f:
        data.append(x.split())
    for move in data:
        if move[0] == 'forward':
            results['horizontal'] += int(move[1])
            results['depth'] += int(move[1]) * results['aim']
        elif move[0] == 'down':
            results['aim'] += int(move[1])
        elif move[0] == 'up':
            results['aim'] -= int(move[1])
    print(results)
    print(results['horizontal'] * results['depth'])


if __name__ == "__main__":
    # part_1()
    part_2()