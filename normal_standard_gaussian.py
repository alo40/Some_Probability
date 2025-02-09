import numpy as np
import matplotlib.pyplot as plt

# # Simulate rolling a six-sided die 10,000 times
# num_rolls = 100000
# data_uniform = np.random.uniform(-7, 7, size=num_rolls)

# Generate random data from a normal distribution
x_0 = 0     # Mean of the distribution
mu_1 = -4     
mu_2 = 1
mu_3 = 4
sigma_0 = 1     # Standard deviation
sigma_1 = 2   
sigma_2 = 8
sigma_3 = 4
num_samples = 1000  # Number of samples

# prior noise
theta = np.random.normal(x_0, sigma_0, 1)[0]

# gaussian noise
w_1 = np.random.normal(mu_1, sigma_1, num_samples)
w_2 = np.random.normal(mu_2, sigma_2, num_samples)
w_3 = np.random.normal(mu_3, sigma_3, num_samples)

# noise measurement
x_1 = w_1 + theta
x_2 = w_2 + theta
x_3 = w_3 + theta

# estimator
MAP = ((x_1[0] + x_2[0] + x_3[0])/sigma_2**2) / (3/sigma_1**2)

# Set figure size (width=10 inches, height=6 inches)
plt.figure(figsize=(14, 8))

# Plot histogram
# plt.hist(data_uniform, bins=100, density=True)
plt.hist(x_1, bins=100, density=True, label=f"$x_1 = {x_1[0]}$")
plt.hist(x_2, bins=100, density=True, label=f"$x_2 = {x_2[0]}$")
plt.hist(x_3, bins=100, density=True, label=f"$x_3 = {x_3[0]}$")
plt.axvline(x=MAP, color='red', linestyle='dashed', linewidth=2, label="estimator")

# Formatting
plt.ylabel("Probability")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot & legend
plt.legend()
plt.show()
