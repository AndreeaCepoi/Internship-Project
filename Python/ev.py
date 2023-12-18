def calculate_range(battery_capacity, energy_consumption, battery_level):
    try:
        estimated_range = (battery_level / 100) * battery_capacity / (energy_consumption / 100)
        return estimated_range
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    try:
        battery_capacity = float(input("Total battery capacity in kwh : "))
        energy_consumption = float(input("Energy Consumption in kwh/100km : "))
        battery_level = float(input("Battery level in % : "))

        estimated_range = calculate_range(battery_capacity, energy_consumption, battery_level)
        print(f"Estimated Range: {estimated_range:.2f} kilometers")

    except ValueError as ve:
        print(f"Error: {ve}. Please enter valid numercial values")
    except Exception as e:
        print(f"Error: {e} An unexpected error occurred")
