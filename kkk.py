import random


class Student:
    n = 0

    def __init__(self, height=180):
        self.height = height
        self.weight = 70
        self.progress = 0
        self.gladness = 50
        self.money = 100
        Student.n += 1

    def to_study(self):
        print("Time to study")
        self.progress += 10
        self.gladness -= 5

    def to_work(self):
        print("Time to work")
        self.money += 20
        self.gladness -= 10

    def to_rest(self):
        print("Time to rest")
        self.gladness += 15
        self.money -= 10

    def live_day(self, day):
        print(f"\nDay {day} of student life")
        if self.money <= 0:
            self.to_work()
        elif self.progress < 20:
            self.to_study()
        else:
            choice = random.choice([self.to_study, self.to_work, self.to_rest])
            choice()

        print(
            f"Progress: {self.progress}, Gladness: {self.gladness}, Money: {self.money}")

    def live_year(self):
        for day in range(1, 366):
            self.live_day(day)


Nick = Student()
Nick.live_year()
