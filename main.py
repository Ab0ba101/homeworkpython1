class Student:
    print("Hi")
    n = 0
    def __init__(self, height = 180):
        self.height = height
        self.weight = 70
        self.progress = 0
        self.gladness = 50
        #print(self)
        Student.n = Student.n+1

    def to_study(self):
        print("Time to study")
        self.progress += 10
        self.gladness -= 5

Nick = Student()
print(Nick.height)
print(Nick.n)
Nick.to_study()
print("Progress:" + str(Nick.progress))
print("Gladness:" + str(Nick.gladness))

Kate = Student(height = 160)
print(Kate.height)
print(Kate.n)

student_3 = Student()
student_4 = Student()
student_5 = Student()
student_6 = Student()
student_7 = Student()
student_8 = Student()
student_9 = Student()
student_10 = Student()