class Pupil:
    Rating = {1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6}

    def __init__(self, name = 'unknow' , surname = 'unknow' , marks = {} ):
        self.name = name
        self.surname = surname
        self.marks = marks

    def set_name(self):
        correct = True
        while correct == True:
            name = input("Name: ")
            if len(name) >= 3:
                self.name = name
                correct = False
            else:
                print ("The name should be longer than 3 letters")

    def set_surname(self):
        correct = True
        while correct == True:
            surname = input("Surname: ")
            if len(surname) >= 3:
                self.surname = surname
                correct = False
            else:
                print ("The surname should be longer than 3 letters")

    def complete_marks(self):
        mark = input("Mark: ")
        correct = True
        while correct == True:
            rating = input("Rating : ")
            if float(rating) in Pupil.Rating:
                self.marks.update({mark : float(rating)})
                correct = False
            else:
                print("Error: this rating isn't correct.")

    def print_marks(self):
        print("Mark\t|Rating")
        for mark in self.marks:
            print("{}: \t{}".format(mark, self.marks[mark]))

    def mean(self):
        if len(self.marks) > 0:
            suma = 0
            for mark in self.marks:
                suma += self.marks[mark]
            return suma/len(self.marks)

    def __str__(self):
        return "{} {}: {}".format(self.name, self.surname, self.mean())
        
class Student(Pupil):
    def __init__(self, name , surname , marks , weights):
        super().__init__( name, surname, marks)
        self.weights = weights

    def complete_weights(self):
        for mark in self.marks:
            correct = True
            while correct == True:
                weight = input("{} weight of this mark: ".format(mark))
                if float(weight) > 0 and float(weight) <=1:
                    self.weights.update({mark: float(weight)})
                    correct = False
                else:
                    print("wrong weight (0,1>")

    def mean(self):
        if len(self.weights) > 0:
            licznik = 0
            mianownik = 0
            for i in self.weights:
                licznik += self.weights[i] * self.marks[i]
                mianownik += self.weights[i]
            return licznik/mianownik

    def print_marks(self):
        print("Mark\t|Rating\t|Weight")
        for mark in self.marks:
            print("{}: \t{} \t {}".format(mark, self.marks[mark], self.weights[mark]))
        

    def __str__(self):
        ciag = super(Student, self).__str__()
        return ciag

def main():
    new = Pupil()
    new.set_name()
    new.set_surname()
    

    choice = True
    while choice == True:
        answer = input("1 -> Update marks\n2 -> Quit\nChoice: ")
        if answer == '1':
            new.complete_marks()
        elif answer == '2':
            choice = False
        else:
            print("Wrong command.")

    new_student = Student(new.name, new.surname, new.marks, {} ) 
    new_student.complete_weights()

    print("\n------------PUPIL--------------------------")            
    print(new)
    new.print_marks()
    print("-------------------------------------------")

    print("\n------------STUDENT-------------------------")
    print(new_student)
    new_student.print_marks()
    print("----------------------------------------------")
        
    #print("\n\nPupil {}\nStudent {}".format(nowy, nowy_student))
    input("\n\nTo finish, press enter.")
    

main()
