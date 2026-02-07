# Longest Common Subsequence (LCS)

## Problem Description

Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

### Examples

- LCS of `"ABCDGH"` and `"AEDFHR"` is `"ADH"` of length 3
- LCS of `"AGGTAB"` and `"GXTXAYB"` is `"GTAB"` of length 4

## Implementation

This implementation provides four different functions:

### 1. `lcs_length(seq1, seq2)`
Returns the length of the longest common subsequence.

**Time Complexity:** O(m*n)  
**Space Complexity:** O(m*n)

### 2. `lcs_string(seq1, seq2)`
Returns the actual longest common subsequence as a string or list.

**Time Complexity:** O(m*n)  
**Space Complexity:** O(m*n)

### 3. `lcs_all(seq1, seq2)`
Returns all possible longest common subsequences (useful when multiple LCS exist).

**Time Complexity:** O(m*n + number of LCS)  
**Space Complexity:** O(m*n)

### 4. `lcs_space_optimized(seq1, seq2)`
Space-optimized version that only returns the length using O(min(m,n)) space.

**Time Complexity:** O(m*n)  
**Space Complexity:** O(min(m,n))

## Usage

```python
from lcs import lcs_length, lcs_string, lcs_all

# Basic usage
seq1 = "AGGTAB"
seq2 = "GXTXAYB"

# Get length
length = lcs_length(seq1, seq2)  # Returns: 4

# Get the LCS string
lcs = lcs_string(seq1, seq2)  # Returns: "GTAB"

# Get all possible LCS
all_lcs = lcs_all(seq1, seq2)  # Returns: {"GTAB"}

# Works with lists too
lcs_string([1, 2, 3, 4], [2, 4, 3])  # Returns: [2, 4]
```

## Running the Code

```bash
# Run the example
python lcs.py

# Run the tests
python -m unittest test_lcs -v
```

## Test Coverage

The test suite includes 30 comprehensive tests covering:
- Basic LCS examples
- Edge cases (empty strings, identical strings, no common subsequence)
- Different data types (strings and lists)
- Long sequences
- Consistency verification between different implementations
- Multiple LCS scenarios

All tests pass successfully ✓

## Algorithm Explanation

The implementation uses **Dynamic Programming** with the following approach:

1. Create a 2D table `dp[m+1][n+1]` where `dp[i][j]` represents the length of LCS of `seq1[0..i-1]` and `seq2[0..j-1]`

2. Fill the table using:
   - If characters match: `dp[i][j] = dp[i-1][j-1] + 1`
   - If characters don't match: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

3. For string reconstruction, backtrack from `dp[m][n]` to find the actual subsequence

## Applications

- Diff utilities (finding differences between files)
- DNA sequence analysis in bioinformatics
- Version control systems
- Plagiarism detection
- Data comparison and synchronization
