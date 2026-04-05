from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79990000001"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79990000002"))
catalog.append(Smartphone("Xiaomi", "13 Pro", "+79990000003"))
catalog.append(Smartphone("Google", "Pixel 8", "+79990000004"))
catalog.append(Smartphone("Nothing", "Phone 2", "+79990000005"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")