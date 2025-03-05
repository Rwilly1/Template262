def reverseVowels(s: str) -> str:
    # Set of vowels in both lowercase and uppercase
    vowels = {'a','e','i','o','u','A','E','I','O','U'}

    # Convert string into a list for easier swapping
    arr = list(s)
    left, right = 0, len(arr) - 1

    while left < right:
        # Move left pointer forward until it points to a vowel
        while left < right and arr[left] not in vowels:
            left += 1
        # Move right pointer backward until it points to a vowel
        while left < right and arr[right] not in vowels:
            right -= 1

        # Swap the vowels
        arr[left], arr[right] = arr[right], arr[left]
        # Move pointers inward
        left += 1
        right -= 1

    # Convert the list back to string
    return ''.join(arr)

# ---- Sample Usage ----
print(reverseVowels("hello"))    # "holle"
print(reverseVowels("leetcode")) # "leotcede"
