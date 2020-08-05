"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """  C - Convert Celsius to Fahrenheit
                F - Convert Fahrenheit to Celsius
                Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = cal_fah(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit =float(input("fahrenheit: "))
            celsius = cal_cel(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def cal_fah(celsius):
    Fahrenheit = celsius * 9.0 / 5 + 32
    return Fahrenheit

def cal_cel(fahrenheit):
    Celsius = 5 / 9 * (fahrenheit - 32)
    return Celsius
main()