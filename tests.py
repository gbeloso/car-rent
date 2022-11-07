from user import User
from car import Car

def test_rent_car():
    testUser = User('Carlos', 'carlos@teste.com', 'Senha1234')
    testCar = Car('Chevrolet', 'Prisma', 2022, 15.00)
    testUser.rent_car(testCar, '2022-11-05', '2022-11-08')
    assert testUser.rented_car == testCar