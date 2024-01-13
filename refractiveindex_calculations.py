"""
Part of repository: 
https://github.com/PierFelix/Interfometer-Refractive-Index-Measurements

@author: PierFelix
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def sqrt(x):
    return x**0.5

def fringes(angle_i, index_of_refraction, thickness, wavelength):
    """
    Calculates the expected amount of fringes, approximates the index of refraction of air as 1. 

    N = (2t / wavelength) * ((n/cos(r)+tan(i)*sin(i)-tan(r)*sin(i)-(n-1)-(1/cos(i)))) \n
    r = arcsin(sin(i)/n)

    thickness: thickness of the material
    index_of_refraction: index of refraction of the material
    wavelength: wavelength of the light emitted by the laser
    angle_i: angle of incidence of the light
    """

    angle_i = (angle_i*np.pi)/180
    sin_i = np.sin(angle_i)
    r = np.arcsin(sin_i/index_of_refraction)
    Alpha = (2*thickness / wavelength)
    #N = (2*thickness / wavelength) * ((index_of_refraction/np.cos(r))+np.tan(angle_i)*sin_i-np.tan(r)*sin_i-(index_of_refraction-1)-(1/np.cos(angle_i)))
    N = (
        Alpha
        - Alpha / np.cos(angle_i)
        + Alpha * index_of_refraction / (np.cos(np.arcsin(np.sin(angle_i) / index_of_refraction)))
        + Alpha * np.tan(angle_i) * np.sin(angle_i)
        - Alpha * np.tan(np.arcsin(np.sin(angle_i)/index_of_refraction)) * np.sin(angle_i)
        - Alpha * index_of_refraction
        )
    # N = -(2 t sin^2(i))/(l n sqrt(1 - (sin^2(i))/n^2)) + (2 n t)/(l sqrt(1 - (sin^2(i))/n^2)) - (2 t sec(i))/l + (2 t sin(i) tan(i))/l - (2 n t)/l + (2 t)/l
    #N = -(2*thickness*np.sin(angle_i)**2)/(wavelength*index_of_refraction*sqrt(1 - (np.sin(angle_i)**2)/index_of_refraction**2)) + (2*index_of_refraction*thickness)/(wavelength*sqrt(1 - (np.sin(angle_i)**2)/index_of_refraction**2)) - (2*thickness*1/(np.cos(angle_i)))/wavelength + (2*thickness*np.sin(angle_i)*np.tan(angle_i))/wavelength - (2*index_of_refraction*thickness)/wavelength + (2*thickness)/wavelength

    return N


def plots(x, y, ax, label="", color = None, linestyle=None) -> None:
    """
    Plots an extra line on the axis.
    """
    ax.plot(x,y, label=f"{label}", c=color, linestyle=linestyle)


def fit(v1, v2, t, w, p0 = None):
    
    v1, v2 = np.array(v1), np.array(v2)
    v1 = v1*np.pi/180
    Alpha = (2*t / w)
    N = (
        (6e6 / 532)
        - (6e6 / 532) / np.cos(v1)
        + (6e6 / 532) * index_of_refraction / (np.cos(np.arcsin(np.sin(v1) / index_of_refraction)))
        + (6e6 / 532) * np.tan(v1) * np.sin(v1)
        - (6e6 / 532) * np.tan(np.arcsin(np.sin(v1)/index_of_refraction)) * np.sin(v1)
        - (6e6 / 532) * index_of_refraction
        )

    A=np.array(
        [np.ones(np.size(v1)),
         1/v1,
         1/(v1**2),
        ]).transpose()

    N = A.transpose()@A
    q = A.transpose()@v2
    [alpha, beta, gamma] = np.linalg.solve(N, q)
    x = np.linspace(v1[0], v1[-1], 10000)
    y = alpha + beta/x + gamma/(x**2)

    print("\nFit parameters voor formule [y = a + b/x + c/x^2]")
    print(*[alpha, beta, gamma])



    popt, pcov = curve_fit(lambda i, n: fringes(i, n, t, w), v1, v2, p0=p0)
    print(popt)
    return popt[0]

if __name__ == "__main__":
    from os.path import dirname

    measurements = np.array([
        [3,	4.5],
        [4,	8.5],
        [5,	12.5],
        [5,	14],
        [5,	13.5],
        [5,	13],
        [5,	12.5],
        [6,	18.5],
        [7,	26],
        [8,	33],
        [9,	42.5],
        [10, 51.5],
        [10, 51.5],
        [10, 52],
        [10, 53],
        [10, 53.5],
        [11, 62.5],
        [12, 65.5],
        [13, 101.5],
        [14, 103.5],
        [15, 120.5],
        [15, 119.5],
        [15, 118.5],
        [15, 118],
        [15, 121],
        [16, 135.5],
        [17, 154],
        [18, 173.5],
        [19, 196],
        [20, 215.5],
        [20, 215],
        [20, 216],
        [20, 216.5],
        [20, 214]

    ])

    t = [2.83] # mm
    wavelength = 532e-6 # mm
    material = "Acrylaat"
    index_of_refraction = 1.48

    min_deg = 0
    max_deg = 20
    steps = 10000
    plot_y_limit = None

    plot = True

    i_deg = np.linspace(min_deg, max_deg, steps)

    fig, ax1 = plt.subplots()
    fig.set_facecolor("#404040")
    ax1.set_facecolor("#404040")
    ax1.spines['bottom'].set_color("#d8d8d8")
    ax1.spines['top'].set_color('#d8d8d8') 
    ax1.spines['right'].set_color('#d8d8d8')
    ax1.spines['left'].set_color('#d8d8d8')
    ax1.tick_params(axis='x', colors='#d8d8d8')
    ax1.tick_params(axis='y', colors='#d8d8d8')

    for j in t:
        N = fringes(i_deg, index_of_refraction, j, wavelength)
        if plot:
            plots(x=i_deg, y=N, ax=ax1, label=f"Theorie", linestyle="--")

    N = fringes(i_deg, fit(measurements[:, 0], measurements[:, 0], t=3.0, w=wavelength, p0=index_of_refraction), 3.0, wavelength)
    #plots(x=i_deg, y=N, ax=ax1, label=f"Fit (3mm)")

    ax1.scatter(measurements[:, 0], measurements[:, 1], c="Red", zorder=2, label="Metingen")

    ax1.set_title(f"Materiaal: {material}, n = {index_of_refraction}, d = {t[0]}mm", c="#d8d8d8")
    ax1.set_ylim(0, plot_y_limit)
    box1 = ax1.get_position()
    ax1.set_position([box1.x0, box1.y0, box1.width * 0.875, box1.height])
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax1.set_xlabel("Hoek (DEG)", c="#d8d8d8")
    ax1.set_ylabel("Franjes (-)", c="#d8d8d8")
    ax1.grid()
    fig.savefig(f"{dirname(__file__)}/Measurement_{material}.png")
    plt.close()
