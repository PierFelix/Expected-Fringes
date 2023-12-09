"""
Part of repository: 
https://github.com/PierFelix/Interfometer-Refractive-Index-Measurements

@author: PierFelix
"""

from expected_fringes import *
from refractiveindex_calculations import *

if __name__ == "__main__":
    from os.path import dirname
    t = [1., 2., 3.] # mm
    wavelength = 532e-6 # mm
    material = "Glass"
    n = 1.5

    min_deg = 0
    max_deg = 10
    steps = 10000
    plot_y_limit = 60

    plot = True

    i_deg = np.linspace(min_deg, max_deg, steps)

    fig, ax1 = plt.subplots()

    table = []
    for j in t:
        N = fringes(j, n, wavelength, i_deg)
        table.append(N[-1])
        if plot:
            plots(x=i_deg, y=N, ax=ax1, label=f"{j} mm")

    ax1.set_title(f"Material: {material}, n = {n}")
    ax1.set_ylim(0, plot_y_limit)
    box1 = ax1.get_position()
    ax1.set_position([box1.x0, box1.y0, box1.width * 0.9, box1.height])
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), reverse=True, title="Thickness", title_fontsize="large")
    ax1.set_xlabel("Angle (DEG)")
    ax1.set_ylabel("Fringes (-)")
    ax1.grid()
    fig.savefig(f"{dirname(__file__)}/{material}.png")
    plt.close()

    print(f"Angle: {max_deg} degrees")
    for j in range(len(t)):
        print(f"{t[j]}mm = {round(table[j], 1)} fringes")
