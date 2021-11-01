def str_len(str_in: str) -> int:
    """
        Given a string parameter, this function should return the length of the parameter.
        """
    return len(str_in)


def first_char(str_in: str) -> str:
    """
        Given a string parameter, this function should return the first letter of the parameter.
        """
    return str_in[0]


def last_char(str_in: str) -> str:
    """
        Given a string parameter, this function should return the last letter of the parameter..
        """
    last = str_in[len(str_in) - 1]
    return last


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
        This function determines if the substring exists within the string. Returns True or False.
        """
    result = sub_str_in in str_in
    return result


def substring(str_in: str, start: int, stop: int) -> str:
    """
        Returns the substring of a string.

        Keyword arguments:
        str_in -- the string in which to generate a substring from
        start -- starting position of the input parameter to start the substring (inclusive)
        stop -- stopping position of the input parameter to stop the substring (exclusive)
        """
    x = start
    y = stop + 1
    return str_in[x:y]


def opposite_case(str_in: str) -> str:
    """
        Given a string parameter, this function returns the same string back with each letter having the opposite case.
        Example:
        When input = "Python" the function returns "pYTHON"
        """
    str_list = []
    for i in str_in:
        if i.isupper():
            str_list.append(i.lower())
        elif i.islower():
            str_list.append(i.upper())
        else:
            str_list.append(i)
    return ''.join(str_list)
