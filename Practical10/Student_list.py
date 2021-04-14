class student():
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.programme = None

    def what_first_name(self, fn):
        self.first_name = fn

    def what_last_name(self, ln):
        self.last_name = ln

    def what_programme(self, pg):
        if pg in ["BMI", "BMS"]:
            self.programme = pg
        else:
            print('There is no such major in the institute')

    def output(self):
        print("Student's name is " + self.first_name + " " +
              self.last_name + ", and his/her undergraduate programme is " + self.programme)

# Examples
student1 = student()
student1.what_first_name("San")
student1.what_last_name("Zhang")
student1.what_programme("BMS")
student1.output()
