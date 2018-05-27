def get_available_seats():
    available_seats_list = []
    for key in seat_assignment_map:
        if (seat_assignment_map[key]=="None"):
            available_seats_list.append(key)

    return available_seats_list

def get_all_seats(seat_assignment_list):
    global all_seats_list
    
    all_seats_list = list(i[0] for i in seat_assignment_list)
    
def assign_name_to_seat(name_to_assign, seat_to_assign):
    global seat_assignment_map

    seat_assignment_map[seat_to_assign] = name_to_assign    
    print("Seat "+ seat_to_assign + " assigned to " + name_to_assign)

def reserve():
    global total_available_seats
    
    #get name of attendee
    name = input("Name: ")

    #get number of seats to reserve
    try:
        number_of_seats = int(input("No. of seats: "))
        if (number_of_seats == 0):
            print("Invalid input")
            return
        elif (number_of_seats > total_available_seats):
            print("Total available seats is " + str(total_available_seats))
            print("Not enough seats available")
            return
    except ValueError:
        print("Invalid input")
        return
            
    #get seats to reserve
    print("Reserving " + str(number_of_seats) + " ticket(s)")
    print("Seats available: ")
    #output seats that are still available
    available_seat_list = get_available_seats()
    available_seat_string = ", "
    print(available_seat_string.join(available_seat_list))
    #check input validity and make assignment
    for i in range(1, number_of_seats + 1):
        while(True):
            seat = input("Seat number " + str(i) + ": ")      
            if (seat == "cancel"):
                print("Cancelling the rest of the reservation process.")
                return
            elif (seat not in available_seat_list):
                print("Invalid input. Select from available seats or type \"cancel\".")
            else:
                assign_name_to_seat(name, seat)
                total_available_seats -= 1
                break

def check_reservation():
    menu_choice = input("Check reservation by seat (S) or by name (n)? S/N?").lower()

    #Check reservation by seat number
    if (menu_choice == 's'):
        seat = input("Check reservation for seat number: ")
        #if input is invalid, return
        if (seat not in all_seats_list):
            print("Invalid input")
            return
        #for valid input, get reservation info
        if (seat_assignment_map[seat] == "None"):
            print("There is no reservation for seat " + seat)
        else:
            print("Seat " + seat + " is reserved for: " + seat_assignment_map[seat])

    #Check reservation by name
    elif (menu_choice == 'n'):
        name_to_check = input("Check reservation(s) made by: ")
        seats_reserved = []
        for seat in seat_assignment_map:
            if (seat_assignment_map[seat] == name_to_check):
                seats_reserved.append(seat)
        if (len(seats_reserved)==0):
            print("No reservations made under the name " + name_to_check)
        else:
            print("These seats have been reserved for " + name_to_check + ": " + ', '.join(seats_reserved))
    else:
        print("Invalid input")

def delete_reservation():
    global total_available_seats
    
    menu_choice = input("Delete reservation by seat (S) or by name (n)? S/N?").lower()

    #Delete reservation by seat number
    if (menu_choice == 's'):
        seat = input("Delete reservation for seat number: ")
        #if input is invalid, return
        if (seat not in all_seats_list):
            print("Invalid input")
            return
        #for valid input, get reservation info
        if (seat_assignment_map[seat] == "None"):
            print("There is no reservation for seat " + seat)
        else:
            while(True):
                continue_deletion = input("Seat "
                      + seat
                      + " reserved for "
                      + seat_assignment_map[seat]
                      + " will be deleted. Continue? (Y/N)").lower()
                if (continue_deletion == 'y'):
                    assign_name_to_seat("None", seat)
                    total_available_seats += 1
                    return
                elif (continue_deletion == 'n'):
                    return
                else:
                    print("Invalid input")

    #Delete reservation by name
    elif (menu_choice == 'n'):
        name_to_delete = input("Delete reservation(s) made by: ")
        seats_reserved = []
        for seat in seat_assignment_map:
            if (seat_assignment_map[seat] == name_to_delete):
                seats_reserved.append(seat)
        if (len(seats_reserved)==0):
            print("No reservations made under the name " + name_to_delete)
        else:
            while(True):
                continue_deletion = input("These seats reserved for "
                                          + name_to_delete
                                          + ": "
                                          + ', '.join(seats_reserved)
                                          + " will be deleted. Continue? (Y/N)").lower()
                if (continue_deletion == 'y'):
                    for s in seats_reserved:
                        assign_name_to_seat("None", s)
                        total_available_seats += 1
                    return
                elif (continue_deletion == 'n'):
                    return
                else:
                    print("Invalid input")
    else:
        print("Invalid input")

def reset_all():
    global total_available_seats

    while(True):
        continue_deletion = input("All reservations will be deleted. Continue? (Y/N)").lower()
        if (continue_deletion == 'y'):
            for key in seat_assignment_map:
                if (seat_assignment_map[key]!="None"):
                    assign_name_to_seat("None", key)
                    total_available_seats += 1
            return
        elif (continue_deletion == 'n'):
            return
        else:
            print("Invalid input")

def save_and_exit():
    seat_assignment_list = seat_assignment_map.items()
    names_list = list(i[1] for i in seat_assignment_list)

    names_file = open(".\\Names.txt",'w')
    names_file.writelines("%s\n" % name for name in names_list)
    names_file.close()

def get_menu_choice():
    while (True):
        print("\nRESERVE (R)? CHECK RESERVATION (C)? DELETE RESERVATION (D)? RESET ALL (A)? EXIT (E)?")
        menu_choice = input("R, C, D, A or E? ").lower()

        if (menu_choice == 'r'):
            reserve()
        elif (menu_choice == 'c'):
            check_reservation()
        elif (menu_choice == 'd'):
            delete_reservation()
        elif (menu_choice == 'a'):
            reset_all()
        elif (menu_choice == 'e'):
            save_and_exit()
            return
        else:
            print("Invalid input")

seat_assignment_map = {}
all_seats_list = []
total_available_seats = 0

def main():
    print("\nHello from Monterey Cinemas Reservation System")
    print("Cinema: 1, Movie: Avengers: Infinity War")
    print("Date: April 25, 2018, Time: 9:40 AM")

    #initializations
    global seat_assignment_map
    global all_seats_list
    global total_available_seats
    seat_assignment_list = []
    
    #open and put seats in a list
    seats_file = open(".\\Seats.txt")
    seats = seats_file.read().splitlines()
    total_seats = len(seats)
    seats_file.close()

    #open and put names in a list
    names_file = open(".\\Names.txt")
    names = names_file.read().splitlines()
    for name in names:
        if (name == "None"):
            total_available_seats += 1
    names_file.close()

    #prepare data
    seat_assignment = zip(seats, names)
    seat_assignment_list = list(seat_assignment)
    seat_assignment_map = dict(seat_assignment_list)
    get_all_seats(seat_assignment_list)

    #reserve, check or save and exit
    get_menu_choice()
  
if __name__== "__main__":
    main()
