import pygame
from sys import exit, argv
import numpy as np
from src.Projection import Projection
import pandas as pd

def Get_Figure_Vertices(filename):
    df = pd.read_csv(filename)
    return np.array([df['x'], df['y'], df['z']]).transpose()

def Handle_Info(screen, txt_surf, text):
    msgs = [
        "Arrow keys: X and Y rotation",
        "Space + Arrow left or right: Z rotation",
        "W: foreward",
        "S: backward",
        "A: left",
        "D: right",
        "Spacebar: up",
        "Left shift: down",
        "I: toggle isometric and perspective camera",
        "ESC: enables cursor"
    ] 
    for i, v in enumerate(msgs):
        txt_surf = text.render(v, False, "white")
        screen.blit(txt_surf, (20, 30*(i+1)))

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
    text = pygame.font.SysFont('calibri', 20)
    msg = "Press Tab to show info"
    txt_surf = text.render(msg, False, "white")
    show_info = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    projection.isometric = not projection.isometric
                elif event.key == pygame.K_TAB:
                    show_info = not show_info
                elif event.key == pygame.K_ESCAPE:
                    projection.lock_mouse = not projection.lock_mouse
                    pygame.mouse.set_visible(not projection.lock_mouse)

        screen.fill("black") 
        if show_info:
            Handle_Info(screen, txt_surf, text)
        else:
            screen.blit(txt_surf, (20, 30))
        projection.Update()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("be sure to execute: 'python main.py <fig.csv>'")
        

    