import numpy as np

def Get_Rotation_X(theta):
        return np.array([
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta),  np.cos(theta)]
        ])

def Get_Rotation_Y(theta):
    return np.array([
        [np.cos(theta),  0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)],
    ])

def Get_Rotation_Z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0 , 0, 1]
    ])

def Get_Camera_Rotation(x, y, angle):
    return (x*np.cos(angle) - y*np.sin(angle),
            y*np.cos(angle) + x*np.sin(angle))