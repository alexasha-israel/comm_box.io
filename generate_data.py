from faker import Faker
import math
import random


class Generator:

    def __init__(self):
        pass

    def generate_mock_data(self):
        list = []
        faker = Faker()
        list.append(faker.company_email())
        list.append(faker.first_name())
        list.append(faker.last_name())
        list.append(faker.city())
        list.append(faker.country())
        list.append(random.randint(0, math.pow(10, 9)))
        return list

    def identities(self, amount):
        for i in range(amount):
            print(Generator.generate_mock_data(self))
