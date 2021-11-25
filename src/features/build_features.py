# build_features.py
#
# Utilities for building features.
import pandas as pd
import numpy as np

# PRICE BINS.
PRICE_BINS = [0, 25, 50, 100]

GREATER_THAN = "(100, 100+]"

# Prepare categories.
def get_range_label(price):
    """Get the label associated with a specific price.
    """
    value = np.round(price, decimals=1)
    if value <= 25:
        return "(0.00, 25.00]"
    elif value > 25 and value <= 50:
        return "(25.00, 50.00]"
    elif value > 50 and value <= 100:
        return "(50.00, 100.00]"
    else:
        return GREATER_THAN
    
def encode_price(price):
    """Encode the price into bins.
    """
    s = pd.cut(price, PRICE_BINS, right=True)
    s = s.cat.add_categories([GREATER_THAN])
    s = s.fillna(GREATER_THAN)
    s.name = "price_range"
    return s