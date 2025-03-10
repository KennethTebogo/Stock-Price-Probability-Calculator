# Stock Price Probability Calculator

This Python script calculates the probability that a stock's price at the end of `M` weeks will be higher than its current price, assuming a lognormal stock price evolution model.

## Features
- Computes the Z-score for given mean growth rate (μ), volatility (σ), and number of weeks (M).
- Uses the standard normal cumulative distribution function (CDF) to find the probability.
- Accepts user input for μ, σ, and M.

## Installation
Ensure you have Python installed (>=3.6) along with the required dependencies:
```sh
pip install scipy
```

## Usage
Run the script and provide the required inputs when prompted:
```sh
python stock_price_probability.py
```

### Example Input:
```
Enter the value of Mu μ: 0.0165
Enter the value of Sigma σ: 0.0730
Enter the number of Weeks: 2
```

### Example Output:
```
Z-score: 0.320057
Probability P(F(M) > F(0)): 0.624795
```

## Explanation
- **Z-score Calculation:**
  $$ Z = \sqrt{M} \times \left(\frac{\mu}{\sigma}\right) $$
- **Probability Computation:**
  $$ P(F(M) > F(0)) = \Phi(Z) $$
  where $$ \Phi(Z) $$ is the cumulative distribution function (CDF) of the standard normal distribution.

## License
This project is licensed under the MIT License.

## Author
Kenneth Tebogo Khondowe

