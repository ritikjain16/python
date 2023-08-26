class Train():
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare
    
    def getStatus(self):
        print(f"The name of train is {self.name}")
        print(f"The no. of seats available in this train are {self.seats}")

    def getFare(self):
        print(f"The fare of this train ticket is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat no. is {self.seats}. Happy Journey.")
            self.seats = self.seats -1   # every time when we book the ticket seat changes.
            

        else:
            print("Sorry this train is Full! Kindly try in Tatkal.")


    def cancelTicket(self):
        if(self.seats>=0 and self.seats<10):
         print(f"Your ticket has been Cancelled.Total seats available in this train are {self.seats+1}")
         self.seats=self.seats+1
        else:
            print("No ticket can be cancelled.")
        


# if you change no. of seats then plz also change in cancel ticket method.
passenger1=Train("Dakshin Express",10,200)
passenger1.getStatus()
passenger1.getFare()
passenger1.bookTicket()
passenger1.cancelTicket()
passenger1.bookTicket()
passenger1.bookTicket()


passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()
passenger1.bookTicket()

passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
passenger1.cancelTicket()
