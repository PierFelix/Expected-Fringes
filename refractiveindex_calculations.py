"""
Part of repository: 
https://github.com/PierFelix/Interfometer-Refractive-Index-Measurements

@author: PierFelix
"""

import numpy as np

def refractiveindex(angle, N, thickness, wavelength, deg = True):
    """
    Calculates the refractive index with the following formula:
        n = (8·t²·cos(i) - 8·t² - 4·t·λ·N·cos(i) + 4·t·λ·N - λ²·N²)/(4·t·(2·t·cos(i) - 2·t + λ·N))

    angle: angle of incidence of the light
    N: amount of `bright -> dark -> bright` transitions (or the opposite)
    thickness: thickness of the material
    wavelength: wavelength of the laser
    """
    if deg:
        angle = angle*np.pi/180

    p1 = 8*(thickness**2)
    p2 = 4*thickness*wavelength*N
    p3 = p2 - p1
    cos = np.cos(angle)

    n = (cos*(p1-p2) + p3 -(wavelength * N)**2)/((p1*cos + p3))

    return n

if __name__ == "__main__":
    t = 3 # mm
    l = 532e-6 # mm
    measurements = [
            [10, 10],
            [10, 18],
            [10, 18],
            [6.7, 8],
            [6.7, 9],
            [10, 18],
            [10, 17],
            [10, 19],
            [10, 21]
        ]
        
    for j in measurements:
        print(f"""Deg = {j[0]}, N = {j[1]}
    n = {refractiveindex(*j, t, l)}""")