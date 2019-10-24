class Fraction:

    def __init__(self, top, bottom): #First method is always a constructor

        #"self" is a special parameter that will always be used as a reference back to the object itself and
        #must always be the first formal parameter -> however, it will never be given a formal parameter value

        self.num = top #"self.num" in the constructor defines the Fraction object to have an internal data object called
        #"num" as part of its state
        self.den = bottom

    def show(self):

        print(self.num, "/", self.den)

    def __str__(self): #Override "__str__" method

        return (str(self.num) + " / " + str(self.den))

    def __add__(self, other_fraction): #Overload the addition operator

        new_num = self.num*other_fraction.den + self.den*other_fraction.num
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)

if __name__ == '__main__':

    my_fraction = Fraction(3,4)
    my_fraction.show()
    print(my_fraction)

    f1 = Fraction(1,4)
    f2 = Fraction(1,2)
    f3 = f1 + f2
    print(f3)
