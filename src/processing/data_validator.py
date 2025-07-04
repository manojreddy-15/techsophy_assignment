def validate_data(prices):
    return {k: v for k, v in prices.items() if v is not None}