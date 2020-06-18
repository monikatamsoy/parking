from cmd import Cmd
import sys

sys.stdin=open(‘input.txt’,‘r’)
sys.stdout=open(‘output.txt’,‘w’)
# don't forget to add comments

class Parkinglot(Cmd): 
    def __init__(self):
        
        self.slots = {}
        Cmd.__init__(self)
    
    def do_create_parking(self,n):
        for i in range(0,int(n)):
            self.slots[i+1] = 0
        print("Created a parking lot with ", n, "slots")

    def do_park(self, car):
        # import pdb; pdb.set_trace()
        cardetails = car.split()
        vacancylist = list(self.slots.values())
        slotslist = list(self.slots.keys())
        try:
            vacantslot = slotslist[vacancylist.index(0)]
            self.slots[vacantslot] = cardetails
            print("Allocated slot number: ", vacantslot)
        except ValueError:
            print("Sorry parking lot is full")
        
    def do_leave(self,n):
        self.slots[int(n)] = 0
        print("Slot number ", n, "is free")

    def do_status(self,line):
        print("Slot no.", "Registration no.", "Color")
        for i in self.slots.keys():
            if self.slots[i] != 0 :
                print(i,"    ", self.slots[i][0],"    ", self.slots[i][1])

    def do_registration_numbers_for_cars_with_colour(self,color):
        result = []
        for i in self.slots.keys():
            if self.slots[i] !=0:
                if self.slots[i][1] == color:
                    result.append(self.slots[i][0])   
        print(*result, sep=',')

    def do_slot_numbers_for_cars_with_colour(self, color):
        result = []
        for i in self.slots.keys():
            if self.slots[i] !=0:
                if self.slots[i][1] == color:
                    result.append(i) 
        print(*result, sep=',')

    def do_slot_number_for_registration_number(self,number):
        result = "Not found"
        for i in self.slots.keys():
            if self.slots[i] != 0:
                if self.slots[i][0] == number:
                    result = i
        print(result)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':

    parking1 = Parkinglot() 
    parking1.cmdloop()



    
