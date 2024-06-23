"""
File: 13 Wind Chill Calculations
Author: Leonardo Severo

Purpose: Write a program that asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.
"""


def calculate_wind_chill(temperature_F, wind_speed_mph):
    wind_chill = 35.74 + 0.6215 * temperature_F - 35.75 * (wind_speed_mph ** 0.16) + 0.4275 * temperature_F * (wind_speed_mph ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        try:
            temperature_input = input("What is the temperature? (Ex: -10C or 8F) ")
            if temperature_input.lower().endswith('c'):
                temperature_C = float(temperature_input.rstrip("cC"))
                temperature_F = celsius_to_fahrenheit(temperature_C)
            elif temperature_input.lower().endswith('f'):
                temperature_F = float(temperature_input.rstrip("fF"))
            else:
                raise ValueError("Invalid input format. Please enter a valid temperature (Fahrenheit or Celsius).")

            break
        except ValueError as e:
            print(f"Error: {e}")

    wind_speeds_mph = list(range(5, 61, 5))
    
    print("\nWind Chill Values:")
    for wind_speed in wind_speeds_mph:
        wind_chill = calculate_wind_chill(temperature_F, wind_speed)
        print(f"At temperature {temperature_F:.2f}F, and wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")

    while True:
        choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if choice == "yes":
            main()
        elif choice == "no":
            print("Thank you for using the wind chill calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
