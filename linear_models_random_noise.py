import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define parameters
mu_1 = 0      # Mean
mu_2 = 0
sigma_1 = 1   # Standard deviation
sigma_2 = 1

# Generate x values
x = np.linspace(-10, 10, 1000)

# Compute the normal distribution (PDF)
y_1 = norm.pdf(x, mu_1, sigma_1)
y_2 = norm.pdf(x, mu_2, sigma_1)
y_3 = y_1 + y_2

# Plot the distribution
plt.plot(x, y_1, label=f'Normal Distribution\n$\mu_1={mu_1}$, $\sigma_1={sigma_1}$')
plt.plot(x, y_2, label=f'Normal Distribution\n$\mu_2={mu_2}$, $\sigma_2={sigma_2}$')
plt.plot(x, y_3, label=f'$y_1 + y_2$')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.title('Normal (Gaussian) Distribution')
plt.legend()
plt.grid()

# Show the plot
plt.show()
