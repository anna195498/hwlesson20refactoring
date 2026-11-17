def avg(numbers):
    """Вычисляет среднее арифметическое списка чисел."""
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)


def find_user(users, name):
    """Ищет пользователя по имени в списке словарей."""
    for u in users:
        if u["name"] == name:
            return u
    return None


class Shop:
    """Класс для хранения и добавления товаров магазина."""

    def __init__(self):
        self.items = []

    def add(self, item, price):
        """Добавляет товар с указанной ценой в список."""
        if price is None:
            return
        self.items.append({"item": item, "price": price})
