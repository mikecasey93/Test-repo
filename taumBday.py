def taumBday(b, w, bc, wc, z):

    base_price = (b * bc) + (w * wc)
    black_to_white = (b * bc) + (w * (bc + z))
    white_to_black = (b * (wc + z)) + (w * wc)


    if base_price < black_to_white and base_price < white_to_black:
        return base_price
    elif white_to_black < base_price and white_to_black < black_to_white:
        return white_to_black
    elif black_to_white < base_price and black_to_white < white_to_black:
        return black_to_white
    else:
        return base_price


taumBday(10,10,1,1,1)
