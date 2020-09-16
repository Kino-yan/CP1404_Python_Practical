from practicals.prac08.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Ben's car", 150, 100)
    bad_car = UnreliableCar("Jane's car", 200, 80)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


main()
