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

# create game window
pygame.init()
window = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Match 3 Game")

# tile grid parameters
start_x = 10    # starting x of grid
start_y = 10    # starting y of grid
size = 48       # side length of tiles
spacing = 24    # spacing between tiles

colors = [pygame.Color("#F94144"),
          pygame.Color("#F3722C"),
          pygame.Color("#F8961E"),
          pygame.Color("#F9C74F"),
          pygame.Color("#90BE6D"),
          pygame.Color("#43AA8B"),
          pygame.Color("#577590")]

# create tiles
tiles = pygame.sprite.Group()
selected = pygame.sprite.Group()

for row in range(8):
    for col in range(8):
        x = start_x + (size + spacing) * (col % 8)
        y = start_y + (size + spacing) * (row % 8)
        color = random.choice(colors)
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
                t.check_click(event.pos, selected)
                t.image.fill((255,0,0))
    for t in selected:
        t.image.fill((0,255,0))
    
    window.fill(pygame.Color("#e9ecef"))
    tiles.update()
    tiles.draw(window)
    pygame.display.update()

pygame.quit()
