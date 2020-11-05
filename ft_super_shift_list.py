def ft_super_shift_list(mass, n):
    spisok = []
    blya = 0
    i = 1
    per = 0
    dlin = len(mass)
    while per + 1 < dlin:
        if blya < n:
            spisok.append(mass[dlin - i])
            i += 1
            blya += 1
        elif per < dlin - n:
            spisok.append(mass[per])
            per += 1
        else:
            per += 1
    return spisok
