def ft_even_index_list(mass):
    spisok = []
    ind = 0
    for i in mass:
        if ind % 2 == 0:
            spisok.append(i)
        ind += 1
    return spisok
