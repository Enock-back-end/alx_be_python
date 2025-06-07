# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def celsius_to_fahrenheit(temp):
    return (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def main():
    print("=== Temperature Conversion Tool ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        temperature = float(input("Enter the temperature to convert: "))

        if choice == 1:
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result:.2f}°F")
        elif choice == 2:
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is {result:.2f}°C")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Call main function
main()
