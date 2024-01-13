from os.path import dirname
import numpy as np
import matplotlib.pyplot as plt


def fringes_thermal(temps, expansion_coefficient, L0: float | int, wavelength=532e-9):
    """
    Calculates the fringes for the TOTAL thermal expansion of a material.
    Imagine the object being against an immovable object and expanding towards the laser bundle.

    temps: Temeperatures of the object, can be an np.array or int/float
    expansion_coefficient: The expansion coëfficient of the material
    L0: The start length
    wavelength: The wavelength of the laser

    N = 
    """
    s1 = (expansion_coefficient*2*(1/wavelength)*L0)
    return s1*temps


if __name__ == "__main__":

    tmin = 19
    tmax = 30
    T = np.linspace(0, tmax-tmin, 1000)
    material = [[16e-6, 65e-3, "RVS"], 
                [23e-6, 60e-3, "Aluminium"],
                [12e-6, 165e-3, "Staal"]]

    fig, ax1 = plt.subplots()
    fig.set_facecolor("#404040")
    ax1.set_facecolor("#404040")
    ax1.spines['bottom'].set_color("#d8d8d8")
    ax1.spines['top'].set_color('#d8d8d8') 
    ax1.spines['right'].set_color('#d8d8d8')
    ax1.spines['left'].set_color('#d8d8d8')
    ax1.tick_params(axis='x', colors='#d8d8d8')
    ax1.tick_params(axis='y', colors='#d8d8d8')

    for a, l, n in material:
        N = fringes_thermal(T, a, l)
        ax1.plot(T, N, label=f"{n}")
        print(f"{n}: {round(fringes_thermal(1, a, l), 1)} fringes/K")

    ax1.set_title(f"Thermische Uitzetting, Verwachting Franjes", c="#d8d8d8")
    ax1.set_ylim(bottom=0)
    ax1.set_xlim(0, tmax-tmin)
    box1 = ax1.get_position()
    ax1.set_position([box1.x0, box1.y0, box1.width * 0.85, box1.height])
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5),
               reverse=True, title="Materiaal", title_fontsize="large")
    ax1.set_xlabel("Temperatuur Verschil (°C)", c="#d8d8d8")
    ax1.set_ylabel("Franjes (-)", c="#d8d8d8")
    ax1.grid()
    fig.savefig(f"{dirname(__file__)}/Thermal_{tmin}-{tmax}C.png")
    plt.close()

    