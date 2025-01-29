# %%
import pygame
from Track import Track

pygame.init()

# %%
#######################   Testing Racetrack drawing functionnality   #######################
#######################   Works just as expected - Good news!   ############################

track = Track(1200, 800, 25)
track.surface = pygame.display.set_mode((track.width, track.height))

running = True
while running:

    clock = pygame.time.Clock()
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
            track.save_track()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                track.save_track()
                break

    track.user_track_drawing()
    pygame.display.flip()

    clock.tick(60)
# %%
