def ft_rshift_list(mass):
    spisok = []
    dlin = len(mass)
    per = 0
    while per + 1 < dlin:
        if per == 0:
            spisok.append(mass[dlin - 1])
            spisok.append(mass[0])
            per += 1
        else:
            spisok.append(mass[per])
            per += 1
    return spisok
