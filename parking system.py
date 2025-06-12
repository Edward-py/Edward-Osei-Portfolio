total_slots = 5  
parking_lot = {}    
available_slots = list(range(1, total_slots + 1))  
 
def park_car():
    if not available_slots:
        print("Parking lot is full.")
        return
 
    license_plate = input("Enter your license plate: ")
    slot = available_slots.pop(0) 
    parking_lot[slot] = license_plate
    print(f"Car {license_plate} parked at slot {slot}.")
 
def remove_car():
    license_plate = input("Enter the license plate of the car you want to remove: ")
 
    for slot, plate in parking_lot.items():
        if plate == license_plate:
            del parking_lot[slot]
            available_slots.append(slot)  # Make the slot available again
            available_slots.sort()  # Keep slots in order
            print(f"Car {license_plate} has left the parking lot.")
            return
    
    print("Car not found.")
 
def main():
    while True:
        print(f"\nAvailable slots: {available_slots}")
        
        choice = input("Do you want to park or unpark a car? (1.park,2.unpark 3.exit): ")
        
        if choice == "1":
            park_car()
        elif choice == "2":
            remove_car()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter '1', '2', or '3'.")
 
if __name__ == "__main__":
    main()