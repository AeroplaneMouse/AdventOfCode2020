import re

expectedFields = (
    'byr', # (Birth Year)
    'iyr', # (Issue Year)
    'eyr', # (Expiration Year)
    'hgt', # (Height)
    'hcl', # (Hair Color)
    'ecl', # (Eye Color)
    'pid', # (Passport ID)
    # 'cid'  # (Country ID)
    )


def rtrim(str, trimC):
    newStr = ''
    index = len(str)
    for c in str:
        if c == trimC:
            break
        newStr += c

    return newStr


def loadPassports(filename):
    passports = []

    with open(filename, 'r') as f:
        currentPassport = dict()
        for line in f:
            # Blank lines
            if line == '\n':
                passports.append(currentPassport)
                currentPassport = dict()
            else:
                fields = line.split(' ')
                # Add fields to passport
                for field in fields:
                    parts = field.split(':')
                    currentPassport[parts[0]] = rtrim(parts[1], '\n')
    return passports


def getUnit(value):
    unit = value[-2:]
    if unit == 'cm' or unit == 'in':
        return unit
    else:
        return None


def validate(passport, strict):
    for field in expectedFields:
        # Check if expected fields are present
        if field not in passport.keys():
            return False

        # Validate content of expected fields
        elif strict:
            value = passport[field]
            chars = len(value)

            if field == 'byr':
                value = int(value)
                if chars != 4 or value < 1920 or value > 2002:
                    return False

            elif field == 'iyr':
                value = int(value)
                if chars != 4 or value < 2010 or value > 2020:
                    return False

            elif field == 'eyr':
                value = int(value)
                if chars != 4 or value < 2020 or value > 2030:
                    return False

            elif field == 'hgt':
                # Extract value and unit
                unit = getUnit(value)
                if unit is None:
                    return False
                else:
                    value = int(value[:-2])

                if unit == 'cm':
                    if value < 150 or value > 193:
                        return False
                elif unit == 'in':
                    if value < 59 or value > 76:
                        return False
                else:
                    return False

            elif field == 'hcl':
                if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):
                    return False

            elif field == 'ecl':
                valid = ['amb','blu','brn','gry','grn','hzl','oth']
                if not value in valid:
                    return False

            elif field == 'pid':
                if chars != 9 or not value.isnumeric():
                    return False

    return True


def main():
    passports = loadPassports('passports.txt')

    print('Passports: ', len(passports))

    # Validate passports
    count = 0
    for p in passports:
        if validate(p, False):
            count += 1
    print('Valid passports: ', count)


    count = 0
    for p in passports:
        if validate(p, True):
            count += 1
    print('Valid passports: ', count)



if __name__ == '__main__':
    main()