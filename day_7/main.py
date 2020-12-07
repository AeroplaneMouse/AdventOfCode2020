import queue

class Rule:
    label = ''
    bags = {}

    def __init__(self, label, bags):
        self.bags = bags
        self.label = label

def extractBags(strings):
    bags = {}

    for b in strings:
        content = b.split(' ')
        label = content[2] + ' ' + content[3]
        num = int(content[1])

        bags[label] = num

    return bags


def loadfile(filename):
    rules = []

    with open(filename) as f:
        for line in f:
            parts = line.split(' bags contain',)
            label = parts[0]

            if parts[1] == ' no other bags.\n':
                bags = {}
            else:
                strBags = parts[1].split(',')
                bags = extractBags(strBags)

            rules.append(Rule(label, bags))

    return rules


def findBagsContaining(rules, label):
    found = []

    for r in rules:
        for bag in r.bags:
            if bag == label:
                found.append(r.label)
                break

    return found


def findBag(rules, bagLabel):
    for r in rules:
        if r.label == bagLabel:
            return r

    print('Error: Bag not found. ' + bagLabel)


def getBags(rules, bagLabel):
    bag = findBag(rules, bagLabel)
    count = 0

    if len(bag.bags) == 0:
        return 0
    else:
        bags = bag.bags
        for b in bags:
            # Get count for each bag in parent bag
            num = bags[b]
            count += num

            # Get count for each child bag in bag
            count += getBags(rules, b) * num

    return count


def main():
    rules = loadfile('rules.txt')

    q = queue.SimpleQueue()
    q.put('shiny gold')
    counted = []

    while not q.empty():
        foundRules = findBagsContaining(rules, q.get())
        for r in foundRules:
            if r not in counted:
                counted.append(r)
                q.put(r)

    print('# of bags containing initial: ' + str(len(counted)))

    count = getBags(rules, 'shiny gold')
    print('A \'shiny gold\' bag contains: ' + str(count) + ' bags!')


if __name__ == '__main__':
    main()
