FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

def main():
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    print(f"{temp}°{unit} is {convert_to_celsius(temp) if unit=='F' else convert_to_fahrenheit(temp)}°{'C' if unit=='F' else 'F'}")

if __name__ == "__main__":
    main()
