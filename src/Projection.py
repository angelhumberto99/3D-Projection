import pygame
import numpy as np
from src.Camera import Camera
from src.Rotations import *

class Projection:
    def __init__(self, screen, w, h, fig):
        self.screen = screen
        self.center = ((w/2), (h/2))
        self.isometric = False
        self.camera = Camera()
        self.focus = 200
        
        self.x_angle = 0.0
        self.y_angle = 0.0
        self.z_angle = 0.0

        self.rotation_speed = 0.05
        self.scale = 100

        self.figure = fig
        self.fig_edges = np.empty((len(fig), 2))

    

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
        for i, v in enumerate(self.figure):
            # applying rotation to each vertex
            rotation = np.dot(self.Rx, v) # x rotation
            rotation = np.dot(self.Ry, rotation) # y rotation
            rotation = np.dot(self.Rz, rotation) # z rotation

            # getting X, Y and Z coordinates
            x = int(rotation[0] * self.scale)
            y = int(rotation[1] * self.scale)
            z = int(rotation[2] * self.scale)

            # correcting X,Y and Z respect to the camera
            x -= int(self.camera.x * self.scale)
            y -= int(self.camera.y * self.scale)
            z -= int(self.camera.z * self.scale)


            # setting the camera rendering
            if not self.isometric:
                try:
                    f = self.focus / z
                except:
                    f = self.focus / 0.1
            else:
                f = 1

            x = (x * f) + self.center[0]
            y = (y * f) + self.center[1]

            # update edges coordinates
            self.fig_edges[i][0] = x
            self.fig_edges[i][1] = y

            # drawing a circle for each vertex
            pygame.draw.circle(self.screen, "white", (x, y), 5)

    def Draw_Edges(self):
        for i in range(len(self.figure)):
            for j in range(i, len(self.figure)):
                # begin path
                a_x = self.fig_edges[i,0]
                a_y = self.fig_edges[i,1]

                # end path
                b_x = self.fig_edges[j,0]
                b_y = self.fig_edges[j,1]
                
                # draw the line between vertices
                pygame.draw.line(self.screen, "white", (a_x, a_y), (b_x, b_y))


    def Update(self):
        # Getting the x, y and z rotation matrices
        self.Rx = Get_Rotation_X(self.x_angle)
        self.Ry = Get_Rotation_Y(self.y_angle)
        self.Rz = Get_Rotation_Z(self.z_angle)

        # User input
        self.Handle_Input()
        self.camera.Update()

        # Drawing
        self.Draw_Vertices()
        self.Draw_Edges()

        