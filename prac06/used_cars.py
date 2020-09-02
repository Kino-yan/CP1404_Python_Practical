"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from practicals.prac06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


    limo=Car(100)
    limo.add_fuel(20)
    print("Limo fuel after top up = {}".format(limo.fuel))
    limo.drive(115)
    print("Limo's odometer now = {}".format(limo.odometer))
    print("Limo fuel after driving = {}".format(limo.fuel))
    limo.__set_name__("BMW")
    my_car.__set_name__("Benz")

    print(my_car)
    print(limo)




main()