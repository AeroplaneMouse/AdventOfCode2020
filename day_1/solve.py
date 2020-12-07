

# Orders a pair from smallest to biggest
def orderSet(pair):
    newPair = set()

    for i in range(0, len(pair)):
        smallest = min(pair)
        pair.remove(smallest)
        newPair.add(smallest)

    return newPair


def findPairs(expenseReport, pairSize, sum):
    pairs = []

    for n in expenseReport:
        newSum = sum - n
        if (pairSize == 1 and newSum == 0):
            pairs.append([n])
        elif (pairSize > 1 and newSum > 0):
            sPairs = findPairs(expenseReport, pairSize - 1, newSum)

            # Compine results
            for p in sPairs:
                p.append(n)
                p.sort()
                if p not in pairs:
                    pairs.append(p)

    return pairs


def computeValue(list):
    value = 1
    for num in list:
        value *= num

    return value


def loadFile(fileName):
    list = []

    # Read file
    with open(fileName, 'r') as f:
        num = f.readline()
        while (len(num) > 0):
            list.append(int(num))
            num = f.readline()

    return list


def main():
    expenseReport = loadFile('expense_report.txt')

    print('2-pairs:')
    pairs = findPairs(expenseReport, 2, 2020)
    for pair in pairs:
        value = computeValue(pair)
        print('{:<15} = '.format(value), pair)

    print()
    print('3-pairs:')
    pairs = findPairs(expenseReport, 3, 2020)
    for pair in pairs:
        value = computeValue(pair)
        print('{:<15} = '.format(value), pair)

# Run main
if __name__ == '__main__':
    main()
