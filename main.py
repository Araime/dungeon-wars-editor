import csv
from os import getcwd, path

import pygame

from button import Button


pygame.init()

clock = pygame.time.Clock()
FPS = 60

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 400

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')

# define game variables
ROWS = 150
TILE_SIZE = 40
LOWER_TILE_TYPES = 67
DECOR_TILE_TYPES = 11
UPPER_TILE_TYPES = 6
COLS = 150
current_tile = 0
level = 1
layer = 'lower'
current_layer_btn = 0
scroll_left = False
scroll_right = False
scroll_up = False
scroll_down = False
scroll = [0, 0]
scroll_speed = 1

# define filepaths
res_dir = path.join(path.dirname(__file__))
img_dir = path.join(res_dir, 'img')
lvl_dir = path.join(getcwd(), 'levels')
lower_tile_dir = path.join(img_dir, 'tile', 'lower')
decor_tile_dir = path.join(img_dir, 'tile', 'decor')
upper_tile_dir = path.join(img_dir, 'tile', 'upper')

# load layers button images
lower_btn_img = pygame.image.load(path.join(img_dir, 'lower-btn.png')).convert_alpha()
decor_btn_img = pygame.image.load(path.join(img_dir, 'decor-btn.png')).convert_alpha()
upper_btn_img = pygame.image.load(path.join(img_dir, 'upper-btn.png')).convert_alpha()

# define empty tile lists
lower_img_list = []
decor_img_list = []
upper_img_list = []

# store lower tiles in a list
for x in range(LOWER_TILE_TYPES):
    img = pygame.image.load(path.join(lower_tile_dir, f'{x}.png')).convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    lower_img_list.append(img)

# store decor tiles in a list
for x in range(DECOR_TILE_TYPES):
    img = pygame.image.load(path.join(decor_tile_dir, f'{x}.png')).convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    decor_img_list.append(img)

# store upper tiles in a list
for x in range(UPPER_TILE_TYPES):
    img = pygame.image.load(path.join(upper_tile_dir, f'{x}.png')).convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    upper_img_list.append(img)

save_img = pygame.image.load(path.join(img_dir, 'save_btn.png')).convert_alpha()
load_img = pygame.image.load(path.join(img_dir, 'load_btn.png')).convert_alpha()

# define colours
BG = (35, 35, 35)
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)

# define font
font = pygame.font.SysFont('Futura', 30)

# create empty tile lists
lower_world_data = []
decor_world_data = []
upper_world_data = []

# lower world layer
for row in range(ROWS):
    r = [-1] * COLS
    lower_world_data.append(r)

# decor world layer
for row in range(ROWS):
    r = [-1] * COLS
    decor_world_data.append(r)

# upper world layer
for row in range(ROWS):
    r = [-1] * COLS
    upper_world_data.append(r)


# function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function for drawing background
def draw_bg():
    screen.fill(BG)


# draw grid
def draw_grid():
    # vertical lines
    for c in range(COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll[0], 0), (c * TILE_SIZE - scroll[0], SCREEN_HEIGHT))
    # horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE - scroll[1]), (SCREEN_WIDTH, c * TILE_SIZE - scroll[1]))


# function for drawing the world tiles
def draw_world():
    # lower
    for y, row in enumerate(lower_world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(lower_img_list[tile], (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))

    # lower
    for y, row in enumerate(decor_world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(decor_img_list[tile], (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))

    # lower
    for y, row in enumerate(upper_world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(upper_img_list[tile], (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))


# create buttons
save_button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50, save_img, 1)
load_button = Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 50, load_img, 1)

# make a button list
# layer buttons
lower_btn = Button(SCREEN_WIDTH + 10, 5, lower_btn_img, 1)
decor_btn = Button(SCREEN_WIDTH + 140, 5, decor_btn_img, 1)
upper_btn = Button(SCREEN_WIDTH + 260, 5, upper_btn_img, 1)
layers_btn_list = [lower_btn, decor_btn, upper_btn]

# lower tile buttons
lower_button_list = []
button_col = 0
button_row = 0
for i in range(len(lower_img_list)):
    tile_button = Button(SCREEN_WIDTH + (50 * button_col) + 25, 50 * button_row + 50, lower_img_list[i], 1)
    lower_button_list.append(tile_button)
    button_col += 1
    if button_col == 7:
        button_col = 0
        button_row += 1

# upper tile buttons
decor_button_list = []
button_col = 0
button_row = 0
for i in range(len(decor_img_list)):
    tile_button = Button(SCREEN_WIDTH + (50 * button_col) + 25, 50 * button_row + 50, decor_img_list[i], 1)
    decor_button_list.append(tile_button)
    button_col += 1
    if button_col == 7:
        button_col = 0
        button_row += 1

# decor tile buttons
upper_button_list = []
button_col = 0
button_row = 0
for i in range(len(upper_img_list)):
    tile_button = Button(SCREEN_WIDTH + (50 * button_col) + 25, 50 * button_row + 50, upper_img_list[i], 1)
    upper_button_list.append(tile_button)
    button_col += 1
    if button_col == 7:
        button_col = 0
        button_row += 1

run = True
while run:

    clock.tick(FPS)

    draw_bg()
    draw_grid()
    draw_world()

    # draw bottom panel
    pygame.draw.rect(screen, BG, (0, SCREEN_HEIGHT, SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))

    draw_text(f'Level: {level}', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 90)
    draw_text('Press UP or DOWN to change level', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 60)
    if path.exists(path.join(lvl_dir, f'level{level}_lower_data.csv')):
        draw_text('File already exists, be careful when saving!', font, RED, 400, SCREEN_HEIGHT + LOWER_MARGIN - 80)

    # save and load data
    if save_button.draw(screen):
        # save level data
        # lower
        with open(path.join(lvl_dir, f'level{level}_lower_data.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in lower_world_data:
                writer.writerow(row)

        # decor
        with open(path.join(lvl_dir, f'level{level}_decor_data.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in decor_world_data:
                writer.writerow(row)

        # upper
        with open(path.join(lvl_dir, f'level{level}_upper_data.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in upper_world_data:
                writer.writerow(row)

    if load_button.draw(screen):
        # load in level data
        # reset scroll back to the start of the level
        scroll = [0, 0]
        save_trigger = 0

        # lower layer
        if path.exists(path.join(lvl_dir, f'level{level}_lower_data.csv')):
            with open(path.join(lvl_dir, f'level{level}_lower_data.csv'), newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        lower_world_data[x][y] = int(tile)
        else:
            print(f"File 'level{level}_lower_data.csv' Doesn't Exist")

        # decor layer
        if path.exists(path.join(lvl_dir, f'level{level}_decor_data.csv')):
            with open(path.join(lvl_dir, f'level{level}_decor_data.csv'), newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        decor_world_data[x][y] = int(tile)
        else:
            print(f"File 'level{level}_decor_data.csv' Doesn't Exist")

        # lower layer
        if path.exists(path.join(lvl_dir, f'level{level}_upper_data.csv')):
            with open(path.join(lvl_dir, f'level{level}_upper_data.csv'), newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        upper_world_data[x][y] = int(tile)
        else:
            print(f"File 'level{level}_upper_data.csv' Doesn't Exist")

    # draw tile panel and tiles
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    # choose a layer button
    if lower_btn.draw(screen):
        current_layer_btn = 0
        layer = 'lower'
        current_tile = 0
    elif decor_btn.draw(screen):
        current_layer_btn = 1
        layer = 'decor'
        current_tile = 0
    elif upper_btn.draw(screen):
        current_layer_btn = 2
        layer = 'upper'
        current_tile = 0

    # highlight the selected layer button
    pygame.draw.rect(screen, RED, layers_btn_list[current_layer_btn].rect, 3)

    # choose a tile from layer tiles
    # lower layer tiles
    if layer == 'lower':
        button_count = 0
        for button_count, i in enumerate(lower_button_list):
            if i.draw(screen):
                current_tile = button_count

        # highlight the selected tile
        pygame.draw.rect(screen, RED, lower_button_list[current_tile].rect, 3)

    # decor layer tiles
    elif layer == 'decor':
        button_count = 0
        for button_count, i in enumerate(decor_button_list):
            if i.draw(screen):
                current_tile = button_count

        # highlight the selected tile
        pygame.draw.rect(screen, RED, decor_button_list[current_tile].rect, 3)

    # decor layer tiles
    elif layer == 'upper':
        button_count = 0
        for button_count, i in enumerate(upper_button_list):
            if i.draw(screen):
                current_tile = button_count

        # highlight the selected tile
        pygame.draw.rect(screen, RED, upper_button_list[current_tile].rect, 3)

    # scroll the map
    if scroll_left and scroll[0] > 0:
        scroll[0] -= 5 * scroll_speed
        if scroll[0] < 0:
            scroll[0] = 0
    if scroll_right and scroll[0] < (COLS * TILE_SIZE) - SCREEN_WIDTH:
        scroll[0] += 5 * scroll_speed
        if scroll[0] > (COLS * TILE_SIZE) - SCREEN_WIDTH:
            scroll[0] = (COLS * TILE_SIZE) - SCREEN_WIDTH
    if scroll_up and scroll[1] > 0:
        scroll[1] -= 5 * scroll_speed
        if scroll[1] < 0:
            scroll[1] = 0
    if scroll_down and scroll[1] < (ROWS * TILE_SIZE) - SCREEN_HEIGHT:
        scroll[1] += 5 * scroll_speed
        if scroll[1] > (ROWS * TILE_SIZE) - SCREEN_HEIGHT:
            scroll[1] = (ROWS * TILE_SIZE) - SCREEN_HEIGHT

    # add new tiles to the screen
    # get mouse position
    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll[0]) // TILE_SIZE
    y = (pos[1] + scroll[1]) // TILE_SIZE

    # check that the coordinates are within the tile area
    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        # update tile value
        if layer == 'lower':
            if pygame.mouse.get_pressed()[0] == 1:
                if lower_world_data[y][x] != current_tile:
                    lower_world_data[y][x] = current_tile
            if pygame.mouse.get_pressed()[2] == 1:
                lower_world_data[y][x] = -1
        elif layer == 'decor':
            if pygame.mouse.get_pressed()[0] == 1:
                if decor_world_data[y][x] != current_tile:
                    decor_world_data[y][x] = current_tile
            if pygame.mouse.get_pressed()[2] == 1:
                decor_world_data[y][x] = -1
        elif layer == 'upper':
            if pygame.mouse.get_pressed()[0] == 1:
                if upper_world_data[y][x] != current_tile:
                    upper_world_data[y][x] = current_tile
            if pygame.mouse.get_pressed()[2] == 1:
                upper_world_data[y][x] = -1

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
                save_trigger = 0
            if event.key == pygame.K_DOWN and level > 1:
                level -= 1
                save_trigger = 0
            if event.key == pygame.K_a:
                scroll_left = True
            if event.key == pygame.K_d:
                scroll_right = True
            if event.key == pygame.K_w:
                scroll_up = True
            if event.key == pygame.K_s:
                scroll_down = True
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                scroll_left = False
            if event.key == pygame.K_d:
                scroll_right = False
            if event.key == pygame.K_w:
                scroll_up = False
            if event.key == pygame.K_s:
                scroll_down = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1

    pygame.display.update()

pygame.quit()
