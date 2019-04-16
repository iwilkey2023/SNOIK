import pygame, random, movement, display
#snake

#to do:

#segment list functionality stuff 

#collision detection 

#snake growth 

#apple regeneration

#possible backround

#callibration




pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (20, 240, 20)
DARK_GREEN = (0, 100, 0)

#apple location
apple_x = 675
apple_y = 275

#player head x and y
player_x = 375
player_y = 275

#list of all segment locations
#locations will be passed down from segment to segment for movement
segments_x = list((375, 325, 275))
segments_y = list((275, 275, 275))
#player speed will need future calabration
speed = 25

#head direction
direction_x = 0
direction_y = 0

#keyboard input
keys=pygame.key.get_pressed()

#pygame stuff
FPS = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()







while 1 == 1:

    SCREEN.fill(BLACK)
    keys=pygame.key.get_pressed()

    player_x += direction_x
    player_y += direction_y

    display.segment_display(segments_x, segments_y, SCREEN, GREEN)

    pygame.draw.rect(SCREEN, DARK_GREEN, (player_x, player_y, 50, 50))
    pygame.draw.rect(SCREEN, RED, (apple_x, apple_y, 50, 50))
   
    direction_x, direction_y = movement.head_movement(player_x, player_y, speed, keys, direction_x, direction_y)

    segments_x, segments_y = movement.segment_updating(player_x, player_y, segments_x, segments_y, SCREEN, GREEN, direction_x, direction_y)
    
    pygame.display.update()
    clock.tick(FPS)
