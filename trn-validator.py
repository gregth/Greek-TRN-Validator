def is_valid_trn(trn):
    """"Validates a given TRN, returns True or False.
    Given TRN should be a string, possibly starting with EL."""

    if not isinstance(trn, str):
        raise TypeError(
            "validate_trn()",
            "Error: Input must be a string.")

    # Strip out prefix EL from input, if exists
    if len(trn) == 11 and trn[:2].upper() == "EL":
        trn = trn[2:]

    # Check if TRN consist of 9 digits only
    if not trn.isdigit() or not len(trn) == 9:
        return False

    power = 1
    sum = 0
    # string[::-1] produces the reversed string of string
    # string[1:8][::-1] -> Get the first 8 digits of TRN and reverse them
    for digit in trn[0:8][::-1]:
        power *= 2
        sum += int(digit) * power

    checksum = (sum % 11) % 10
    if int(trn[8]) == checksum:
        return True
    return False
