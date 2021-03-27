def build_pyramid(width):
    for i in range(0, width):
        light_row = 2 * ('/' + '█' * i)
        dark_row = 2 * ('▒' * i + '\\')
        print(f'{light_row.rjust(width * 2)}|{dark_row}')


def create_pyramid(width):
    for j in range(width + 1):
        row = '^' * j
        print(f'{row.rjust(width)}')


def main():
    width = 10

    build_pyramid(width)

    create_pyramid(width)


if __name__ == '__main__':
    main()
