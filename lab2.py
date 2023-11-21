import random

class Hotel:
    def __init__(self, name, services=None):
        self.name = name
        self.services = services or {}

class BusinessHotel(Hotel):
    def __init__(self, name, services=None):
        super().__init__(name, services)
        self.services['business'] = 0.5

class SportHotel(Hotel):
    def __init__(self, name, services=None):
        super().__init__(name, services)
        self.services['sport'] = 0.5

class Service:
    def __init__(self, name, services):
        self.name = name
        self.services = services or {}

    def serve(self, client):
        print(vars(client))
        while any(client.needs.values()):
            for need, need_value in client.needs.items():
                if need in self.services and self.services[need] > 0:
                    if self.services[need] >= need_value:
                        client.needs[need] = 0
                    else:
                        client.needs[need] -= self.services[need]
            client.needs = {k: round(v, 2) for k, v in client.needs.items()}
            print(vars(client))

class BusinessService(Service):
    def __init__(self, name, services=None):
        super().__init__(name, services)

    def serve(self, client):
        super().serve(client)
        if client.role == 'Businessman':
            if 'business' in client.needs and client.needs['business'] > 0:
                print(f"{client.name} has special needs for a businessman.")

class SportService(Service):
    def __init__(self, name, services=None):
        super().__init__(name, services)

    def serve(self, client):
        super().serve(client)
        if client.role == 'Sportsman':
            if 'sport' in client.needs and client.needs['sport'] > 0:
                print(f"{client.name} has special needs for a sportsman.")

class Client:
    def __init__(self, name, needs=None):
        self.name = name
        self.needs = needs or self.generate_random_needs()

    def generate_random_needs(self):
        random_needs = {'eat', 'bar', 'child room', 'massage'}
        random_values = {need: round(random.uniform(0.1, 1.0), 1) for need in random.sample(random_needs, 3)}

        return random_values

class Businessman(Client):
    def __init__(self, name, needs=None):
        super().__init__(name, needs)
        self.role = "Businessman"
        self.needs['business'] = round(random.uniform(0.1, 1.0), 1)

class Sportsman(Client):
    def __init__(self, name, needs=None):
        super().__init__(name, needs)
        self.role = "Sportsman"
        self.needs['sport'] = round(random.uniform(0.1, 1.0), 1)

client = Client("John")
businessman = Businessman("Bob")
busHotel = BusinessHotel("Business Hotel", services={"eat": 0.5, "bar": 0.35, "child room": 0.25, 'massage': 0.5})
hotel = Hotel("Hotel", services={"eat": 0.5, "bar": 0.35, "child room": 0.25, 'massage': 0.5})
service = Service(hotel.name, hotel.services)
busService = BusinessService(busHotel.name, busHotel.services)

service.serve(client)
busService.serve(businessman)
