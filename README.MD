# Movie Theater Reservation System

A console application seat assignment or reservation system for use of theater staff.

It includes the following functions:
- Reserves seats
- Checks reservations by seat number or name
- Deletes a reservation by seat number or name
- Resets the system/Deletes all reservations
- Saves the reservations at the end of the program

The project demonstrates the use of Python's built-in functions specifically: `print`, `input`, `open`, `zip`, `list`, `str`, `int`, `dict` and `len`.

## Installation

1. Install **python 3.6.3**.
2. Clone the github repository [reservation-system](https://github.com/czar3985/reservation-system).
	```
	$ git clone https://github.com/czar3985/reservation-system
	```
3. The necessary files needed to the run the program are:
	```
	reservation_system.py
	Seats.txt
	Names.txt
	```
4. Run the python script _reservation_system.py_. The following resource gives more information on how to run python scripts: [How to Run a Python Script via a File or the Shell](https://www.pythoncentral.io/execute-python-script-file-shell/).

## Usage

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