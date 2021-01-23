import random

# tą bibliotekę trzeba doinstalować
# będzie nam potrzebna do generowania księżniczek
from faker import Faker

from api import check_temperature
from crud import (
    add_princess,
    add_dragon,
    eat_princess,
    show_sala_bankietowa, find_dragons
)
from database import Session


def generate_random_princess():
    fake = Faker(["pl_PL"])

    return [
        fake.first_name_female(),
        random.choice([True, False]),
        random.randint(-50, 150),
        random.randint(-50, 150),
    ]

def build_kingdom(session):
    # generujemy 100 losowych księżniczek
    princesses = [generate_random_princess() for _ in range(100)]

    dragons = [
        [-22, -43],  # Rio de Janeiro
        [62, 129],  # Jakuck
    ]

    for princess in princesses:
        add_princess(
            session=session,
            imie=princess[0],
            czy_dziewica=princess[1],
            szerokosc=princess[2],
            wysokosc=princess[3]
        )

    for dragon in dragons:
        add_dragon(
            session=session,
            szerokosc=dragon[0],
            wysokosc=dragon[1]
        )


def dragon_hunt(session):
    dragons = find_dragons(session)

    for dragon in dragons:
        temperature = check_temperature(
                szerokosc=int(dragon.szerokosc),
                wysokosc=int(dragon.wysokosc)
            )

        if temperature < 10 or temperature is None:
            # Jeśli jest mniej niż 10 stopni celsjuszsa smok nie wylatuje z pieczary,
            # bo za zimno.
            # Używamy `continue` aby przejść do następnego smoka.
            continue

        eat_princess(session, dragon.szerokosc, dragon.wysokosc)


def make_a_party(session):
    survived_princesses = show_sala_bankietowa(session)
    print("Księżniczki, które przeżyły:")
    for princess in survived_princesses:
        print(
            f"Księżniczka {princess.imie},"
            f" dziewica: {princess.czy_dziewica}"
        )
    print(f"Liczba księżniczek które przeżyły: {len(survived_princesses)}")


if __name__ == '__main__':
    random.seed(0)  # nieistotne
    Faker.seed(0)  # nieistotne
    session = Session()

    build_kingdom(session)
    dragon_hunt(session)
    make_a_party(session)
