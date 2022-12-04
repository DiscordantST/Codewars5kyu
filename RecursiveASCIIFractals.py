def fractalize(seed, i):
    if i <= 1: return seed
    star = fractalize(seed, i-1)
    dot = [row.replace('*','.') for row in star]
    return [
        ''.join(rowrow)
        for row in seed
        for rowrow in zip(*(star if c == '*' else dot for c in row))
    ]