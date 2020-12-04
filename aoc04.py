import sys


def isValidPassport(passport):
    '''Check whether a passport is valid, i.e. it contains all required fields

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)

    cid (Country ID) is an optional field, passport is still considered valid
        if this field is missing

    :param passport: dictionary with passport fields
    :returns: bool
    '''
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for field_name in required_fields:
        if field_name not in passport:
            return False
    else:
        return True


if __name__ == '__main__':
    passports = sys.stdin.read().split('\n\n')
    valid_count = 0
    for passport in passports:
        passport = passport.strip().replace('\n', ' ')
        fields = passport.split(' ')
        passport_data = {}
        for field in fields:
            name, value = field.split(':')
            passport_data[name] = value

        if isValidPassport(passport):
            valid_count += 1

    print(valid_count)
