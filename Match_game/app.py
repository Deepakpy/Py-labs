import pygame
import game_config as gc 
from game_config import MARGIN
from pygame import display, event, image
from animal import Animal 
from time import sleep

def find_index(x,y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    return row * gc.NUM_TILES_SIDE + col
pygame.init()

display.set_caption('My Game')

screen = display.set_mode((512,512))

matched = image.load('other_assets/matched.png')
# screen.blit(matched,(0,0))
# display.flip()
running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images = []
while running:
    current_events=event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.type == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #print(mouse_x,mouse_y)
            index = find_index(mouse_x, mouse_y)
            #print(index)
            if index not in current_images:
                current_images.append(index)
            if len(current_images)>2:
                current_images = current_images[1:]
    screen.fill((255, 255, 255))
    total_skipped = 0
    for tile in tiles:
        image_i = tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE, tile.row * gc.IMAGE_SIZE))
        else:
            total_skipped += 1
    display.flip()
    if len(current_images) == 2:
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip  = True
            tiles[idx2].skip = True
            sleep(0.4)
            screen.blit(matched,(0,0))
            display.flip()
            sleep(0.4)
            current_images = []
    if total_skipped == len(tiles):
        running = False
print('Goodbye!')
