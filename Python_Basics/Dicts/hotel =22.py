hotel = {
    "name": "Hotel Lindora",
    "number_of_stars": 5,
    "rooms": [
        {"number": 101, "floor": 1, "price": 50},
        {"number": 202, "floor": 2, "price": 80}
    ]
}
for rooms in hotel["rooms"]:
    print("habitacion:", rooms["number"])
    print("floor:", rooms["floor"] )
    print("price:", rooms["price"] )