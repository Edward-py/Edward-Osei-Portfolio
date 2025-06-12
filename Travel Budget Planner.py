def get_user_input ():
    destination = input("Enter travel destination: ")
    days = int(input("Enter the number of days ypu plan to stay: "))
    budget = float(input("Enter your total budget in £: "))
    return destination, days,budget

def select_options():
    print("\nChoose accommodation type: ")
    print("1. Budget (£50 per night)")
    print("2. Standard (£100 per night)")
    print("3. Luxury (£200 per night)")
    acco_choice = int(input("Enter choice (1-3): "))
    acco_cost = [50, 100, 200][acco_choice - 1]

    print("\nChoose food preference: ")
    print("1. Budget (£20 per day)")
    print("2. Standard (£40 per day)")
    print("3. Luxury (£70 per day)")
    food_choice = int(input("Enter choice (1-3): "))
    food_cost = [20, 40, 70][food_choice - 1]

    print("\nChoose transport type: ")
    print("1. Public Transport (£10 per day)")
    print("2. Rental Car (£50 per day)")
    transport_choice = int(input("Enter choice (1-2): "))
    transport_cost = [10, 50][transport_choice - 1]
 
    return acco_cost, food_cost, transport_cost

def calculate_budget(days, budget, acco_cost, food_cost, transport_cost):
    activity_cost = 30
    total_acco = acco_cost * days
    total_food = food_cost * days
    total_transport = transport_cost * days
    total_activities = activity_cost * days
    total_cost = total_acco + total_food + total_transport + total_activities
    balance = budget - total_cost

    print("\nEstimated Costs:")
    print(f"Accommodation: £{total_acco}")
    print(f"Food: £{total_food}")
    print(f"Transport: £{total_transport}")
    print(f"Activities: £{total_activities}")
    print(f"Total Estimated Cost: £{total_cost}")

    if balance >= 0:
        print(f"You are within budget! Remaining balance: £{balance}")
    else:
        
        print(f"Over budget by £{-balance}! Consider reducing accommodation or activities.")

def main():
    print("Welcome to Travel Budget Planner!")
    destination, days, budget = get_user_input()
    acco_cost, food_cost, transport_cost = select_options()
    calculate_budget(days, budget, acco_cost, food_cost, transport_cost)
 
if __name__ == "__main__":
    main()
 

