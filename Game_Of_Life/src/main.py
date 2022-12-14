# Will have to put quotation marks around command line arguments
#For example (horizontal blinker): python src/main.py "[(1, 0), (1, 1), (1, 2)]"
import sys, ast, gameoflife # pragma: no cover

def print_cells(bounds, cell_positions): # pragma: no cover
    for i in range(bounds[0][0], bounds[1][0] + 1):
        for j in range(bounds[0][1], bounds[1][1] + 1):
            if (i,j) in cell_positions:
                print("O", end = " ")
            else:
                print("-", end = " ")
        print("\n")

def main(): #pragma: no cover
    inputList = ast.literal_eval( sys.argv[1] )
    cell_positions = inputList
    count = 0

    print("Initial Cells: ")
    while True:
        bounds = gameoflife.get_bounds(cell_positions)
        print_cells(bounds, cell_positions)

        if gameoflife.compute_next_generation(gameoflife.compute_next_generation(cell_positions)) == cell_positions:
            count +=1
        if gameoflife.compute_next_generation(cell_positions) == []:
            statement = "No cells will be alive in the next generation"
            break
        if gameoflife.compute_next_generation(cell_positions) == cell_positions:
            statement = "Stable in the next generation"
            break
        if count == 5:
            statement = "Generations are repeating"
            break
        
        cell_positions = gameoflife.compute_next_generation(cell_positions)
        print("Next Generation:")

    if inputList != [] and count != 5:
        print("Next Generation:")
        print_cells(gameoflife.get_bounds(gameoflife.compute_next_generation(cell_positions)), cell_positions)
    print(statement)

main() # pragma: no cover