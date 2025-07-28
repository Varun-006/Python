#inheritence allowes class to accese properties of another class
class person:
    def detailes(self):
        print("hello")
class student(person):
    def clg(self):
        print("hii")
g=student()
g.detailes()
g.clg()