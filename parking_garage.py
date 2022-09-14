class ParkingGarage():
    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
    def take_ticket(self):
        print("You have been given a ticket")
        self.tickets -= 1
        self.parking_spaces -= 1
    def pay_for_parking(self):
        payment = int(input("Please enter the amount paid for your parking ticket: $"))
        self.current_ticket["amt_paid"] = payment
        if payment > 0:
            print("Your ticket has been paid. You have 15 minutes to leave. Have a nice day!")
            self.current_ticket["paid"] = "True"
            self.tickets += 1
            self.parking_spaces += 1


my_garage = ParkingGarage(5, 5,{"paid": "", "amt_paid": ""})
my_garage.take_ticket()
my_garage.pay_for_parking()
