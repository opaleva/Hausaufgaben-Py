from typing import List


def get_set(animals: List[str]) -> List[str]:
    return list(set(animals))


def get_intersection(birds_1: List[str], birds_2: List[str]) -> str:
    return ', '.join(sorted(list(set(birds_1) & set(birds_2))))


def get_symmetric_difference(birds_1: List[str], birds_2: List[str]) -> str:
    return ', '.join(sorted(list(set(birds_1) ^ set(birds_2))))


def main():
    animals: List[str] = ['Igel', 'Frettchen', 'Flusspferd', 'Nashorn', 'Igel', 'Kaninchen', 'Frettchen']
    print(f'{animals} \n–> {sorted(get_set(animals))}\n')

    birds_1: List[str] = ['Papagei', 'Ente', 'Huhn', 'Pinguin', 'Spatz']
    birds_2: List[str] = ['Eule', 'Gans', 'Pinguin', 'Ente', 'Wellensittich']
    print(f'1st: {birds_1}\n2nd: {birds_2}')
    print(f'–> {get_intersection(birds_1, birds_2)}')
    print(f'–> {get_symmetric_difference(birds_1, birds_2)}')


if __name__ == '__main__':
    main()
