import pygame
import random

# setup classes
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_click(self, mouse, selected_group):
        if self.rect.collidepoint(mouse):
            if selected_group.has(self):
                selected_group.remove(self)
            else:
                selected_group.add(self)
            print(selected_group)
            return(True)
        return(False)

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
tiles = pygame.sprite.Group()
selected = pygame.sprite.Group()
color_bag = colors
color_index = 0

for row in range(grid_size):
    for col in range(grid_size):
        x = start_x + (size + spacing) * (col % grid_size)
        y = start_y + (size + spacing) * (row % grid_size)
        if color_index == 7:
            random.shuffle(color_bag)
            color_index = 0
        color = color_bag[color_index]
        color_index += 1
        tiles.add(Tile(x, y, color, size))


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
                    t.image.fill((255,0,0))
    for t in selected:
        t.image.fill((0,255,0))
    
    window.fill(pygame.Color("#e9ecef")) # grey background
    tiles.update()
    tiles.draw(window)
    pygame.display.update()

pygame.quit()
