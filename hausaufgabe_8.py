from typing import Pattern, List
from random import randint, choice
import re
import string


def check_ip(ip: str, regex_ip: Pattern[str]) -> None:
    if regex_ip.fullmatch(ip):
        print(ip, '–> Valid')
    else:
        print(ip, '–> Invalid')


def check_mac(mac: str, regex_mac: Pattern[str]) -> None:
    if regex_mac.fullmatch(mac):
        print(mac, '–> Valid')
    else:
        print(mac, '–> Invalid')


def get_time(text_time: str, regex_time: Pattern[str]) -> None:
    if regex_time.findall(text_time):
        print('Бессмысленный набор слов с указанием времени в верном формате:'
              '', *re.findall(regex_time, text_time))
    else:
        print('Бессмысленный набор слов и цифр')


def get_sign(text_sign: str, regex_sign: Pattern[str]) -> None:
    if regex_sign.findall(text_sign):
        print('Бессмысленный набор слов с указанием номера в верном формате:'
              '', *re.findall(regex_sign, text_sign))
    else:
        print('Бессмысленный набор слов и цифр')


def get_animals(text_animals: str, regex_animals: Pattern[str]) -> None:
    if regex_animals.findall(text_animals):
        for match in regex_animals.findall(text_animals):
            print('–>', ''.join(match))
    else:
        print('–> In diesem Zoo gibt es keine Tiere, die ich füttern möchte.')


def main():
    ip: str = f'{randint(0, 300)}.{randint(0, 300)}.{randint(0, 300)}.' \
              f'{randint(0, 300)}'
    regex_ip: Pattern[str] = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]'
                                        r'?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]'
                                        r'[0-9]?)$')
    check_ip(ip, regex_ip)

    mac = "%00x:%00x:%00x:%00x:%00x:%00x" % (randint(0, 300), randint(0, 255),
                                             randint(0, 300), randint(0, 255),
                                             randint(0, 300), randint(0, 255))
    regex_mac: Pattern[str] = re.compile(r'([0-9a-fA-F]{2}(:|-|.)){5}[0-9a-fA-F]'
                                         r'{2}')
    check_mac(mac, regex_mac)

    text_time: str = f'{"_"*15}\nТекст01:{randint(0, 12)}1:59 с{randint(0, 2)}' \
                     f'{randint(0, 6)}:{randint(0, 6)}{randint(0, 9)}:' \
                     f'{randint(0, 6)}{randint(0, 9)}какими-то непонятными цифрами'
    regex_time: Pattern[str] = re.compile(r'((?:[0-1][0-9]|2[0-3]):(?:[0-5][0-9])'
                                          r':(?:[0-5][0-9]))|24:00:00')
    print(text_time)
    get_time(text_time, regex_time)

    letters: str = 'АБВГДЕКМНОРСТУХ'
    text_sign: str = f'{"_"*15}\nЕщё одинА000АА77 текст с{choice(letters)}001' \
                     f'{choice(letters)}{choice(letters)}777непонятнымиА9' \
                     f'{randint(0, 12)}0ЕВ05 цифрами'
    # С июня 2020 г. убраны ограничения на коды регионов => '\d{3}'
    regex_sign: Pattern[str] = re.compile(r'([АВЕКМНОРСТУХ]\d{3}(?<!000)'
                                          r'[АВЕКМНОРСТУХ]{2}\d{2,3})')
    print(text_sign)
    get_sign(text_sign, regex_sign)

    animals: List[str] = ['den Löwen', 'den Elefanten', 'die Giraffe',
                          'das Faultier', 'die Schlange', 'das Meerschweinchen']
    text_animals: str = f'{"_"*15}\nIch möchte {choice(animals)} füttern. ' \
                        f'Ich möchte {choice(animals)} nicht füttern. ' \
                        f'Ich möchte vielleicht irgendwie eines Tages ' \
                        f'{choice(animals)} füttern.'
    regex_animals: Pattern[str] = re.compile(r'(Ich\smöchte\s)[^!.?]*?(den\sLöwen'
                                             r'|den\sElefanten|die\sGiraffe)'
                                             r'[^!.?]*?(\sfüttern.)', re.IGNORECASE)
    print(text_animals)
    get_animals(text_animals, regex_animals)
    print('_' * 100)


if __name__ == '__main__':
    a: int = int(input('Какое количество проверок?\n'))
    for _ in range(a):
        main()
