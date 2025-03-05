def reverseString(s: list[str]) -> None:
    """
    Reverses the input list of characters in-place with O(1) extra memory.

    :param s: List of characters
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
