def ft_len(str):
    num = 0
    for i in str:
        num += 1
    return num


def ft_rev_list(mass):
    dlin = ft_len(mass)
    for i in range(dlin - 1, -1, -1):
        mass.append(mass.pop(i))
    return mass


def ft_rev_par_list(mass):
    spisok = []
    dlin = ft_len(mass)
    per = 0
    while per <= dlin:
        if dlin % 2 == 0:
            if per < dlin:
                spisok.append(mass[per + 1])
                spisok.append(mass[per])
                if dlin % 2 == 0:
                    per += 2
                else:
                    if dlin > per + 3:
                        per += 2
                        spisok.append(mass[per])
                        per += 1000
                    else:
                        per += 2
            else:
                per += 1000
        else:
            if per < dlin:
                spisok.append(mass[per + 1])
                spisok.append(mass[per])
                if dlin > per + 3:
                    per += 2
                else:
                    per += 2
                    spisok.append(mass[per])
                    per += 1000
            else:
                per += 1000
    return spisok
