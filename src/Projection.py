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
        self.fig_edges = np.empty((len(fig), 2))

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
        for i, v in enumerate(self.figure):
            # applying rotation to each vertex
            rotation = np.dot(self.Rx, v) # x rotation
            rotation = np.dot(self.Ry, rotation) # y rotation
            rotation = np.dot(self.Rz, rotation) # z rotation

            # getting x and y coordinates
            x = int(rotation[0] * self.scale) + self.center[0]
            y = int(rotation[1] * self.scale) + self.center[1]

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
        self.Rx = self.Get_Rotation_X(self.x_angle)
        self.Ry = self.Get_Rotation_Y(self.y_angle)
        self.Rz = self.Get_Rotation_Z(self.z_angle)

        # User input
        self.Handle_Input()

        # Drawing
        self.Draw_Vertices()
        self.Draw_Edges()

        