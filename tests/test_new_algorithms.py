import unittest
from algorithms.graph.bfs_shortest_path import bfs_shortest_path
from algorithms.sliding_window.longest_substring import length_of_longest_substring


class TestNewAlgorithms(unittest.TestCase):
    
    # BFS Tests
    def test_bfs_simple_path(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        # Path: A -> C -> F (length 3, same as A->B->E->F length 4?) No BFS guarantees shortest by edges
        # A->C->F is 2 hops. A->B->E->F is 3 hops.
        # Check: path should be ['A', 'C', 'F'] or ['A', 'B', 'E', 'F']? 
        # BFS explores level by level.
        # Level 0: A
        # Level 1: B, C
        # Level 2: D, E, F (from C)
        # So it finds F at distance 2.
        path = bfs_shortest_path(graph, 'A', 'F')
        self.assertEqual(len(path), 3) # Node count
        self.assertEqual(path, ['A', 'C', 'F'])

    def test_bfs_no_path(self):
        graph = {'A': ['B'], 'B': ['A'], 'C': ['D']}
        self.assertIsNone(bfs_shortest_path(graph, 'A', 'C'))

    # Sliding Window Tests
    def test_longest_substring_basic(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_longest_substring_repeating(self):
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    def test_longest_substring_mixed(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_longest_substring_empty(self):
        self.assertEqual(length_of_longest_substring(""), 0)

    def test_longest_substring_space(self):
        self.assertEqual(length_of_longest_substring(" "), 1)

if __name__ == '__main__':
    unittest.main()
