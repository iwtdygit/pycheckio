def second_index(text: str, symbol: str) -> [int, None]:
    """
    You are given two strings and you have to find
    an index of the second occurrence
    of the second string in the first one.
    https://py.checkio.org/en/mission/second-index/
    """
    a = text.find(symbol, text.find(symbol)+1)
    return None if a == -1 else a
