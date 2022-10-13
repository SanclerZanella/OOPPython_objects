'''

    Basic inheritance

    Inheritance is extends a first class that already works, taking advantage
    of everything in the first class adding it to the new class with new
    attributes and methods in the new class.

    How does it happens when we call a method?
        a.b
        (1) does 'b' exist as an attribute on 'a'?
        (2) does 'b' exist as an attribute on 'a' class?
        (3) does 'b' exist as an attribute on 'a' parent class?
        repeat this until we get to a class whose parent is "object"
        (4) does 'b' exist as an attribute on object?

    The point with inheritance is don't repeat myself, don't repeat data.

    The key idea in inheritance is I want create a class that most of it
    of its functionality is already implemented and I wan to make use of
    this functionality

'''


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


p1 = Person('name1')
p2 = Person('name2')

p1.greet()
p2.greet()


# The Employee inherit from the class Person
class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)  # super() gives back on which I can run it
        self.id = id


e1 = Employee('employee1', 1)
e2 = Employee('employee2', 2)

e1.greet()
e2.greet()


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.meetings = list()
        self.students = list()

    def add_meetings(self, new_meeting):
        self.meetings.append(new_meeting)

    def add_students(self, new_student):
        self.students.append(new_student)

    def all_meetings(self):
        return 'Meeting at: ' + '\n'.join('\t' + one_meeting
                                          for one_meeting in self.meetings)


c1 = Course('Python', 'Reuven')
c1.add_meetings('2018-May-10 10:00')
c1.add_meetings('2018-May-12 10:00')

c1.add_students('Joe')
c1.add_students('Mary')

c1.all_meetings()


class OlineCourse(Course):
    def __init__(self, title, teacher, url):
        super().__init__(title, teacher)
        self.url = url

    def get_username(self, student):
        return student.lower()

    def all_usernames(self):
        return {one_student: self.get_username(one_student)
                for one_student in self.students}


c2 = OlineCourse('Online Python', 'Reuven', 'http://lerner.com.il/')
c2.add_meetings('2018-May-10 10:00')
c2.add_meetings('2018-May-12 10:00')

c2.add_students('Joe')
c2.add_students('Mary')

c2.all_usernames()

# OnlineCourse is-a Course : OnlineCourse inherits from Course

print(OlineCourse.__bases__)  # Keep track of inhetances
print(c2.all_meetings())
