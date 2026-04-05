from address import Address
from mailing import Mailing

from_addr = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="1",
    apartment="10",
)

to_addr = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="20",
    apartment="15",
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="AB123456789RU",
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)