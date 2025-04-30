# Define the list of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to print all allowed vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
    print("\n********************************")

# Function to display the menu
def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

# Main function to handle the menu selection and program flow
def main():
    while True:
        display_menu()
        
        # Get user input for menu choice
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            
            if choice == 1:
                print_vehicles()
            elif choice == 2:
                print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice, please enter 1 or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the program
if __name__ == "__main__":
    main()
