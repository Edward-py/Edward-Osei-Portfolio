tickets = {}  # Dictionary to store tickets with ID as the key
ticket_id = 1  # Auto-incrementing ticket ID
 
def add_ticket():
    global ticket_id
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
 
    tickets[ticket_id] = {
        "Customer": customer_name,
        "Issue": issue_description,
        "Status": "Open"
    }
 
    print(f"Ticket {ticket_id} created successfully!\n")
    ticket_id += 1
 
def view_tickets():
    if not tickets:
        print("No tickets available.\n")
        return
    
    print("Viewing all tickets...")
    for id, details in tickets.items():
        print(f"ID: {id} | Customer: {details['Customer']} | Issue: {details['Issue']} | Status: {details['Status']}")
    print()
 
def close_ticket():
    try:
        id = int(input("Enter Ticket ID to close: "))
        if id in tickets:
            tickets[id]["Status"] = "Closed"
            print(f"Ticket {id} has been closed.\n")
        else:
            print("Ticket ID not found.\n")
    except ValueError:
        print("Invalid input. Please enter a valid Ticket ID.\n")
 
def search_ticket():
    try:
        id = int(input("Enter Ticket ID to search: "))
        if id in tickets:
            details = tickets[id]
            print(f"ID: {id} | Customer: {details['Customer']} | Issue: {details['Issue']} | Status: {details['Status']}\n")
        else:
            print("Ticket ID not found.\n")
    except ValueError:
        print("Invalid input. Please enter a valid Ticket ID.\n")
 
while True:
    print("1. Add Ticket\n2. View Tickets\n3. Close Ticket\n4. Search Ticket\n5. Exit")
    choice = input("Choose an option: ")
 
    if choice == "1":
        add_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        close_ticket()
    elif choice == "4":
        search_ticket()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.\n")
 