import pytest
import sys
import os

# Ensure project root is on sys.path so tests can import package modules
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from dynamic_programming.knapsack_0_1 import knapsack_0_1


def test_knapsack_0_1_basic():
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 6
    assert knapsack_0_1(weights, values, capacity) == 65

def test_knapsack_0_1_example():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    assert knapsack_0_1(weights, values, capacity) == 220

def test_knapsack_0_1_empty():
    assert knapsack_0_1([], [], 10) == 0

def test_knapsack_0_1_zero_capacity():
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 0
    assert knapsack_0_1(weights, values, capacity) == 0

def test_knapsack_0_1_large_capacity():
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 100
    assert knapsack_0_1(weights, values, capacity) == 65

def test_knapsack_0_1_single_item_fits():
    weights = [5]
    values = [10]
    capacity = 5
    assert knapsack_0_1(weights, values, capacity) == 10

def test_knapsack_0_1_single_item_too_heavy():
    weights = [6]
    values = [10]
    capacity = 5
    assert knapsack_0_1(weights, values, capacity) == 0
