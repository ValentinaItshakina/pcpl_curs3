import random

def gen_random(num_count, begin, end):
    rez = [random.randint(begin, end) for i in range(num_count)]
    return rez

def main():
    print(gen_random(5, 1, 3))

if __name__ == '__main__':
    main()
