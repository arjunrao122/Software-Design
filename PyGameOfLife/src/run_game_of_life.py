import pygame
from gameoflife import compute_next_generation

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

screen = pygame.display.set_mode([WIDTH, HEIGHT])


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREY, rect, 1)


def draw_cells(alive_cells):
    for cell in alive_cells:
        rect = pygame.Rect(cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLACK, rect)



def get_cell_position(pos):
    return pos[0] // CELL_SIZE, pos[1] // CELL_SIZE



running = True
simulating = False
alive_cells = set()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not simulating:
                cell_pos = get_cell_position(pygame.mouse.get_pos())
                if cell_pos in alive_cells:
                    alive_cells.remove(cell_pos)
                else:
                    alive_cells.add(cell_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulating = not simulating

    screen.fill(WHITE)

    if simulating:
        alive_cells = set(compute_next_generation(list(alive_cells)))

    draw_cells(alive_cells)
    draw_grid()

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
