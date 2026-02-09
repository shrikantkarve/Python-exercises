"""Edit Distance - dynamic programming exercise.

Function provided: `edit_distance(str1, str2)`
- returns the minimum number of operations (insert, delete, replace) 
  to transform `str1` into `str2`.

Complexity: O(m * n) time, O(m * n) space where m and n are lengths of strings.
"""


def edit_distance(str1: str, str2: str) -> int:
    """Return the minimum edit distance between two strings.

    Args:
        str1: First string.
        str2: Second string.

    Returns:
        Minimum number of operations.

    Examples:
        >>> edit_distance("kitten", "sitting")
        3
        >>> edit_distance("sunday", "saturday")
        3
    """
    m = len(str1)
    n = len(str2)

    # Create a table to store results of subproblems
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill dp[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j],      # Remove
                    dp[i - 1][j - 1]   # Replace
                )

    return dp[m][n]
