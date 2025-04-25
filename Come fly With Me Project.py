# come_fly_with_me.py

# Define constants
TOTAL_SEATS = 20
FIRST_CLASS_SEATS = [1, 2, 3, 4]         # $50 fee
EMERGENCY_ROW_SEATS = [9, 10, 11, 12]    # Require confirmation
SEAT_PRICE = 0
FIRST_CLASS_FEE = 50

# Track seat availability: 0 = available, 1 = taken
seats = [0] * TOTAL_SEATS

def display_seats():
    print("\nSeat Map (X = taken, O = available):")
    for i in range(TOTAL_SEATS):
        status = "X" if seats[i] else "O"
        print(f"{i+1}:{status}", end="  ")
        if (i + 1) % 4 == 0:
            print()  # New line every 4 seats

def is_seat_valid(seat_num):
    return 1 <= seat_num <= TOTAL_SEATS

def is_seat_taken(seat_num):
    return seats[seat_num - 1] == 1

def mark_seat_taken(seat_num):
    seats[seat_num - 1] = 1

def purchase_seats():
    while True:
        display_seats()
        try:
            selected = input("\nEnter seat numbers to purchase (comma-separated), or 'q' to quit: ")
            if selected.lower() == 'q':
                break

            seat_numbers = list(map(int, selected.split(',')))
            total_cost = 0

            for seat in seat_numbers:
                if not is_seat_valid(seat):
                    print(f"Seat {seat} is invalid.")
                    continue
                if is_seat_taken(seat):
                    print(f"Seat {seat} is already taken.")
                    continue

                # Emergency seat check
                if seat in EMERGENCY_ROW_SEATS:
                    confirm = input(f"Seat {seat} is an emergency exit row. Are you able and willing to assist in case of emergency? (yes/no): ").lower()
                    if confirm != 'yes':
                        print(f"Cannot proceed with seat {seat} without confirmation.")
                        continue

                # First-class fee
                if seat in FIRST_CLASS_SEATS:
                    print(f"Seat {seat} is First Class and has a fee of ${FIRST_CLASS_FEE}.")
                    total_cost += FIRST_CLASS_FEE

                mark_seat_taken(seat)
                print(f"Seat {seat} successfully booked.")

            print(f"Total cost: ${total_cost}")
        except ValueError:
            print("Invalid input. Please enter seat numbers separated by commas.")

# Start the booking system
print("🛫 Welcome to the Airplane Seat Booking System 🛬")
purchase_seats()
print("Thank you for flying with us!")
