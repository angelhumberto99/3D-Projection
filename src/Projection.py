import pygame
import numpy as np

class Projection:
    def __init__(self, screen, w, h, fig):
        self.screen = screen
        self.center = ((w/2), (h/2))

        self.x_angle = 0.0
        self.y_angle = 0.0
        self.z_angle = 0.0

        self.rotation_speed = 0.05
        self.scale = 100

        self.figure = fig

    def Get_Rotation_X(self, theta):
        return np.array([
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta),  np.cos(theta)]
        ])

    def Get_Rotation_Y(self, theta):
        return np.array([
            [np.cos(theta),  0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)],
        ])

    def Get_Rotation_Z(self, theta):
        return np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0 , 0, 1]
        ])

    def Handle_Input(self):
        key = pygame.key.get_pressed()

        # handles Z rotation
        if key[pygame.K_SPACE]:
            if key[pygame.K_LEFT]:
                self.z_angle += self.rotation_speed
            elif key[pygame.K_RIGHT]:
                self.z_angle -= self.rotation_speed
        # handles X rotation
        elif key[pygame.K_LEFT]:
            self.x_angle += self.rotation_speed
        elif key[pygame.K_RIGHT]:
            self.x_angle -= self.rotation_speed
        # handles Y rotation
        elif key[pygame.K_UP]:
            self.y_angle += self.rotation_speed
        elif key[pygame.K_DOWN]:
            self.y_angle -= self.rotation_speed

    def Draw_Vertices(self):
        for v in self.figure:
            # applying rotation to each vertex
            rotation = np.dot(self.Rx, v) # x rotation
            rotation = np.dot(self.Ry, rotation) # y rotation
            rotation = np.dot(self.Rz, rotation) # z rotation

            # getting x and y coordinates
            x = int(rotation[0] * self.scale) + self.center[0]
            y = int(rotation[1] * self.scale) + self.center[1]

            # drawing a circle for each vertex
            pygame.draw.circle(self.screen, "white", (x, y), 5)

    def Update(self):
        # getting the x, y and z rotation matrices
        self.Rx = self.Get_Rotation_X(self.x_angle)
        self.Ry = self.Get_Rotation_Y(self.y_angle)
        self.Rz = self.Get_Rotation_Z(self.z_angle)

        self.Handle_Input()
        self.Draw_Vertices()

        