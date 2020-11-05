def ft_same_parts_list(mass):
    col = False
    vrem = mass[0]
    mass.remove(mass[0])
    for i in mass:
        if i > 0 and vrem > 0 or i < 0 and vrem < 0:
            col = True
        vrem = i
    return col
