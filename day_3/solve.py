
def nextPos(row, col, width, height, route):
    row += route[0]
    col = (col + route[1]) % width

    return row, col


def countTrees(map, startPos, route, writePath):
    # route(down, right)
    nTrees = 0

    height = len(map)
    width = len(map[0])

    row = startPos[0]
    col = startPos[1]

    # Continue counter until end has been reached
    while row < height:
        # Count tree
        if map[row][col] == '#':
            nTrees += 1

        # Update map with path
        if writePath:
            if map[row][col] == '#':
                map[row][col] = 'X'
            else:
                map[row][col] = 'O'

        # Set next pos
        row, col = nextPos(row, col, width, height, route)

    return nTrees


# Loades map file
def loadfile(filename):
    map = []
    charOfInterest = ['.', '#']

    # Read file
    with open(filename, 'r') as f:
        # Read line
        for line in f:
            # Load single row map data into list
            row = []
            for c in line:
                # Only add . and # to skib newline and what not
                if c in charOfInterest:
                    row.append(c)

            # Add single row to map
            map.append(row)

    return map


# Prints the entier map
def toString(map):
    row = ''
    for r in map:
        # print(r)
        for c in r:
            row += c
        row += '\n'

    return row


# Main function
def main():
    map = loadfile('map.txt')

    # Day 1
    trees = countTrees(map, startPos=(0, 0), route=(1, 3), writePath=True)
    print('Trees encountered: ', trees)

    # Save pathed map
    # with open('pathed_map.txt', 'w') as f:
    #     f.write(toString(map))


    # Day 2
    map = loadfile('map.txt')
    routes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]

    result = 1
    for route in routes:
        trees = countTrees(map, startPos=(0, 0), route=route, writePath=False)
        print('Route: ', route, ' encountered: ', trees)
        result *= trees

    print('Day 2: ', result)



if __name__ == '__main__':
    main()
