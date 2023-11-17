import unittest
from src import gameoflife

DEAD = gameoflife.CellState.DEAD
ALIVE = gameoflife.CellState.ALIVE


class GameOfLifeTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_dead_cell_behavior(self):
        number_of_live_neighbors_and_next_state = [(0, DEAD), (1, DEAD), (2, DEAD), (5, DEAD), (8, DEAD), (3, ALIVE)]

        for number_of_live_neighbors, next_cell_state in number_of_live_neighbors_and_next_state:
            with self.subTest(msg="next_cell_state for number_of_live_neighbors",
                              number_of_live_neighbors=number_of_live_neighbors):
                self.assertEqual(next_cell_state, gameoflife.next_state(DEAD, number_of_live_neighbors))

    def test_alive_cell_behavior(self):
        number_of_live_neighbors_and_next_state = [(1, DEAD), (4, DEAD), (8, DEAD), (2, ALIVE), (3, ALIVE)]

        for number_of_live_neighbors, next_cell_state in number_of_live_neighbors_and_next_state:
            with self.subTest(msg="next_cell_state for number_of_live_neighbors",
                              number_of_live_neighbors=number_of_live_neighbors):
                self.assertEqual(next_cell_state, gameoflife.next_state(ALIVE, number_of_live_neighbors))

    def test_generate_eight_signals_at_2_3(self):
        position_of_signals = [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]
        self.assertEqual(position_of_signals, gameoflife.generate_neighbor_signals((2, 3)))

    def test_generate_eight_signals_at_3_3(self):
        position_of_signals = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(position_of_signals, gameoflife.generate_neighbor_signals((3, 3)))

    def test_generate_eight_signals_at_2_4(self):
        position_of_signals = [(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]
        self.assertEqual(position_of_signals, gameoflife.generate_neighbor_signals((2, 4)))

    def test_generate_eight_signals_at_0_0(self):
        position_of_signals = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.assertEqual(position_of_signals, gameoflife.generate_neighbor_signals((0, 0)))

    def test_given_no_positions_returns_empty_list(self):
        positions = []
        self.assertEqual([], gameoflife.generate_signals_for_multiple_positions(positions))
    
    def test_given_one_position_returns_eight_signals(self):
        positions = [(2, 3)]
        signals = [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]
        self.assertEqual(signals, gameoflife.generate_signals_for_multiple_positions(positions))

    def test_given_two_positions_returns_sixteen_signals(self):
        positions = [(0, 0), (2, 4)]
        signals = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),
                    (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]
        self.assertEqual(signals, gameoflife.generate_signals_for_multiple_positions(positions))

    def test_given_three_positions_returns_twenty_four_signals(self):
        positions = [(0, 0), (2, 3), (2, 4)]
        signals = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),
                    (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4), 
                    (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]
        self.assertEqual(signals, gameoflife.generate_signals_for_multiple_positions(positions))

    def test_count_live_neighbors_no_positions(self):
        self.assertEqual({}, gameoflife.count_live_neighbors([]))

    def test_count_live_neighbors_one_positions(self):
        self.assertEqual({(0, 0): 1}, gameoflife.count_live_neighbors([(0, 0)]))

    def test_count_live_neighbors_two_same_positions(self):
        self.assertEqual({(0, 0): 2}, gameoflife.count_live_neighbors([(0, 0), (0, 0)]))

    def test_count_live_neighbors_three_positions_with_one_distinct(self):
        self.assertEqual({(0, 0): 2, (0, 1): 1}, gameoflife.count_live_neighbors([(0, 0), (0, 1), (0, 0)]))

    def test_compute_next_generation_block_returns_block(self):
        block = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.assertEqual(block, gameoflife.compute_next_generation(block))

    def test_compute_next_generation_beehive_returns_beehive(self):
        beehive = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]
        self.assertEqual(beehive, gameoflife.compute_next_generation(beehive))

    def test_compute_next_generation_horizontal_blinker_returns_vertical(self):
        horizontal = [(1, 0), (1, 1), (1, 2)]
        vertical = [(0, 1), (1, 1), (2, 1)]
        self.assertEqual(vertical, gameoflife.compute_next_generation(horizontal))

    def test_compute_next_generation_vertical_blinker_returns_horizontal(self):
        vertical = [(0, 1), (1, 1), (2, 1)]
        horizontal = [(1, 0), (1, 1), (1, 2)]
        self.assertEqual(horizontal, gameoflife.compute_next_generation(vertical))

    def test_compute_next_generation_glider_single_top_returns_moving_right(self):
        initial = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        result = [(1, 0), (1, 2), (2, 1), (2, 2), (3, 1)]
        self.assertEqual(result, gameoflife.compute_next_generation(initial))

    def test_get_bounds_empty(self):
        self.assertEqual(((0, 0), (100, 100)), gameoflife.get_bounds([]))

    def test_get_bounds_one_point(self):
        self.assertEqual(((-8, -7), (12, 13)), gameoflife.get_bounds([(2, 3)]))

    def test_get_bounds_two_points(self):
        self.assertEqual(((-9, -8), (13, 15)), gameoflife.get_bounds([(1, 2), (3, 5)]))

    def test_get_bounds_three_points(self):
        self.assertEqual(((-10, -9), (14, 16)), gameoflife.get_bounds([(0, 3), (1, 1), (4, 6)]))

    def test_get_bounds_four_points(self):
        self.assertEqual(((-10, -10), (16, 15)), gameoflife.get_bounds([(0, 3), (2, 0), (4, 5), (6, 2)]))


if __name__ == '__main__':
    unittest.main()
