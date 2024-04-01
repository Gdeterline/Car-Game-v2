import pygame
import math
from Car import Car

# Mask color range
COLOR_RANGE_START = (0, 100, 0)  # Start color of the range (dark green)
COLOR_RANGE_END = (100, 255, 100)  # End color of the range (light green)


########## Collision Manager class ##########
########## NEEDS TO BE WORKED ON ##########

class CollisionManager():
        
        def __init__(self, car, racetrack):
            self.car = car
            self.racetrack = racetrack
            
            # Définir la plage de couleurs à rendre transparente
            COLOR_RANGE_START = (0, 100, 0)  # Couleur de départ de la plage (vert foncé)
            COLOR_RANGE_END = (100, 255, 100)  # Couleur de fin de la plage (vert clair)

            # Rendre la plage de couleurs transparente dans l'image du circuit
            self.racetrack.set_colorkey(COLOR_RANGE_START, pygame.RLEACCEL)
            self.racetrack.set_colorkey(COLOR_RANGE_END, pygame.RLEACCEL)

            # Créer un masque à partir de l'image du circuit
            def create_mask(image):
                mask = pygame.mask.from_surface(image)
                return mask

            circuit_mask = create_mask(racetrack)
