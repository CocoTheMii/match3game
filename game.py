import pygame
import random
import os

assets = {
    "tile": os.path.join("assets", "tile.png"),
    "selector": os.path.join("assets", "select.png")
    }

# setup classes
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size):
        super().__init__()

        self.image = pygame.image.load(assets["tile"])
        self.image.fill(color, special_flags=pygame.BLEND_MIN)
        self.color = color

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_click(self, mouse, selected_group):
        if self.rect.collidepoint(mouse):
            if selected_group.has(self):
                selected_group.remove(self)
            else:
                selected_group.add(self)
            return(True)
        return(False)

class SelectFrame(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(assets["selector"])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def check_matches(tile_grid, row, col, color):
    match = False

    if row >= 2:
        if tile_grid[row-1][col].color == tile_grid[row-2][col].color == color:
            match = True
            print("MATCH: " + str(row) + " " + str(col) + " " + str(color))
    if col >= 2:
        if tile_grid[row][col-1].color == tile_grid[row][col-2].color == color:
            match = True
            print("MATCH: " + str(row) + " " + str(col) + " " + str(color))
    
    return match

def swap(tile_grid, tiles):
    index = []
    for t in tiles:
        for row in tile_grid:
            for col in row:
                if col == t:
                    break
            else:
                continue
            break
        col = row.index(col)
        row = tile_grid.index(row)
        index.append([row, col])

    pos1 = [tiles[0].rect.x, tiles[0].rect.y]
    pos2 = [tiles[1].rect.x, tiles[1].rect.y]

    tiles[0].rect.x = pos2[0]
    tiles[0].rect.y = pos2[1]
    tiles[1].rect.x = pos1[0]
    tiles[1].rect.y = pos1[1]

    tile_grid[index[0][0]][index[0][1]] = tiles[1]
    tile_grid[index[1][0]][index[1][1]] = tiles[0]

# found the culprit of the square tiles bug!
# some old randomizing code i forgot to update

""" # define functions
def check_matches(tile_grid, grid_size, colors, mode="full"):
    matches = []

    # check for horizontal matches
    if (mode == "row") or (mode == "full"):
        for row in range(grid_size):
            tile_run = []
            for col in range(grid_size):
                t = tile_grid[row][col]
                if (len(tile_run) == 0) or (t.color == tile_run[-1].color):
                    tile_run.append(t)
                else:
                    if len(tile_run) >= 3:
                        matches.append(tile_run)
                    tile_run = [t]

    # check for vertical matches
    if (mode == "col") or (mode == "full"):
        for col in range(grid_size):
            tile_run = []
            for row in range(grid_size):
                t = tile_grid[row][col]
                if (len(tile_run) == 0) or (t.color == tile_run[-1].color):
                    tile_run.append(t)
                else:
                    if len(tile_run) >= 3:
                        matches.append(tile_run)
                    tile_run = [t]
    
    # randomize any matching tiles
    for group in matches:
        for t in group:
            t.color = random.choice(colors)
            t.image.fill(t.color)
    # check again to remove any newly created matches
    if len(matches) > 0:
        check_matches(tile_grid, grid_size, colors) """


# create game window
pygame.init()
window = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Match 3 Game")

# tile grid parameters
start_x = 10    # starting x of grid
start_y = 10    # starting y of grid
size = 48       # side length of tiles
spacing = 24    # spacing between tiles
grid_size = 8   # number of tiles per row/column

colors = [pygame.Color("#ff3355"),  # red
          pygame.Color("#ff8c1a"),  # orange
          pygame.Color("#ffbf00"),  # yellow
          pygame.Color("#59c059"),  # green
          pygame.Color("#0da57a"),  # teal
          pygame.Color("#4d97ff"),  # blue
          pygame.Color("#cf63cf")]  # purple

# create tiles
tile_grid = []
tiles = pygame.sprite.Group()
selected = pygame.sprite.Group()
selectors = pygame.sprite.Group()

for row in range(grid_size):
    tile_grid.append([])
    for col in range(grid_size):
        x = start_x + (size + spacing) * (col % grid_size)
        y = start_y + (size + spacing) * (row % grid_size)

        match = True
        while match:
            color = random.choice(colors)
            match = check_matches(tile_grid, row, col, color)
        
        tile_grid[row].append(Tile(x, y, color, size))
        tiles.add(tile_grid[row][col])

swap(tile_grid, [tile_grid[0][0], tile_grid[0][1]])

# game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for t in tiles:
                click = t.check_click(event.pos, selected)
                if click == True:
                    print(selected)
                    print(t.color)
    selectors.empty()
    if len(selected.sprites()) == 1:
        t = selected.sprites()[0]
        x = t.rect.x - spacing / 2 + 4
        y = t.rect.y - spacing / 2 + 4
        selectors.add(SelectFrame(x, y))
    elif len(selected.sprites()) == 2:
        swap(tile_grid, selected.sprites())
        selected.empty()
            
    
    window.fill(pygame.Color("#e9ecef")) # grey background
    tiles.update()
    tiles.draw(window)
    selectors.update()
    selectors.draw(window)
    pygame.display.update()

pygame.quit()
