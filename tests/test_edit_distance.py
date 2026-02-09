import pytest
import sys
import os

# Ensure project root is on sys.path so tests can import package modules
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from dynamic_programming.edit_distance import edit_distance


def test_edit_distance_basic():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("sunday", "saturday") == 3

def test_edit_distance_same():
    assert edit_distance("abc", "abc") == 0

def test_edit_distance_empty():
    assert edit_distance("", "") == 0
    assert edit_distance("a", "") == 1
    assert edit_distance("", "a") == 1

def test_edit_distance_insert():
    assert edit_distance("abc", "abdc") == 1

def test_edit_distance_delete():
    assert edit_distance("abdc", "abc") == 1

def test_edit_distance_replace():
    assert edit_distance("abc", "adc") == 1

def test_edit_distance_complex():
    assert edit_distance("intention", "execution") == 5
