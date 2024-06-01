import matplotlib.pyplot as plt
import numpy as np


def walking():
    # Create some data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(2.5 * x)
    y2 = np.sin(5.05 * x)

    y = y1 + y2
    # Plot the data
    plt.plot(x, y)
    plt.show()

    return


# walking()
def changeablePlot():

    x = np.linspace(0, 10 * np.pi, 100)
    y = np.sin(x)

    plt.ion()
    fig, ax = plt.subplots()
    (line1,) = ax.plot(x, y, "b-")

    for phase in np.linspace(0, 2 * np.pi, 1000):
        plt.title(f"Freq = {phase+0.5}")
        out = np.sin((0.5 + phase) * x) + y
        line1.set_ydata(out)
        plt.ylim(min(out) - 2, max(out) + 2)
        fig.canvas.draw()
        plt.pause(0.1)  # Add a short pause to improve animation smoothness


# changeablePlot()
walking()
