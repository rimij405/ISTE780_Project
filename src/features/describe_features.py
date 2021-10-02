# describe_features.py
#
# Utilities for describing features.

def report_quantiles(price):
    """Report quantiles
    """
    Q0 = price.quantile(0.00)
    Q1 = price.quantile(0.25)
    Q2 = price.quantile(0.50)
    Q3 = price.quantile(0.75)
    Q4 = price.quantile(1.00)
    IQR = Q3 - Q1
    Q34 = Q4 -Q3
    print("Quantiles: 0% [{}], 25% [{}], 50% [{}], 75% [{}], 100% [{}]".format(Q0, Q1, Q2, Q3, Q4))
    print("Inter-quartile Range: {}".format(IQR))
    print("Distance between Q4 and Q3: {}".format(Q34))
    
def describe_price(price):
    """Describe series or dataframe with price
    """
    
    # Missing prices?
    num_na = price.isna().sum()
    print("There are {} records with missing list prices.".format(num_na))
    
    # Report quantiles?
    report_quantiles(price)
    
    return price.describe()

def count(s):
    """Count size.
    """
    return s.shape[0]

def count_above(price, value):
    """Count products with price above value.
    """
    n = count(price[price > value])
    print("There are {} products with prices greater than {}".format(n, value))
    
def count_below(price, value):
    """Count products with price below value.
    """
    n = count(price[price <= value])
    print("There are {} products with prices less than or equal to {}".format(n, value))
    