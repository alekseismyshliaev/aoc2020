import sys


def validate_byr(byr):
    '''Validate birth year

    :param byr: string
    :returns: bool
    '''
    return (
        len(byr) == 4 and
        byr.isdigit() and
        1920 <= int(byr) <= 2002
    )


def validate_iyr(iyr):
    '''Validate issue year

    :param iyr: string
    :returns: bool
    '''
    return (
        len(iyr) == 4 and
        iyr.isdigit() and
        2010 <= int(iyr) <= 2020
    )


def validate_eyr(eyr):
    '''Validate expiration year

    :param eyr: string
    :returns: bool
    '''
    return (
        len(eyr) == 4 and
        eyr.isdigit() and
        2020 <= int(eyr) <= 2030
    )


def validate_hgt(hgt):
    '''Validate height

    :param hgt: string
    :returns: bool
    '''
    if hgt.endswith('cm'):
        height = hgt[:-2]
        return (
            height.isdigit() and
            150 <= int(height) <= 193
        )
    elif hgt.endswith('in'):
        height = hgt[:-2]
        return (
            height.isdigit() and
            59 <= int(height) <= 76
        )
    else:
        return False


def validate_hcl(hcl):
    '''Validate hair colour

    :param hcl: string
    :returns: bool
    '''
    if hcl.startswith('#'):
        hair_colour = hcl[1:]
        try:
            hex_colour = int(hair_colour, 16)
        except ValueError:
            return False
        else:
            return True
    else:
        return False


def validate_ecl(ecl):
    '''Validate eye colour

    :param ecl: string
    :returns: bool
    '''
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validate_pid(pid):
    '''Validate passport id

    :param pid: string
    :returns: bool
    '''
    return (
        len(pid) == 9 and
        pid.isdigit()
    )


def validate_cid(cid):
    '''Validate country id

    :param cid: string
    :returns: bool
    '''
    return True


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
            validator = globals().get('validate_' + field_name)
            if not validator(passport[field_name]):
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

        if isValidPassport(passport_data):
            valid_count += 1

    print(valid_count)
