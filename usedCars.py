"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""


from Prac07.car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)
    limo = Car(120)
    print("fuel =",limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)

main()