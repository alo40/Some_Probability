import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(num_points=100000):
    """Estimate π using the Monte Carlo method."""
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    
    # Compute whether points are inside the quarter circle
    inside_circle = x**2 + y**2 <= 1
    
    # Estimate π
    pi_estimate = (np.sum(inside_circle) / num_points) * 4
    
    return pi_estimate, x, y, inside_circle

def plot_simulation(x, y, inside_circle):
    """Plot the Monte Carlo simulation results."""
    plt.figure(figsize=(14,14))
    plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label="Inside Circle")
    plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label="Outside Circle")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Monte Carlo Simulation for Estimating π")
    plt.show()

def main():
    num_points = 10000  # Adjust as needed
    pi_estimate, x, y, inside_circle = monte_carlo_pi(num_points)
    print(f"Estimated π: {pi_estimate}")
    plot_simulation(x, y, inside_circle)

if __name__ == "__main__":
    main()
