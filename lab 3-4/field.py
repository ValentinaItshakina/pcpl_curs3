def field(items, *args):
    rez = []
    if len(args) == 1:
        for item in items:
            if args[0] in item:
                rez.append(item[args[0]])
        print(*rez)
        return 1
    for item in items:
        prrez = {}
        for a in args:
            if a in item:
                prrez[a] = item[a]
        if prrez:
            rez.append(prrez)
    print(*rez)
    return 1


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    field(goods, 'title')
    field(goods, 'title', 'price')

if __name__ == '__main__':
    main()