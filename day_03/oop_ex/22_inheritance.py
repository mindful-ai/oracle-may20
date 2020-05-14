class student(object):

    # Data/attributes
    def __init__(self, name, cls, rid):
        self.name = name
        self.cls = cls
        self.regid = rid
        self.physics = 0
        self.maths = 0
        self.chemistry = 0
        self.biology = 0
        self.average = 0


    # Functions

    def printinfo(self):
        print('NAME: ', self.name)
        print('CLASS: ', self.cls)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.maths)
        print('PHYSICS  : ', self.physics)
        print('CHEMISTRY: ', self.chemistry)
        print('BIOLOGY  : ', self.biology)
        print('-----------------------------------')
        print('AVERAGE  : ', self.average)

    def setMaths(self, marks):
        self.maths = marks

    def setPhysics(self, marks):
        self.physics = marks

    def setChemistry(self, marks):
        self.chemistry = marks

    def setBiology(self, marks):
        self.biology = marks


    def calcAverage(self):
        self.average = (self.physics + self.chemistry + self. biology + self.maths)/4


#######################################################################################


class ext_student(student):

    # Attributes
    def __init__(self, name, cls, rid, native, extra):
        super().__init__(name, cls, rid) # initializing the parent with appropriate data
        self.native = native # New attribute
        self.extra = extra   # New attribute

    def __str__(self):
        return 'This is the object for ' + str(self.name)

    def __len__(self):
        return 10

    # Functions
    def getGrade(self): # New function in the extended class
        if(self.average > 90):
            return 'A+'
        elif(70 < self.average < 90):
            return 'A'
        elif(50 < self.average < 70):
            return 'B'
        else:
            return 'C'


    def printinfo(self):  # Overriding the function
        super().printinfo()
        print('-----------------------------------')
        print('Native : %s' % self.native)
        print('Extras : ', self.extra)
        print('Grade  : %s' % self.getGrade())


#######################################################################################





s1 = ext_student('Rohit', 12, 'A001', 'Bellary', ['Music', 'Sports'])
s1.printinfo()
print('\n\n')

s1.setPhysics(100)
s1.setMaths(99)
s1.setChemistry(98)
s1.setBiology(97)
s1.printinfo()
print('\n\n')

s1.calcAverage()
s1.printinfo()


print('-------------------------------------')

print(s1)
print(len(s1))
