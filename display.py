import pygame, random
#segment display function
def segment_display(segment_x, segment_y, SCREEN, GREEN):
    for i in range (len(segment_x)):
        pygame.draw.rect(SCREEN, GREEN, (segment_x[i], segment_y[i], 50, 50))

def collision_self(head_x, head_y, segment_x_list, segment_y_list):

def collision_wall(side_length ,head_x, head_y, screen_width, screen_height):
    if head_x < 0:
        return True
    elif (head_x + side_length) > screen_width:
        return True

    if head_y < 0:
        return True
    elif (head_y + side_length) > screen_height:
        return True

#working on collision stuff
# def collision_apple(player_x, player_y, apple_x, apple_y):
