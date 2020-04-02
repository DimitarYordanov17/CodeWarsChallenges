def rgb(r, g, b):
    hex_value_r = ""
    hex_value_g = ""
    hex_value_b = ""


    if r > 255:
        hex_value_r = hex(255)[2:]
    elif r <= 0:
        hex_value_r = "00"
    else:
        hex_value_r = hex(r)[2:]


    if g > 255:
        hex_value_g = hex(255)[2:]
    elif g <= 0:
        hex_value_g = "00"
    else:
        hex_value_g = hex(g)[2:]

    if b > 255:
        hex_value_b = hex(255)[2:]
    elif b <= 0:
        hex_value_b = "00"
    else:
        hex_value_b = hex(b)[2:]


    return (hex_value_r.zfill(2) + hex_value_g.zfill(2) + hex_value_b.zfill(2)).upper()




print(rgb(148, 0, 211))

