
# Tests
def Test_Policy_isValid_single_letter_policy_day1Validation():
    p = Policy(1, 3, ['a'])
    validPasswords = ['a', 'bab', 'aaa', 'aba', 'aa']
    invalidPasswords = ['b', 'c', 'bbaaaa', 'aaaba']

    print('Valid passwords:')
    for q in validPasswords:
        print('{:<7} | {}'.format(q, p.isValid_day1(q)))

    print()
    print('Invalid passwords:')
    for q in invalidPasswords:
        print('{:<7} | {}'.format(q, p.isValid_day1(q)))


def Test_Policy_isValid_single_letter_policy_day2Validation():
    p = Policy(1, 10, ['a'])
    validPasswords = ['ajahkjhks', 'babbbbbbba', 'aaaaaaaaaaaaaaa']
    invalidPasswords = ['ba']

    print('Valid passwords:')
    for q in validPasswords:
        print('{:<15} | {}'.format(q, p.isValid_day2(q)))

    print()
    print('Invalid passwords:')
    for q in invalidPasswords:
        print('{:<15} | {}'.format(q, p.isValid_day2(q)))


class Policy:
    minimum = 0
    maximum = 0
    letters = []

    def __init__(self, low, high, letters):
        self.minimum = low
        self.maximum = high
        self.letters = letters

    def isValid_day1(self, password):
        occurences = {}

        # Count occurences
        for l in self.letters:
            occurences[l] = 0
            for c in password:
                if l == c:
                    occurences[l] += 1
        # Check for validity
        for key in occurences:
            v = occurences[key]
            if v < self.minimum or v > self.maximum:
                return False

        return True

    def isValid_day2(self, password):
        pos_1 = self.minimum - 1
        pos_2 = self.maximum - 1
        passLength = len(password)
        for letter in self.letters:
            flag = False
            if pos_1 < passLength and password[pos_1] == letter:
                flag = True

            if pos_2 < passLength and password[pos_2] == letter:
                flag ^= True

            if not flag:
                return False

        return True


class PPCombo:
    password = ""
    policy = None

    def __init__(self, policy, password):
        self.policy = policy
        self.password = password


def extractPolicy(policyParts):
    p = policyParts.split(' ')

    # Extract limits
    limits = p[0].split('-')
    low = int(limits[0])
    high = int(limits[1])

    # Extract letters
    letters = []
    for letter in p[1]:
        letters.append(letter)

    return Policy(low, high, letters)


def loadFile(filename):
    ppCombos = []

    with open(filename, 'r') as f:
        line = f.readline()
        while(line != ''):
            parts = line.split(':')
            policy = extractPolicy(parts[0])
            password = parts[1][1:-1]

            ppCombos.append(PPCombo(policy, password))
            line = f.readline()

    return ppCombos


def main():
    ppCombos = loadFile('policy-password_combo.txt')

    # Count day 1 valid passwords
    count = 0
    for combo in ppCombos:
        passw = combo.password
        pol = combo.policy
        if pol.isValid_day1(passw):
            count += 1

    print('This is {} valid passwords: Day 1'.format(count))

    # Count day 2 valid passwords
    count = 0
    for combo in ppCombos:
        passw = combo.password
        pol = combo.policy
        if pol.isValid_day2(passw):
            count += 1
    print('This is {} valid passwords: Day 2'.format(count))


if __name__ == '__main__':
    main()

