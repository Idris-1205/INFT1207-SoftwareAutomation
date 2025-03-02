import statistics

def validate_temp(value):
    """Validate if the temperature is within the acceptable range (-50°C to 150°C)."""
    try:
        value = str(value).strip()  # Ensure it's a string before conversion
        temperature = float(value)  # Convert to float
        if -50 <= temperature <= 150:
            return temperature  # Valid temperature
        else:
            return "Out-of-bound"
    except ValueError:
        return "Invalid"

def process_temperatures(temp_list):
    """Process the list of temperatures and return outputs such as min, max, and avg."""
    valid_temps = []
    
    for temp in temp_list:
        temp = str(temp).strip()  # Ensures we are working with a string
        result = validate_temp(temp)  # Pass only cleaned strings

        if result == "Invalid":
            return "Invalid input detected!!"
        elif result == "Out-of-bound":
            return "Out-of-bound value detected!!"
        else:
            valid_temps.append(result)

    if not valid_temps:
        return "No valid input provided."

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

def main():
    """Interactive main function for user input."""
    while True:
        user_input = input("Enter the temperatures separated by a space: ")
        user_temps = user_input.split()
        output = process_temperatures(user_temps)
        print(f"\nResult: {output}\n")

        # Ask if the user wants to continue
        choice = input("Would you like to enter more temperatures? (Yes/No): ").strip().lower()
        if choice == 'no':
            print("\nThank you for using the Temperature Sensor Analysis Tool.\n")
            break

if __name__ == "__main__":
    main()
