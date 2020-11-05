def ft_rev_par_list(mass):
    spisok = []
    dlin = len(mass)
    per = 0
    while per <= dlin:
        print(per)
        print(dlin)
        if per < dlin:
            spisok.append(mass[per + 1])
            spisok.append(mass[per])
            per +=2
            print(spisok)
            print(per)
        else:
            per += 1000
    return spisok[::-1]
