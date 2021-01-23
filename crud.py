from sqlalchemy import func

from models import Ksiezniczki, Smoki


def add_princess(session, imie, czy_dziewica, szerokosc, wysokosc):
    new_princess = Ksiezniczki(
        imie=imie,
        czy_dziewica=czy_dziewica,
        szerokosc=szerokosc,
        wysokosc=wysokosc
    )
    session.add(new_princess)
    session.commit()


def show_sala_bankietowa(session):
    return session.query(Ksiezniczki).all()


def add_dragon(session, szerokosc, wysokosc):
    dragon = Smoki(
        szerokosc=szerokosc,
        wysokosc=wysokosc
    )
    session.add(dragon)
    session.commit()


def find_dragons(session):
    return session.query(Smoki).all()


def eat_princess(session, szerokosc, wysokosc):
    princesses_to_eat = (
        session.query(Ksiezniczki)
        .filter(Ksiezniczki.czy_dziewica == True)
        .filter(func.abs(Ksiezniczki.szerokosc - szerokosc) < 25)
        .filter(func.abs(Ksiezniczki.wysokosc - wysokosc) < 25)
    )
    for princess in princesses_to_eat:
        session.delete(princess)
    session.commit()


if __name__ == '__main__':
    # jeśli chcecie usunąć dane z bazy danych:
    from database import Session
    session = Session()
    session.query(Ksiezniczki).delete()
    session.query(Smoki).delete()
    session.commit()
