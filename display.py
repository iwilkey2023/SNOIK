import pygame, random
#segment display function
def segment_display(segment_x, segment_y, SCREEN, GREEN):
    for i in range (len(segment_x)):
        pygame.draw.rect(SCREEN, GREEN, (segment_x[i], segment_y[i], 50, 50))



#working on collision stuff
def collision(player_x, player_y, segments_x, segments_y, apple_x, apple_y):
