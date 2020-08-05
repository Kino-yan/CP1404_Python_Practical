
class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return self.name, ":", self.student_id

if __name__=='__main__':  # unit test
     student = Student("Jordan", 23)
     print(student)