def libraryFine(d1, m1, y1, d2, m2, y2):

    if d1 > d2 and m1 == m2 and y1 == y2:
        fine = 15 * (d1 - d2)
    elif m1 > m2 and y1 == y2:
        fine = 500 * (m1 - m2)
    elif y1 > y2:
        fine = 10000
    else:
        fine = 0

    return fine

print(libraryFine(9, 6, 2015, 6, 6, 2015))
