from operator import itemgetter


def bigger_price(limit: int, data: list) -> list:
    """
    You have a table with all available goods in the store. The data is represented as a list of dicts
    Your mission here is to find the TOP most expensive goods.
    The amount we are looking for will be given as a first argument and the whole data as the second one
    https://py.checkio.org/en/mission/bigger-price/
    """
    return sorted(data, key=itemgetter('price'), reverse=True)[0:limit]