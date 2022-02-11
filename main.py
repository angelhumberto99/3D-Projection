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

    pygame.font.init()
    text = pygame.font.SysFont('Comic Sans MS', 20)
    msg = "Use arrow keys to interact with X and Y rotations"
    msg2 = "Hold Spacebar + arrow keys to rotate Z axis"
    msg3 = "Use the scroll wheel to scale the figure"
    txt_surf = text.render(msg, False, "white")
    txt_surf2 = text.render(msg2, False, "white")
    txt_surf3 = text.render(msg3, False, "white")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEWHEEL:
                projection.scale += event.y

        screen.fill("black") 
        screen.blit(txt_surf, (20, 10))
        screen.blit(txt_surf2, (20, 35))
        screen.blit(txt_surf3, (20, 60))
        projection.Update()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("execute as python main.py <fig.csv>")
        

    