# # creating a class
# class Railway():
#     def book(self):
#         print("Booked")

# # creating an object of class Railway
# passenger1=Railway()
# passenger1.book()    # calls book method




class Wish():
    def wishme(self):
        print("Good Morning",self.name)


p1 = Wish()
name1 = input("Enter your Name: ")
p1.name = name1
p1.wishme()


