def checkio(input):
    
    if input == []: return 0
    return sum(input[0::2]) * input[~0]
