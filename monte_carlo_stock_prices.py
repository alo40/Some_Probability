import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_price = 100  # Starting stock price
days = 252          # Number of days to simulate (1 year)
num_simulations = 1000
mu = 0.0002         # Expected daily return
sigma = 0.02        # Daily volatility

# Simulate multiple paths
simulated_prices = np.zeros((days, num_simulations))
simulated_prices[0] = initial_price

for t in range(1, days):
    random_shock = np.random.normal(mu, sigma, num_simulations)
    simulated_prices[t] = simulated_prices[t - 1] * (1 + random_shock)

# Plot the simulations
plt.figure(figsize=(14, 12))
plt.plot(simulated_prices, alpha=0.1, color='blue')
plt.title("Monte Carlo Simulation of Stock Prices")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()
