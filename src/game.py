import pygame
import random
import sys

# Initialisation
pygame.init()

# Parametres
IMAGE_PATH = '../assets/photo.jpg'
CLICK_SOUND_PATH = '../assets/click.wav'
WIN_SOUND_PATH = '../assets/win.wav'
BACKGROUND_MUSIC_PATH = '../assets/background.mp3'

COLS = 5
ROWS = 5
TILE_SIZE = 100
WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Puzzle Game 5x5')

# Load taswira
image = pygame.image.load(IMAGE_PATH)
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

# Load sounds
click_sound = pygame.mixer.Sound(CLICK_SOUND_PATH)
win_sound = pygame.mixer.Sound(WIN_SOUND_PATH)
pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)  # Looping forever

music_on = True

# Create tiles
tiles = []
for row in range(ROWS):
    for col in range(COLS):
        rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        tile = image.subsurface(rect)
        tiles.append(tile)

# Shuffle tiles
empty_tile_index = COLS * ROWS - 1
tile_order = list(range(COLS * ROWS))
tile_order.remove(empty_tile_index)
random.shuffle(tile_order)
tile_order.append(empty_tile_index)

def draw_tiles():
    for index, tile_num in enumerate(tile_order):
        x = (index % COLS) * TILE_SIZE
        y = (index // COLS) * TILE_SIZE
        if tile_num != empty_tile_index:
            screen.blit(tiles[tile_num], (x, y))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (x, y, TILE_SIZE, TILE_SIZE))

def get_clicked_tile(pos):
    x, y = pos
    col = x // TILE_SIZE
    row = y // TILE_SIZE
    index = row * COLS + col
    return index

def is_adjacent(index1, index2):
    row1, col1 = divmod(index1, COLS)
    row2, col2 = divmod(index2, COLS)
    return (abs(row1 - row2) == 1 and col1 == col2) or (abs(col1 - col2) == 1 and row1 == row2)

def is_solved():
    return tile_order == list(range(COLS * ROWS))

# Game Loop
running = True
font = pygame.font.SysFont(None, 60)
won = False

while running:
    screen.fill((255, 255, 255))
    draw_tiles()

    if won:
        text = font.render('Bravo! 🎉', True, (0, 200, 0))
        rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked_index = get_clicked_tile(pygame.mouse.get_pos())
            empty_index = tile_order.index(empty_tile_index)
            if is_adjacent(clicked_index, empty_index) and not won:
                tile_order[empty_index], tile_order[clicked_index] = tile_order[clicked_index], tile_order[empty_index]
                click_sound.play()

            # Bouton mute/unmute music
            if pygame.mouse.get_pos()[0] > WIDTH - 50 and pygame.mouse.get_pos()[1] < 50:
                if music_on:
                    pygame.mixer.music.pause()
                    music_on = False
                else:
                    pygame.mixer.music.unpause()
                    music_on = True

        if not won and is_solved():
            win_sound.play()
            won = True

    # Dessiner mute/unmute button
    pygame.draw.rect(screen, (100, 100, 100), (WIDTH - 50, 0, 50, 50))
    if music_on:
        pygame.draw.line(screen, (255, 255, 255), (WIDTH - 40, 10), (WIDTH - 10, 40), 5)
    else:
        pygame.draw.line(screen, (255, 0, 0), (WIDTH - 40, 10), (WIDTH - 10, 40), 5)
        pygame.draw.line(screen, (255, 0, 0), (WIDTH - 40, 40), (WIDTH - 10, 10), 5)
