def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
        https://py.checkio.org/en/mission/between-markers/
    """
    a = 0 if begin not in text else text.find(begin)+len(begin)
    b = len(text) if end not in text else text.find(end)
    return text[a:b]
