import pygame, random



#Player (head) key input
def head_movement(player_x, player_y, speed, keys, direction_x, direction_y):
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        direction_x = 0 - speed
        direction_y = 0

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        direction_x = speed
        direction_y = 0 

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        direction_x = 0
        direction_y = 0 - speed 

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        direction_x = 0
        direction_y = speed

    return direction_x, direction_y


    #segment movment stuff
def segment_updating(player_x, player_y, segments_x, segments_y, SCREEN, GREEN, direction_x, direction_y):
    if direction_x or direction_y != 0:
        segments_x.insert(0, player_x)
        segments_y.insert(0, player_y)
        segments_x.pop()
        segments_y.pop()
        return segments_x, segments_y
    else:
        return segments_x, segments_y
