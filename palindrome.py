def is_palindrome(value: str) -> bool:
    """
        This function determines if a word or phrase is a palindrome

        :param value: A string
        :return: A boolean
        """
    lowered = value.lower()
    base = lowered.replace(" ", "")
    if base[::-1] == base:
        return True
    else:
        return False
