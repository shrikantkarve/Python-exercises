# Python Exercises

A collection of Python scripts covering various algorithms, data structures, and utilities.

## 📂 Structure

```
.
├── algorithms/
│   ├── backtracking/   # 8-queens, sudokusolve, towers-of-hanoi
│   ├── graph/          # count_islands, bfs_shortest_path (wip)
│   ├── greedy/         # coin_change
│   ├── math/           # prime_generator, collatz-conjecture
│   └── sorting/        # quicksort
├── dynamic_programming/ # 11+ classic DP problems
├── utils/              # Calculator, myEnumerator, flatten_list
└── tests/              # Unit tests
```

## 🧩 Exercises Inventory

### Dynamic Programming

| Problem | File | Difficulty |
|---|---|---|
| **Edit Distance** | `dynamic_programming/edit_distance.py` | Hard |
| **Knapsack 0/1** | `dynamic_programming/knapsack_0_1.py` | Medium |
| **Longest Incr. Subseq** | `dynamic_programming/longest_increasing_subsequence.py` | Medium |
| **Max Product Subarray** | `dynamic_programming/max_product_subarray.py` | Medium |
| **Min Path Sum** | `dynamic_programming/min_path_sum.py` | Medium |
| **Word Break** | `dynamic_programming/word_break.py` | Medium |
| **Coin Change (Min)** | `dynamic_programming/coin_change_min_coins.py` | Medium |
| **Burst Balloons** | `dynamic_programming/burst_balloons.py` | Hard |
| **Regex Matching** | `dynamic_programming/regex_matching.py` | Hard |
| **Longest Palindromic Subseq** | `dynamic_programming/longest_palindromic_subseq.py` | Medium |
| **Egg Drop** | `dynamic_programming/egg_drop.py` | Hard |
| **LCS** | `lcs.py` | Medium |

### Algorithms & Data Structures

| Problem | Category | File |
|---|---|---|
| **Count Islands** | Graph | `algorithms/graph/count_islands.py` |
| **Quicksort** | Sorting | `algorithms/sorting/qsort.py` |
| **Coin Change (Greedy)** | Greedy | `algorithms/greedy/coin_change.py` |
| **Sudoku Solver** | Backtracking | `algorithms/backtracking/sudokusolve.py` |
| **8 Queens** | Backtracking | `algorithms/backtracking/eight-queens/*.py` |
| **Towers of Hanoi** | Backtracking | `algorithms/backtracking/towers-of-hanoi/*.py` |
| **Prime Generator** | Math | `algorithms/math/prime_generator.py` |
| **Collatz Conjecture** | Math | `algorithms/math/collatz-conjecture.py` |

### Utilities

| utility | File |
|---|---|
| **Calculator** | `utils/Calculator.py` |
| **Custom Enumerator** | `utils/myEnumerator.py` |
| **Flatten List** | `utils/flatten_list.py` |

## 🧪 Testing

Run all tests using `pytest`:

```bash
pytest
```
