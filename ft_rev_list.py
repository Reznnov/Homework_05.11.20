def ft_rev_list(mass):
    dlin = len(mass)
    for i in range(dlin - 1, -1, -1):
        mass.append(mass.pop(i))
    return mass
