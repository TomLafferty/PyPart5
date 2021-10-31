
def str_len(str_in: str) -> int:
    return len(str_in)
    """
    Given a string parameter, this function should return the length of the parameter.
    """
     # remove pass statement and implement me


def first_char(str_in: str) -> str:
    return str_in[0]
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    # remove pass statement and implement me


def last_char(str_in: str) -> str:
    last = str_in[len(str_in) - 1]
    return last
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    # remove pass statement and implement me


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    if str_in.find(sub_str_in) == -1:
        return False
    else:
        return True
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
   # remove pass statement and implement me


def substring(str_in: str, start: int, stop: int) -> str:
    x = start
    y = stop + 1
    return str_in[x:y]
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
     # remove pass statement and implement me


def opposite_case(str_in: str) -> str:
    str_list = []
    for i in str_in:
        if i.isupper():
            str_list.append(i.lower())
        elif i.islower():
            str_list.append(i.upper())
        else:
            str_list.append(i)
    return ''.join(str_list)
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """
     # remove pass statement and implement me

