import math
import scipy.stats as stats

def normal_cumulative_distribution_function(x):
    """Computes the cumulative distribution function (Φ) for the standard normal distribution."""
    return stats.norm.cdf(x)

def probability_stock_price_increase(µ, σ, M):
    """Calculates P(F(M) > F(0)) for lognormal stock price evolution."""
    if M < 1:
        raise ValueError("M must be at least 1 (weeks must be positive).")

    # Compute Z-score
    z_score = math.sqrt(M) * (µ / σ)

    # Compute probability using normal CDF
    probability = normal_cumulative_distribution_function(z_score)

    return z_score, probability

# Example values
print("Assuming this model, with lognormal parameters μ and σ, write a programme to calculate the probability that the price of the share at the end of the M weeks is higher than it is today? Test your programme for μ = 0.0165, σ = 0.0730, M = 2.")

µ = float(input("Enter the value of Mu μ:"))  # Mean growth rate

σ = float(input("Enter the value of Sigma σ:"))  # Volatility

M = float(input("Enter the number of Weeks:"))  # Number of weeks

# Calculate probability
z, prob = probability_stock_price_increase(µ, σ, M)

# Display results
print(f"Z-score: {z:.6f}")
print(f"Probability P(F(M) > F(0)): {prob:.6f}")

