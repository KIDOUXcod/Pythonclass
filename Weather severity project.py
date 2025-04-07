# Project: Creating a program that calculates weather severity
def weather_severity_project():
    total_rain = 0.0
    total_wind = 0.0
    day_count = 0

    print("Enter rainfall (inches) and wind speed (mph) for each day, seperated by a space.")
    print("Enter -1.0 for rainfall to end data entry.")

    while True:
        input_str = input().strip()
        if not input_str:
            if not input_str:
                continue #skip empty

        try:
                    # split the input into rain and wind values
                parts = input_str.split()
                rain = float(parts[0])

                    #check for sentinel value
                if rain == -1.0:
                    break

                if len(parts) < 2:
                        wind = float(input("Please enter wind speed (mph): for this day"))
                else:
                    wind = float(parts[1])

                    # Add to total
                total_rain += rain
                total_wind += wind
                day_count += 1

        except (ValueError, IndexError):
                print("Invalid input. Please try again. Enter rainfall and wind speed as two numbers separated by a space.")
                continue

    if day_count == 0:
        print("No weather data entered. Please try again.")
        return


# Calculate averages
    avg_rain = total_rain / day_count
    avg_wind = total_wind / day_count
    severity = (avg_rain * 10) + avg_wind
#Output results
    print(f"\nThe average rainfall is {avg_rain:.1f} inches")
    print(f"The average wind speed is {avg_wind:.1f} mph")
    print(f"The weather severity for these {day_count} readings is {severity:.1f}")

# Finish, Run the program
weather_severity_project()
print("Thank you for using this program!")
print("Weather severity project by Kidmar Desir")