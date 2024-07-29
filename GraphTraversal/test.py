import unittest
from graph_utils import create_directed_graph_from_edges
from bellman_ford import bellman_ford, bellman_ford_with_negative_cycle_detection


class TestBellmanFordWithNegativeEdges(unittest.TestCase):
    def setUp(self):
        self.edges_with_negative_weights = [
            ("A", "B", 4),
            ("A", "C", 2),
            ("B", "C", -5),
            ("B", "D", 10),
            ("C", "E", 3),
            ("E", "D", 4),
            ("D", "F", 11),
        ]
        self.directed_graph_with_negative_weights = create_directed_graph_from_edges(
            self.edges_with_negative_weights
        )
        self.start_node = "A"

    def test_bellman_ford_with_negative_weights(self):
        expected_distances = {"A": 0, "B": 4, "C": -1, "D": 6, "E": 2, "F": 17}
        distances = bellman_ford(
            self.directed_graph_with_negative_weights, self.start_node
        )
        self.assertEqual(distances, expected_distances)

    def test_bellman_ford_with_negative_cycle_detection_with_negative_weights(self):
        expected_distances = {"A": 0, "B": 4, "C": -1, "D": 6, "E": 2, "F": 17}
        distances = bellman_ford_with_negative_cycle_detection(
            self.directed_graph_with_negative_weights, self.start_node
        )
        self.assertEqual(distances, expected_distances)

    def test_bellman_ford_with_negative_cycle(self):
        edges_with_negative_cycle = [("A", "B", 1), ("B", "C", 1), ("C", "A", -3)]
        graph_with_negative_cycle = create_directed_graph_from_edges(
            edges_with_negative_cycle
        )
        distances = bellman_ford_with_negative_cycle_detection(
            graph_with_negative_cycle, "A"
        )
        self.assertEqual(distances["A"], float("-infinity"))
        self.assertEqual(distances["B"], float("-infinity"))
        self.assertEqual(distances["C"], float("-infinity"))


if __name__ == "__main__":
    unittest.main()
