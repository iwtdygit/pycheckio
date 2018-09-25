def popular_words(text: str, words: list) -> dict:
    """
    At the input of your function are given 2 arguments:
    the text and the array of words the popularity of which you need to determine.
    https://py.checkio.org/en/mission/popular-words/
    """

    return dict([(i, text.lower().split().count(i)) for i in words])
