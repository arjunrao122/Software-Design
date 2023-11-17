from enum import Enum


class CellState(Enum):
    ALIVE = 1
    DEAD = 0


def next_state(current_state, number_of_live_neighbors):
    return CellState.ALIVE if number_of_live_neighbors == 3 or number_of_live_neighbors == 2 and current_state == CellState.ALIVE else CellState.DEAD


def generate_neighbor_signals(cell):
    return [(point, live_neighbors_count)
            for point in list(range(cell[0] - 1, cell[0] + 2))
            for live_neighbors_count in list(range(cell[1] - 1, cell[1] + 2))
            if (point, live_neighbors_count) != cell
            ]


def generate_signals_for_multiple_positions(alive_cells):
    return sum([generate_neighbor_signals(cell) for cell in alive_cells], [])


def count_live_neighbors(position):
    return {key: position.count(key) for key in position}


def compute_next_generation(input_shape):
    return sorted(
        [key for key, value in count_live_neighbors(generate_signals_for_multiple_positions(input_shape)).items()
         if next_state(CellState.ALIVE if key in input_shape else CellState.DEAD, value) == CellState.ALIVE])


def get_bounds(point_list):
    return ((min([point[0] for point in point_list]) - 10, min([point[1] for point in point_list]) - 10), 
            (max([point[0] for point in point_list]) + 10, max([point[1] for point in point_list]) + 10)) if point_list != [] else ((0, 0), (100, 100)) 

