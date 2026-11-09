from lab_python_fp import field
from lab_python_fp import gen_random
from lab_python_fp import Unique

if __name__ == "__main__":
    # 1
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    field(goods, 'title')
    field(goods, 'title', 'price')

    #2
    print(gen_random(5, 1, 3))

    #3
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

    #4
    result = result_with_lambda = sorted(data, key=abs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda item: abs(item), reverse=True)
    print(result_with_lambda)