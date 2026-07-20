import numpy as np

weights = np.array([.5, .3, .2])
returns = np.array([.12, .05, -.03])
#Caluculate expected portfolio return
portfolio_return = np.dot(weights, returns)
return_percentage = 100 * portfolio_return


covariance_matrix = np.array([
    [.04, .06, .07],
    [.06, .03, .01],
    [.07, .01, .03]
    ])
#Calculate portfolio variance using the covariance matrix
portfolio_variance = weights.T @ covariance_matrix @ weights

#Convert variance into volatility
portfolio_volatility = np.sqrt(portfolio_variance)
volatility_percentage = 100 * portfolio_volatility

#Calculate sharpe ratio
risk_free_rate = 0.03
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility


print("--------------------")
print("Portfolio Analysis")
print("--------------------")
print()
print(f"Portfolio Return: {return_percentage:.2f}%")
print(f"Portfolio Variance: {portfolio_variance:.4f}")
print(f"Portfolio Volatility: {volatility_percentage:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

