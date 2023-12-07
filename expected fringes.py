from os.path import dirname
import numpy as np
import matplotlib.pyplot as plt

d = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0] # mm
wavelength = 532e-6 # nm
material = "Acrylic"
n = 1.48899

min_deg = 0
max_deg = 15
steps = 10000
plot_y_limit = 175

sin = np.sin
cos = np.cos
tan = np.tan
arcsin = np.arcsin

i_deg = np.linspace(min_deg, max_deg, steps)
i_rad = (i_deg*np.pi)/180 # numpy only works with radians

def fringes(thickness, index_of_refraction, wavelength, angle_i):
    """
    N = (2d / wavelength) * ((n/cos(r)+tan(i)*sin(i)-tan(r)*sin(i)-(n-1)-(1/cos(i))))
    r = arcsin(sin(i)/n)
    """

    N = (2*thickness / wavelength) * ((index_of_refraction/cos(arcsin(sin(angle_i)/n)))+tan(angle_i)*sin(angle_i)-tan(arcsin(sin(angle_i)/n))*sin(angle_i)-(index_of_refraction-1)-(1/cos(angle_i)))
    return N


def plots(x, y, ax, label="", color = None) -> None:
    """
    Plots an extra line on the axis.
    """
    ax.plot(x,y, label=f"{label}", c=color)


if __name__ == "__main__":
    fig, ax1 = plt.subplots()

    for j in d:
        N = fringes(j, n, wavelength, i_rad)
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
