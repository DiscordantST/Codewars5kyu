def rgb(r, g, b):
    c = []
    if r > 255:
        r = 255
    if r < 0:
        r = 0
    c.append(hex(r).upper().replace("0X", "").zfill(2))
    if g > 255:
        g = 255
    if g < 0:
        g = 0
    c.append(hex(g).upper().replace("0X", "").zfill(2))
    if b > 255:
        b = 255
    if b < 0:
        b = 0
    c.append(hex(b).upper().replace("0X", "").zfill(2))
    return "".join(c)

# another aswer
# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))