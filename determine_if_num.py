import re


def parse_number(s):
    """
    Regex checks for optional leading negative sign,
    either 1 or more integer OR 0 or more integers followed by
    decimal and one or more integer,
    and checks for an 'e' and a positive or negative integer
    representing scientific notation
    """
    result = re.search("^-?([0-9]+|[0-9]*(\.[0-9]+))(e-?[0-9]+)?$", s)

    if result is None:
        return False
    return True


if __name__ == "__main__":
    # True
    print(parse_number("12.3"))  # Floating Point
    print(parse_number("123"))  # Integer
    print(parse_number("-123"))  # Negative numbers
    print(parse_number("-.3"))  # Negative floating point
    print(parse_number("1.5e5"))  # Scientific notation
    # False
    print(parse_number("12a"))
    print(parse_number("1 2"))  # No space between numbers
    print(parse_number("1e1.2"))  # Exponent can only be an integer (positive or negative or 0)
    print(parse_number(""))  # empty string
