import pygame

class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = -3.0
        self.speed = 0.1

    def Handle_Movement(self):
        key = pygame.key.get_pressed()

        # back and forward
        if key[pygame.K_w]:
            self.z += self.speed
        elif key[pygame.K_s]:
            self.z -= self.speed

        # Left and right
        elif key[pygame.K_a]:
            self.x += self.speed
        elif key[pygame.K_d]:
            self.x -= self.speed
        
        # up and down
        elif key[pygame.K_j]:
            self.y += self.speed
        elif key[pygame.K_l]:
            self.y -= self.speed
    
    def Update(self):
        self.Handle_Movement()