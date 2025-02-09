import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def setup_plot():
    """Initialize the figure and plot."""
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 100)
    line, = ax.plot(x, np.sin(x))

    # Set axis limits
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.2, 1.2)

    return fig, ax, line, x

def update(frame, line, x):
    """Update the sine wave for animation."""
    line.set_ydata(np.sin(x + frame / 10))  # Shift the sine wave
    return line,

def main():
    fig, ax, line, x = setup_plot()

    ani = animation.FuncAnimation(
        fig, update, frames=100, fargs=(line, x), interval=50, blit=True
    )

    plt.show()

if __name__ == "__main__":
    main()
