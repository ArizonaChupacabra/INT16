# так
def str_title(t_str: str):
    new_str = [i[0].upper() + i[1:].lower() for i in t_str.split()]
    return new_str


print(' '.join(str_title("тесТОвое задание для pt")))
print(' '.join(str_title(input())))


# или так
def str_title2(t_str: str):
    new_str = [i.capitalize() for i in t_str.split()]
    return new_str


print(' '.join(str_title2("тесТОвое задание для pt")))
print(' '.join(str_title2(input())))
