import math


class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.id = row * 8 + col

    def __str__(self):
        return '[{},{}]'.format(self.row, self.col)

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __cmp__(self, other):
        return other.id - self.id

    def __hash__(self):
        return self.id

def getSeat(min, max, code):
    for c in code:
        mid = math.ceil((min + max) / 2)
        if c == 'F' or c == 'L':
            max = mid - 1
        elif c == 'B' or c == 'R':
            min = mid
        else:
            print('Error: Boarding code [', c, ']')

        if min == max:
            break

    return min


def getValidSeats(passes):
    seats = []

    for p in passes:
        row = getSeat(0, 127, p[:-4])
        col = getSeat(0, 7, p[-4:])
        seats.append(Seat(row, col))
    return seats


def getMySeat(seats):
    possibleSeats = []
    for i in range(1, len(seats)-1):
        s = seats[i]
        n1 = seats[i-1]
        n2 = seats[i+1]

        if n1.id != s.id-1 and n2.id != s.id+1:
            possibleSeats.append(s)

    return possibleSeats


def loadfile(filename):
    boardingPasses = []

    with open(filename, 'r') as f:
        for line in f:
            boardingPasses.append(line)

    return boardingPasses


def main():
    passes = loadfile('boarding_passes.txt')

    seats = getValidSeats(passes)

    heighestID = 0
    for seat in seats:
        if seat.id > heighestID:
            heighestID = seat.id
    print('Heighest seat ID: ', heighestID)


    allSeats = [Seat(r, c) for r in range(1, 127) for c in range(0, 8)]

    counter = 0
    for s in seats:
        if s in allSeats:
            allSeats.remove(s)
        else:
            counter += 1

    # Find seats id's without free neighbor seats
    possibleSeats = getMySeat(allSeats)
    print('My seats: ', possibleSeats)
    print('Missing seats: ', counter)

if __name__ == "__main__":
    main()