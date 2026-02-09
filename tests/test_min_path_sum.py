import pytest
import sys
import os

# Ensure project root is on sys.path so tests can import package modules
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from dynamic_programming.min_path_sum import min_path_sum


def test_min_path_sum_basic():
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    assert min_path_sum(grid) == 7

def test_min_path_sum_example2():
    grid = [[1, 2, 3],
            [4, 5, 6]]
    assert min_path_sum(grid) == 12

def test_min_path_sum_single_element():
    grid = [[5]]
    assert min_path_sum(grid) == 5

def test_min_path_sum_single_row():
    grid = [[1, 2, 3, 4]]
    assert min_path_sum(grid) == 10

def test_min_path_sum_single_col():
    grid = [[1],
            [2],
            [3],
            [4]]
    assert min_path_sum(grid) == 10

def test_min_path_sum_empty():
    assert min_path_sum([]) == 0
    assert min_path_sum([[]]) == 0
