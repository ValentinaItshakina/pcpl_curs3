class Program:
    """Программа (сторона «много»)"""
    def __init__(self, id, name, size_mb, comp_id):
        self.id = id
        self.name = name
        self.size_mb = size_mb
        self.comp_id = comp_id


class Computer:
    """Компьютер (сторона «один»)"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProgramComputer:
    """Программы на компьютерах для реализации связи многие-ко-многим"""
    def __init__(self, comp_id, prog_id):
        self.comp_id = comp_id
        self.prog_id = prog_id


# Тестовые данные: Компьютеры
comps = [
    Computer(1, 'Аналитический ПК'),
    Computer(2, 'Офисный компьютер'),
    Computer(3, 'Архивный сервер'),
]

# Тестовые данные: Программы
progs = [
    Program(1, 'Антивирус', 150.5, 1),
    Program(2, 'Текстовый редактор', 45.2, 2),
    Program(3, 'Браузер', 300.0, 3),
    Program(4, 'Архиватор', 20.0, 3),
    Program(5, 'УтилитА', 15.0, 1),
]

# Тестовые данные: Связь многие-ко-многим
comps_progs = [
    ProgramComputer(1, 1),
    ProgramComputer(1, 5),
    ProgramComputer(2, 2),
    ProgramComputer(3, 3),
    ProgramComputer(3, 4),
    ProgramComputer(3, 1),
]


def main():
    # 1. Соединение данных один-ко-многим
    one_to_many = [(p.name, p.size_mb, c.name)
                   for c in comps
                   for p in progs
                   if p.comp_id == c.id]
    # 2. Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, cp.comp_id, cp.prog_id)
                         for c in comps
                         for cp in comps_progs
                         if c.id == cp.comp_id]
    many_to_many = [(p.name, p.size_mb, comp_name)
                    for comp_name, comp_id, prog_id in many_to_many_temp
                    for p in progs if p.id == prog_id]
    # Задание 11.1 (Вариант Д.1)
    # Вывести список всех программ, у которых название заканчивается на букву «р», и названия их компьютеров.
    print('Задание 1')
    res_11 = [(p_name, c_name) for p_name, p_size, c_name in one_to_many if p_name[-1] == 'р']
    print(res_11)
    # Задание 11.2 (Вариант Д.2)
    # Вывести список компьютеров со средним размером программ в каждом компьютере,
    # отсортированный по среднему размеру (с округлением до 2 знаков).
    print('\nЗадание 2')
    res_12_unsorted = []
    for c in comps:
        # Фильтруем программы для текущего компьютера
        c_progs = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_progs) > 0:
            c_sizes = [size for _, size, _ in c_progs]
            # Вычисление среднего значения и округление до 2 знаков
            c_sizes_avg = round(sum(c_sizes) / len(c_sizes), 2)
            res_12_unsorted.append((c.name, c_sizes_avg))
    # Сортировка по среднему размеру (по убыванию)
    res_12 = sorted(res_12_unsorted, key=lambda i: i[1], reverse=True)
    print(res_12)
    # Задание 11.3 (Вариант Д.3)
    # Вывести список всех компьютеров, у которых название начинается с буквы «А», и список установленных на них программ.
    print('\nЗадание 3')
    res_13 = {}
    for c in comps:
        if c.name[0] =='А':
            c_progs = list(filter(lambda i: i[2] == c.name, many_to_many))
            c_progs_names = [x for x, _, _ in c_progs]
            res_13[c.name] = c_progs_names
    print(res_13)


if __name__ == '__main__':
    main()