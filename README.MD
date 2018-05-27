PROJECT TITLE: Movie Theater Reservation System

A console application seat assignment or reservation system for use of theater staff.

It includes the following functions:
- Reserves seats
- Checks reservations by seat number or name
- Deletes a reservation by seat number or name
- Resets the system/Deletes all reservations
- Saves the reservations at the end of the program

The project demonstrates the use of Python's built-in functions specifically: print, input, open, zip, list, str, int, dict and len.

GETTING STARTED

Prerequisites: 
- Python 3.6.3 and python.exe should be added to the PATH environmental variable.
This guide in running Python scripts for different systems is particularly helpful:
https://www.pythoncentral.io/execute-python-script-file-shell/

- Project contents: reservation_system.py, Seats.txt and Names.txt

DEPLOYMENT

The processing always goes back to the main menu after every transaction.
The main menu options are:
- Reserve
- Check Reservation
- Delete Reservation
- Reset All
- Exit

To reserve, the program gets the person's name and number of seats to be reserved. 
The number of seats is checked against the remaining available seats.
It provides the list of available seats the user can choose from.

To check or delete a reservation, the user may do it by Name or by Seat Number.

Reset all will delete all current reservations.

Input error checking is performed in every transaction. The user is also asked
to confirm deletions when that option is selected.

To end the program, exit has to be selected in order to save all transactions.
Killing the program prematurely will not save reservation data entered in the session.