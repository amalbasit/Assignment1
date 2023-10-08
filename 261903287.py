## Constants

ALL_FLIGHTS = "all_flights.txt"
USER_BOOKINGS = "user_bookings.txt"


## Read a File

def file_reading(file):

    with open(file, "r") as f:

        lines = f.readlines()

    return lines


## Seating Matrix

def seating_matrix(layout):

    for i in layout:
        for j in i:
            print(j, end = " ")
        print()


## Book a Ticket Function in User Menu

def book_ticket():

    lines = file_reading(ALL_FLIGHTS)

    if len(lines) == 0:

        print("\nThere are no flights in the system.")

    else:

        print("\nAvailable Flights:\n")

        for flight_dict_str in lines:

            flight_dict = eval(flight_dict_str)

            count = 0
            
            for key, value in flight_dict.items():
            
                print(f"{key} : {value}")

                count += 1

                if count == 6:

                    break

            print("\n")

        while True: 

            flight_no = input("\nPlease enter the flight number for the flight you would like to book a seat on: ")

            for flight_dict_str in lines:

                flight_dict = eval(flight_dict_str)

                if flight_dict["Flight Number"] == flight_no:

                    name = input("\nPlease enter your full name: ")

                    print(f"\nSeat Layout - Flight {flight_no}\n")

                    layout = flight_dict["Seat Layout"]

                    seating_matrix(layout)
                
                    print("\nOnly spaces marked with a '*' are available. Please enter the seat number you would like to book below.")

                    while True:

                        while True: 

                            row = int(input("\nRow Number: "))

                            if row > 0 and row < 14:
                                
                                break

                            else: 

                                print("\nInvalid input. Only Rows 1 - 13 are available. Please try again.")

                        while True:

                            column = (input("\nSeat Number: "))

                            if column in "Aa":
                                numcolumn = 1
                                break

                            elif column in "Bb":
                                numcolumn = 2
                                break

                            elif column in "Cc":
                                numcolumn = 3
                                break

                            elif column in "Dd":
                                numcolumn = 4
                                break

                            elif column in "Ee":
                                numcolumn = 5
                                break

                            elif column in "Ff":
                                numcolumn = 6
                                break
                        
                            else:
                                print("\nInvalid input. Only Columns A - F are available. Please try again.")


                        if layout[row][numcolumn] == "X":
                            print("\nThis seat has already been booked. Please try again.")

                        else:
                            layout[row][numcolumn] = "X"
                            break

                    seating_matrix(layout)

                    flight_dict['Seat Layout'] = layout

                    with open(ALL_FLIGHTS, "w") as f:
                                
                        for line in lines:
                                
                                if line.find(flight_no) != -1:
                                    pass
                                else:
                                    f.write(line)

                        f.write(str(flight_dict) + '\n')

                    print("\nYour seat has been booked successfully! Please see below your booking details: \n")
                    print(f"\nName: {name}")
                    print(f"Flight Number: {flight_no}")
                    print(f"Seat Number: {row}{column}")
                    print("\n")

                    with open(USER_BOOKINGS, "a") as f:
                        f.write(f"Name: {name}")
                        f.write(f"Flight Number: {flight_no}")
                        f.write(f"Seat Number: {row}{column}")
                        f.write("\n")

                    break

            else:
                print("\nThis flight does not exist. Please try again.")
                continue

            break


## Cancel a Booking Function in User Menu

def cancel_booking(name, row_no, col_no, flight_no):

    lines = file_reading(USER_BOOKINGS)

    bookings_saved = []

    booking_cancelled = False

    for line in lines:

        if name in line and str(row_no) in line and col_no in line and flight_no in line:

            booking_cancelled = True

        else:
            bookings_saved.append(line)

    if booking_cancelled:

        with open(USER_BOOKINGS, "w") as f:

            f.writelines(bookings_saved)

        print("\nYour booking has been cancelled!")

    else:

        print("\nThere is no booking with those details.")
    
    lines = file_reading(ALL_FLIGHTS)
    
    modified_flight_dicts = []
    
    for flight_dict_str in lines:
        
        flight_dict = eval(flight_dict_str)
        
        if flight_dict["Flight Number"] == flight_no:
            
            layout = flight_dict["Seat Layout"]  
    
            if col_no in "Aa":
                numcolumn = 1

            elif col_no in "Bb":
                numcolumn = 2

            elif col_no in "Cc":
                numcolumn = 3

            elif col_no in "Dd":
                numcolumn = 4

            elif col_no in "Ee":
                numcolumn = 5

            elif col_no in "Ff":
                numcolumn = 6
            
            if layout[int(row_no)][numcolumn] == "X":
                layout[int(row_no)][numcolumn] = "*"

            else:
                print("This seat is already vacant.")
            
            flight_dict['Seat Layout'] = layout


        modified_flight_dicts.append(str(flight_dict) + '\n')


    with open(ALL_FLIGHTS, "w") as f:
        f.writelines(modified_flight_dicts)


## Show All Flights Function in User Menu

def show_all_flights():
    
    lines = file_reading(ALL_FLIGHTS)

    for flight_dict_str in lines:

        flight_dict = eval(flight_dict_str) 
        
        print("\nFlight Details:\n")

        count = 0
        
        for key, value in flight_dict.items():
        
            print(f"{key} : {value}")

            count += 1

            if count == 6:

                print("Seat Layout: ")

                layout = flight_dict["Seat Layout"]

                seating_matrix(layout)

                break

    if len(lines) == 0:

        print("\nThere are no flights in the system.")


## Add a Flight Function in Admin Menu

def add_flight(airline, flight_num, departure_location, arrival_destination, departure_time, arrival_time, seat_layout):
    
    flight_dict = {'Flight Number' : flight_num, 'Airline' : airline, 'Departure Location' : departure_location, 'Arrival Destination' : arrival_destination, 'Departure Time' : departure_time, 'Arrival Time' : arrival_time, 'Seat Layout' : seat_layout}
        
    with open(ALL_FLIGHTS, 'a') as i:

        i.write(str(flight_dict) + '\n')

    print(f"\n\nThe flight has been added successfully!")


## Modify a Flight Function in Admin Menu

def modify_flight(modify_num):

    found = False

    modified_flights = []

    lines = file_reading(ALL_FLIGHTS)

    for flight_dict_str in lines:
        
        flight_dict = eval(flight_dict_str)  

        if flight_dict["Flight Number"] == modify_num:

            found = True

            while True:

                print("""\n\nWhich detail would you like to modify?
                    
1. Flight Number
2. Departure Location
3. Arrival Destination
4. Departure Time
5. Arrival Time""")
                
                modifying_details = input("\nOption: ")

                if modifying_details == "1":

                    new_num = input("\nWrite the updated Flight Number: ")

                    flight_dict['Flight Number'] = new_num

                    break
                

                elif modifying_details == "2":

                    new_location = input("\nWrite the updated Departure Location: ")

                    flight_dict['Departure Location'] = new_location

                    break

                elif modifying_details == "3":

                    new_destination = input("\nWrite the updated Arrival Destination: ")

                    flight_dict['Arrival Destination'] = new_destination

                    break

                elif modifying_details == "4":

                    new_dep_time = input("\nWrite the updated Departure Time: ")

                    flight_dict['Departure Time'] = new_dep_time

                    break

                elif modifying_details == "5":

                    new_arr_time = input("\nWrite the updated Arrival Time: ")

                    flight_dict['Arrival Time'] = new_arr_time

                    break

                else:
                    print("\nPlease enter a valid input.")

            modified_flights.append(flight_dict)                    
            
            
    if not found:
        print("\nThe flight you're looking for does not exist.")

    else:

        with open(ALL_FLIGHTS, "w") as f:
                    
            for line in lines:
                    
                    if line.find(modify_num) != -1:
                        pass
                    else:
                        f.write(line)
                
            for modified_flight in modified_flights:
                f.write(str(modified_flight) + '\n')

            print("\n\nThe flight has been modified successfully!")
          

## Remove a Flight Function

def remove_flight(remove_num):

    removed = False
    
    lines = file_reading(ALL_FLIGHTS)

    for line in lines:
        
        if remove_num in line:

            removed = True

            with open(ALL_FLIGHTS, "w") as f:
                
                for line in lines:
                    
                    if line.find(remove_num) != -1:
                        pass
                    
                    else:
                        f.write(line)

    if removed:
        print("\n\nThe flight has been removed successfully!")

    else:
        print("\n\nThis flight is not in our system.")


## User Interface

def user_interface(username):

    print(f"\nWelcome, {username}!") 

    while True:
    
        print("""\nWhat would you like to do today?\n
1. Book a Ticket
2. Cancel a Booking
3. Show Flights
4. Logout
""")
        
        option = input("Option: ")

        if option == "1":
            book_ticket()
            

        elif option == "2":
            name = input("\nPlease provide the name under which you did the booking: ")
            flight_no = input("\nPlease provide the flight number you booked: ")
            row_no = input("\nPlease provide the row number you booked: ")
            col_no = input("\nPlease provide the column number you booked: ")
            cancel_booking(name, row_no, col_no, flight_no)

        elif option == "3":
            show_all_flights()

        elif option == "4":
            print("\nLogging out...\n") 
            break

        else:
            print("\nPlease enter a valid option.\n")

    
## Admin Interface

def admin_interface(username):

    print(f"\nWelcome, {username}!") 

    while True:
    
        print("""\n\nWhat would you like to do today?\n
1. Add a Flight
2. Modify a Flight
3. Remove a Flight
4. Logout
""")
        
        option = input("Option: ")

        if option == "1":

            airline = input("\nAirline: ")
            flight_num = input("\nFlight Number: ")
            departure_location = input("\nDeparture Location: ")
            arrival_destination = input("\nArrival Destination: ")
            departure_time = input("\nDeparture Time: ")
            arrival_time = input("\nArrival Time: ")
            seat_layout =  [["       ","A","B","C","D","E","F"],
                    ["Row 1: ","*","*","*","*","*","*"],
                    ["Row 2: ","*","*","*","*","*","*"],
                    ["Row 3: ","*","*","*","*","*","*"],
                    ["Row 4: ","*","*","*","*","*","*"],
                    ["Row 5: ","*","*","*","*","*","*"],
                    ["Row 6: ","*","*","*","*","*","*"],
                    ["Row 7: ","*","*","*","*","*","*"],
                    ["Row 8: ","*","*","*","*","*","*"],
                    ["Row 9: ","*","*","*","*","*","*"],
                    ["Row 10:","*","*","*","*","*","*"],
                    ["Row 11:","*","*","*","*","*","*"],
                    ["Row 12:","*","*","*","*","*","*"],
                    ["Row 13:","*","*","*","*","*","*"]]            

            add_flight(airline, flight_num, departure_location, arrival_destination, departure_time, arrival_time, seat_layout)


        
        elif option == "2":
            modify_num = input("\nEnter the flight number of the flight you wish to modify: ")
            modify_flight(modify_num)


        elif option == "3":
            remove_num = input("\nEnter the flight number of the flight you wish to remove: ")
            remove_flight(remove_num)


        elif option == "4":
            print("\nLogging out...\n") 
            break

        else:
            print("\nPlease enter a valid option.\n")


## Login Screen

while True:

    print("\nWelcome to the Airplane Management System! Please enter your login details below to proceed.\n")

    user_username = "user"
    user_password = "user123"
    admin_username = "admin"
    admin_password = "admin123"

    username = input("Username: ")
    password = input("Password: ")

    if username == user_username and password == user_password:
        user_interface(user_username)

    elif username == admin_username and password == admin_password:
        admin_interface(admin_username)

    else:
        print("\nError! Wrong username or password. Please try again!\n")

