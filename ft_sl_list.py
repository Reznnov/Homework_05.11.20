def ft_sl_list(mass):
    col = 0
    vrem = mass[0]
    for i in mass:
        if i > vrem:
            col += 1
        vrem = i
    return col
        
