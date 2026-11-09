import random

def gen_random(num_count, begin, end):
    rez = [random.randint(begin, end) for i in range(num_count)]
    return rez

class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        # Получаем параметр ignore_case из kwargs, по умолчанию False
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            # Получаем следующий элемент из итератора/генератора
            item = next(self.items)

            # Определяем ключ для проверки на дубликаты
            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            # Если элемент еще не встречался, запоминаем его ключ и возвращаем оригинал
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self

def main():
    data_nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(f"\n1. Числа (список): {data_nums}")
    print(f"Результат Unique:   {list(Unique(data_nums))}")

    # 2. Пример с генератором
    print("\n2. Генератор случайных чисел (диапазон от 1 до 3):")
    data_gen = gen_random(10, 1, 3)
    # Передаем сам генератор
    print(f"Результат Unique:   {list(Unique(data_gen))}")

    # 3. Пример со строками и разным регистром (ignore_case=False по умолчанию)
    data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"\n3. Строки: {data_str}")
    print(f"Unique(data, ignore_case=False): {list(Unique(data_str, ignore_case=False))}")

    # 4. Пример со строками и ignore_case=True
    print(f"Unique(data, ignore_case=True):  {list(Unique(data_str, ignore_case=True))}")

if __name__ == "__main__":
    main()