"""
Palindrome Detection Script
============================

This module provides multiple approaches for detecting palindromes in strings.
A palindrome is a word, phrase, number, or sequence of characters that reads
the same backward as forward (e.g., "racecar", "A man a plan a canal Panama").

The script demonstrates several detection methods with varying complexity and
efficiency characteristics, from basic string reversal to optimized two-pointer
approaches that work with phrases and sentences.

Author: Palindrome Detection Team
Version: 1.0
"""

import re
import string


def is_palindrome_basic(text):
    """
    Check if a string is a palindrome using the string reversal method.

    This is the most straightforward approach: reverse the string and compare
    it to the original. While simple and readable, this method creates a new
    string in memory for the reversed version.

    Time Complexity: O(n) - where n is the length of the string
        - Reversing the string takes O(n) time
        - Comparing the two strings takes O(n) time
        - Total: O(n) + O(n) = O(n)

    Space Complexity: O(n)
        - Creates a reversed copy of the string, requiring additional memory
        - The reversed string takes up n characters of space

    Args:
        text (str): The string to check for palindrome property

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome_basic("racecar")
        True
        >>> is_palindrome_basic("hello")
        False
        >>> is_palindrome_basic("a")
        True
        >>> is_palindrome_basic("")
        True

    Edge Cases:
        - Empty string: Returns True (considered a palindrome by convention)
        - Single character: Returns True (always a palindrome)
        - Case-sensitive: "Racecar" would return False (use case-insensitive version)
    """
    # Handle edge case: empty strings are considered palindromes
    if not text:
        return True

    # Python's slice notation [::-1] reverses the string
    # Step -1 means traverse the string backwards from end to start
    reversed_text = text[::-1]

    # Direct string comparison - Python compares character by character
    return text == reversed_text


def is_palindrome_two_pointer(text):
    """
    Check if a string is a palindrome using the two-pointer technique.

    This optimized approach uses two pointers starting from opposite ends of the
    string, moving towards the center. It compares characters at each position
    and stops early if a mismatch is found. This method is more memory-efficient
    than string reversal because it doesn't create a copy of the string.

    Time Complexity: O(n/2) ≈ O(n) - where n is the length of the string
        - In the best case (early mismatch), can return in O(1)
        - In the worst case (is a palindrome), checks n/2 pairs
        - Average case: O(n/2) which simplifies to O(n)

    Space Complexity: O(1)
        - Only uses two integer pointers (left and right)
        - No additional data structures or string copies created
        - Memory usage is constant regardless of input size

    Args:
        text (str): The string to check for palindrome property

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome_two_pointer("racecar")
        True
        >>> is_palindrome_two_pointer("noon")
        True
        >>> is_palindrome_two_pointer("world")
        False

    Edge Cases:
        - Empty string: Returns True immediately (no iterations needed)
        - Single character: Loop doesn't execute, returns True
        - Two characters: Compares once, handles correctly
    """
    # Handle edge case: empty strings are palindromes
    if not text:
        return True

    # Initialize two pointers
    # left starts at the beginning of the string (index 0)
    left = 0
    # right starts at the end of the string (index len(text) - 1)
    right = len(text) - 1

    # Continue while pointers haven't crossed
    # When left >= right, we've checked all necessary pairs
    while left < right:
        # Compare characters at current pointer positions
        if text[left] != text[right]:
            # Mismatch found - not a palindrome
            # Early return saves unnecessary comparisons
            return False

        # Characters match - move pointers toward center
        left += 1   # Move left pointer forward
        right -= 1  # Move right pointer backward

    # All character pairs matched - it's a palindrome
    return True


def is_palindrome_case_insensitive(text):
    """
    Check if a string is a palindrome, ignoring case differences.

    This function extends the basic palindrome check by preprocessing the input
    to handle case variations. "Racecar", "RaceCar", and "RACECAR" are all
    treated as palindromes. The preprocessing step converts all characters to
    lowercase before comparison.

    Time Complexity: O(n)
        - Converting to lowercase: O(n)
        - Two-pointer comparison: O(n)
        - Total: O(n) + O(n) = O(n)

    Space Complexity: O(n)
        - Creates a lowercase copy of the string
        - The normalized string requires n characters of storage

    Args:
        text (str): The string to check for palindrome property

    Returns:
        bool: True if the string is a palindrome (ignoring case), False otherwise

    Examples:
        >>> is_palindrome_case_insensitive("Racecar")
        True
        >>> is_palindrome_case_insensitive("RaceCar")
        True
        >>> is_palindrome_case_insensitive("Hello")
        False
        >>> is_palindrome_case_insensitive("A")
        True

    Edge Cases:
        - Empty string: Returns True
        - Mixed case: "AaBbAa" becomes "aabbaa" - not a palindrome
        - Non-alphabetic characters: Numbers and symbols are case-insensitive anyway
    """
    # Handle edge case: empty strings are palindromes
    if not text:
        return True

    # Preprocessing: normalize to lowercase
    # This ensures 'A' and 'a' are treated as the same character
    normalized = text.lower()

    # Use the efficient two-pointer method on normalized string
    left = 0
    right = len(normalized) - 1

    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_phrase(text):
    """
    Check if a phrase is a palindrome, ignoring spaces, punctuation, and case.

    This is the most sophisticated palindrome checker that handles real-world
    phrases and sentences. It preprocesses the input by:
    1. Converting to lowercase (case-insensitive comparison)
    2. Removing all spaces (so "race car" becomes "racecar")
    3. Removing all punctuation marks (so "A man, a plan!" keeps only letters)

    This allows detection of complex palindromes like:
    - "A man a plan a canal Panama"
    - "Was it a car or a cat I saw?"
    - "Madam, I'm Adam"

    Time Complexity: O(n)
        - Lowercase conversion: O(n)
        - Regex substitution for removing non-alphanumeric: O(n)
        - Two-pointer comparison: O(m) where m ≤ n (cleaned string length)
        - Total: O(n) + O(n) + O(m) = O(n)

    Space Complexity: O(n)
        - Creates intermediate strings during preprocessing
        - Cleaned string requires at most n characters (usually less)

    Args:
        text (str): The phrase or sentence to check for palindrome property

    Returns:
        bool: True if the phrase is a palindrome (ignoring spaces, punctuation,
              and case), False otherwise

    Examples:
        >>> is_palindrome_phrase("A man a plan a canal Panama")
        True
        >>> is_palindrome_phrase("race car")
        True
        >>> is_palindrome_phrase("Was it a car or a cat I saw?")
        True
        >>> is_palindrome_phrase("Hello, World!")
        False
        >>> is_palindrome_phrase("Madam, I'm Adam")
        True

    Edge Cases:
        - Empty string: Returns True
        - Only spaces/punctuation: After cleaning becomes "", returns True
        - Single word: Behaves like case-insensitive check
        - Numbers: Treated as valid characters (kept in cleaned string)
    """
    # Handle edge case: empty strings are palindromes
    if not text:
        return True

    # Preprocessing Step 1: Convert to lowercase
    # This handles case-insensitive comparison (A = a)
    cleaned = text.lower()

    # Preprocessing Step 2: Remove all non-alphanumeric characters
    # This regex pattern [^a-z0-9] matches any character that is NOT:
    # - a lowercase letter (a-z)
    # - a digit (0-9)
    # The re.sub function replaces all matches with empty string ''
    # This removes: spaces, punctuation, special characters
    # Examples:
    #   "A man, a plan!" -> "amanaplan"
    #   "race car" -> "racecar"
    #   "Hello, World!" -> "helloworld"
    cleaned = re.sub(r'[^a-z0-9]', '', cleaned)

    # Edge case check: if all characters were removed, consider it a palindrome
    if not cleaned:
        return True

    # Apply two-pointer technique to cleaned string
    left = 0
    right = len(cleaned) - 1

    while left < right:
        # Compare characters at symmetric positions
        if cleaned[left] != cleaned[right]:
            # Mismatch found in cleaned string
            return False

        # Move pointers toward center
        left += 1
        right -= 1

    # All comparisons passed - it's a palindrome
    return True


def analyze_palindrome(text):
    """
    Comprehensive palindrome analysis with detailed results.

    This utility function runs all available palindrome detection methods
    on the input text and provides a detailed breakdown of results. This is
    useful for understanding how different methods interpret the same input
    and for educational purposes to see the differences between approaches.

    Args:
        text (str): The text to analyze

    Returns:
        dict: A dictionary containing results from all detection methods
            Keys: 'basic', 'two_pointer', 'case_insensitive', 'phrase'
            Values: Boolean results from each method

    Examples:
        >>> analyze_palindrome("Racecar")
        {
            'basic': False,
            'two_pointer': False,
            'case_insensitive': True,
            'phrase': True
        }
    """
    return {
        'basic': is_palindrome_basic(text),
        'two_pointer': is_palindrome_two_pointer(text),
        'case_insensitive': is_palindrome_case_insensitive(text),
        'phrase': is_palindrome_phrase(text)
    }


# Main execution block - runs when script is executed directly
# Does not run when imported as a module
if __name__ == "__main__":
    print("=" * 70)
    print("Palindrome Detection Script - Test Suite")
    print("=" * 70)
    print()

    # Test Case 1: Simple palindrome (lowercase, no spaces)
    print("Test Case 1: Simple palindrome")
    print("-" * 50)
    test1 = "racecar"
    print(f"Input: '{test1}'")
    print(f"Basic method: {is_palindrome_basic(test1)}")
    print(f"Two-pointer method: {is_palindrome_two_pointer(test1)}")
    print(f"Case-insensitive method: {is_palindrome_case_insensitive(test1)}")
    print(f"Phrase method: {is_palindrome_phrase(test1)}")
    print()

    # Test Case 2: Not a palindrome
    print("Test Case 2: Not a palindrome")
    print("-" * 50)
    test2 = "hello"
    print(f"Input: '{test2}'")
    print(f"Basic method: {is_palindrome_basic(test2)}")
    print(f"Two-pointer method: {is_palindrome_two_pointer(test2)}")
    print(f"Case-insensitive method: {is_palindrome_case_insensitive(test2)}")
    print(f"Phrase method: {is_palindrome_phrase(test2)}")
    print()

    # Test Case 3: Palindrome with mixed case
    print("Test Case 3: Palindrome with mixed case")
    print("-" * 50)
    test3 = "RaceCar"
    print(f"Input: '{test3}'")
    print(f"Basic method: {is_palindrome_basic(test3)}")
    print(f"  (False because case-sensitive: 'R' != 'r')")
    print(f"Two-pointer method: {is_palindrome_two_pointer(test3)}")
    print(f"  (False because case-sensitive)")
    print(f"Case-insensitive method: {is_palindrome_case_insensitive(test3)}")
    print(f"  (True because ignores case)")
    print(f"Phrase method: {is_palindrome_phrase(test3)}")
    print(f"  (True because ignores case)")
    print()

    # Test Case 4: Famous palindrome phrase
    print("Test Case 4: Famous palindrome phrase")
    print("-" * 50)
    test4 = "A man a plan a canal Panama"
    print(f"Input: '{test4}'")
    print(f"Basic method: {is_palindrome_basic(test4)}")
    print(f"  (False because spaces and case matter)")
    print(f"Two-pointer method: {is_palindrome_two_pointer(test4)}")
    print(f"  (False because spaces and case matter)")
    print(f"Case-insensitive method: {is_palindrome_case_insensitive(test4)}")
    print(f"  (False because spaces still matter)")
    print(f"Phrase method: {is_palindrome_phrase(test4)}")
    print(f"  (True because ignores spaces and case)")
    print()

    # Test Case 5: Palindrome phrase with punctuation
    print("Test Case 5: Palindrome phrase with punctuation")
    print("-" * 50)
    test5 = "Was it a car or a cat I saw?"
    print(f"Input: '{test5}'")
    print(f"Basic method: {is_palindrome_basic(test5)}")
    print(f"Two-pointer method: {is_palindrome_two_pointer(test5)}")
    print(f"Case-insensitive method: {is_palindrome_case_insensitive(test5)}")
    print(f"Phrase method: {is_palindrome_phrase(test5)}")
    print(f"  (Only phrase method returns True)")
    print()

    # Test Case 6: Single character (edge case)
    print("Test Case 6: Single character (edge case)")
    print("-" * 50)
    test6 = "a"
    print(f"Input: '{test6}'")
    print(f"All methods: {is_palindrome_basic(test6)}")
    print(f"  (Single characters are always palindromes)")
    print()

    # Test Case 7: Empty string (edge case)
    print("Test Case 7: Empty string (edge case)")
    print("-" * 50)
    test7 = ""
    print(f"Input: '{test7}'")
    print(f"All methods: {is_palindrome_basic(test7)}")
    print(f"  (Empty strings are considered palindromes by convention)")
    print()

    # Test Case 8: Numeric palindrome
    print("Test Case 8: Numeric palindrome")
    print("-" * 50)
    test8 = "12321"
    print(f"Input: '{test8}'")
    print(f"Basic method: {is_palindrome_basic(test8)}")
    print(f"Two-pointer method: {is_palindrome_two_pointer(test8)}")
    print(f"  (All methods work with numeric strings)")
    print()

    # Comprehensive analysis example
    print("=" * 70)
    print("Comprehensive Analysis Example")
    print("=" * 70)
    analysis_test = "Madam, I'm Adam"
    print(f"Analyzing: '{analysis_test}'")
    results = analyze_palindrome(analysis_test)
    print("\nResults:")
    for method, result in results.items():
        print(f"  {method:20s}: {result}")
    print()

    print("=" * 70)
    print("Time and Space Complexity Summary")
    print("=" * 70)
    print("Method                  | Time      | Space")
    print("-" * 70)
    print("Basic (reversal)        | O(n)      | O(n)")
    print("Two-pointer             | O(n)      | O(1)")
    print("Case-insensitive        | O(n)      | O(n)")
    print("Phrase (with cleaning)  | O(n)      | O(n)")
    print("-" * 70)
    print("\nRecommendation: Use two-pointer for best space efficiency")
    print("                Use phrase method for real-world text")
    print()
