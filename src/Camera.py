import pygame
import numpy as np
from src.Rotations import *

class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = -3.0
        self.speed = 0.1
        self.angle = 0.0
        self.x_rotation = 0.0
        self.y_rotation = 0.0
        self.sens = 500

    def Handle_Movement(self):
        key = pygame.key.get_pressed()

        # back and forward
        if key[pygame.K_w]:
            self.z += self.speed
        elif key[pygame.K_s]:
            self.z -= self.speed

        # Left and right
        elif key[pygame.K_a]:
            self.x -= self.speed
        elif key[pygame.K_d]:
            self.x += self.speed
        
        # up and down
        elif key[pygame.K_SPACE]:
            self.y -= self.speed
        elif key[pygame.K_LSHIFT]:
            self.y += self.speed
    
    def Handle_Rotation(self):
        x, y = pygame.mouse.get_rel()
        self.x_rotation += x / self.sens
        self.y_rotation += y / self.sens

    def Update(self):
        self.Handle_Movement()
        self.Handle_Rotation()