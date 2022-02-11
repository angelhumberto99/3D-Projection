import pygame
from sys import exit, argv
import numpy as np
from src.Projection import Projection
import pandas as pd

def Get_Figure_Vertices(filename):
    df = pd.read_csv(filename)
    return np.array([df['x'], df['y'], df['z']]).transpose()

def main(argv):
    pygame.init()

    width = 1200
    height = 700

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("3D Projection")
    clock = pygame.time.Clock()

    fig = Get_Figure_Vertices(argv)

    projection = Projection(screen, width, height, fig)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEWHEEL:
                projection.scale += event.y

        screen.fill("black") 
        projection.Update()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("execute as python main.py <fig.csv>")
        

    