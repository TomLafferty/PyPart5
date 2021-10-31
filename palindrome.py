def is_palindrome(value: str) -> bool:
    lowered = value.lower()
    base = lowered.replace(" ","")
    if base[::-1] == base:
        return True
    else:
        return False


    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
      # remove pass statement and implement me
