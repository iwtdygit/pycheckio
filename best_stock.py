def best_stock(data):
    """
    You are given the current stock prices. You have to find out which stocks cost more.
    Input: The dictionary where the market identifier code is a key and the value is a stock price.
    Output: A string and the market identifier code.
    https://py.checkio.org/en/mission/best-stock/
    """

    return max(data, key=data.get)
