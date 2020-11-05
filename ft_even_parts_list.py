def ft_even_parts_list(mass):
    spisok = []
    for i in mass:
        if i % 2 == 0:
            spisok.append(i)
    return spisok
