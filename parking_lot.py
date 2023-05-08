class Car:
    def __init__(self, lincence, model, color):
        self.lincence = lincence
        self.model = model
        self.color = color
    def __repr__(self):
        return f"{self.lincence}, {self.model}, {self.color}"

class Garage:
    def __init__(self):
        self.car_added = []
        self.spots = 10
        self.car_infos = {}
        self.bill = 0
        self.ticket = []

    def spots_available(self):
        return self.spots
    
    def add_car_to_garage(self, car):
        
        self.spot_name = ['A1', 'B1', 'C1', 'D1','E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        if self.spots_available() > 0:
            user_data = str(car).split(', ')
            # print(user_data)
            #print(user_data)
            self.spots -= 1
            self.car_added.append(user_data)
            self.car_infos = {'Tickets' : [], 'Licences' : [], 'Model' : [], 'Color' : []}
            ticket = ""
        
            for i, val in enumerate(self.car_added):
                ticket = self.spot_name[i] + val[0]
                # print(user_data[0])
                # print(val[0])
                self.car_infos['Tickets'].append(ticket)
                self.car_infos['Licences'].append(val[0])
                self.car_infos['Model'].append(val[1])
                self.car_infos['Color'].append(val[2])
            print(f'Successfully Parked your Car!! You ticket is {ticket}')
        else:
            print("Sorry!! There are no space in our park.")
    def unpark(self, ticket, hours):
        past_spot_len = len(self.car_infos['Tickets'])
        if(ticket not in self.car_infos['Tickets']):
            print("Sorry your ticket number is wrong!!")
        else:
            for i, val in enumerate(self.car_infos['Tickets']):
                if val == ticket:
                    print(f"Your licence number is: {self.car_infos['Licences'][i]}")
                    print(f"Your model number is: {self.car_infos['Model'][i]}")
                    print(f"Your color is: {self.car_infos['Color'][i]}")

                    self.car_infos['Licences'].pop(i)
                    self.car_infos['Model'].pop(i)
                    self.car_infos['Color'].pop(i)
                    self.car_infos['Tickets'].pop(i)
                    self.spots += 1
        
        if hours > 10:
            print(f"Total bill = {hours * 5 + 100}")
        else:
            print(f"Total bill = {hours * 5}")
    def total_cars_in_garage(self):
        for i in self.car_infos.items():
            number += 1
        print(f'Total car number is: {number}')







my_garage = Garage()

print("**************Welcome our parking system*******************")
while(True):
    print("Our all services:")
    print("1. Park Your Car.")
    print("2. Parking Space Check.")
    print("3. Unpark Your Car")

    user_choice = int(input("Enter your choice: "))
    if(user_choice == 1):
        car_license = input("Enter your license number: ")
        car_model = input("Enter your model number: ")
        car_color = input("Enter your color: ")
        user_car = Car(car_license, car_model, car_color)
        my_garage.add_car_to_garage(user_car)
    elif(user_choice==2):
        result = my_garage.spots_available()
        print(f'Total space available is: {result}')
    
    elif(user_choice==3):
        ticket = input("Enter your tickt number: ")
        hours = int(input("Enter your total parking time(Hour): "))
        my_garage.unpark(ticket, hours)



# user_car1 = Car('A0123899', 'Tes45LA', 'Black')
# user_car2 = Car('B0484784', 'FerariK45', 'Red')
# user_car3 = Car('L0484754', 'Lemborginni', 'Yellow')
# my_garage.add_car_to_garage(user_car1)
# my_garage.add_car_to_garage(user_car2)
# my_garage.add_car_to_garage(user_car3)
# my_garage.unpark('A1A0123899', 10)
# my_garage.unpark('B1B0484784', 11)
# my_garage.total_cars_in_garage()





        