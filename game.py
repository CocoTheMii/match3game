import pygame

# setup classes
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# create game window
pygame.init()
window = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Match 3 Game")

# tile grid parameters
start_x = 10    # starting x of grid
start_y = 10    # starting y of grid
size = 50       # side length of tiles
spacing = 10    # spacing between tiles

# create tiles
tiles = []
all_sprites = pygame.sprite.Group()

for r in range(8):
    tiles.append([])
    for t in range(8):
        x = start_x + (size + spacing) * (t % 8)
        y = start_y + (size + spacing) * (r % 8) 
        tiles[r].append(Tile(x, y, size))
        all_sprites.add(tiles[r][t])

# game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((255,255,255))
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()
