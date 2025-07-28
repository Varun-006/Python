#clase is a blueprint for creating object
class student:
    def __init__(A,name,usn):#_init_() is constructor
        A.name=name
        A.usn=usn
    def d(A):
        print("name:",A.name)
        print("usn:",A.usn)
s1=student("varun",444)
s1.d()