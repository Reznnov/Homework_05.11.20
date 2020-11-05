def ft_rev_list(mass):
    dlin = len(mass)
    for i in range(dlin - 1, -1, -1):
        mass.append(mass.pop(i))
    return mass


def ft_rev_par_list(mass):
    spisok = []
    dlin = len(mass)
    per = 0
    while per <= dlin:
        if per < dlin:
            spisok.append(mass[per + 1])
            spisok.append(mass[per])
            per += 2
        else:
            per += 1000
    return ft_rev_list(spisok)
