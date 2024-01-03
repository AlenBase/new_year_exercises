from abc import ABC, abstractmethod

class SchoolMember(ABC):
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    @abstractmethod
    def display_info(self):
        pass

class Student(SchoolMember):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)

    def display_info(self):
        return f"Student: {self.name}, Contact: {self.contact_info}"

class Teacher(SchoolMember):
    def __init__(self, name, contact_info, subject_taught):
        super().__init__(name, contact_info)
        self.subject_taught = subject_taught

    def display_info(self):
        return f"Teacher: {self.name}, Contact: {self.contact_info}, Subject Taught: {self.subject_taught}"

class Course(ABC):
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.enrolled_students = []

    @abstractmethod
    def display_info(self):
        pass

    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"{student.name} enrolled in {self.course_name}.")

    def view_student_progress(self):
        print(f"\nStudent Progress for {self.course_name}:")
        for student in self.enrolled_students:
            print(f"{student.name}")

class MathCourse(Course):
    def display_info(self):
        return f"Math Course: {self.course_name}, Teacher: {self.teacher.name}"

class EnglishCourse(Course):
    def display_info(self):
        return f"English Course: {self.course_name}, Teacher: {self.teacher.name}"

if __name__ == "__main__":
    student1 = Student("Rocky Balboa", "rocky_balboa@yandex.com")
    student2 = Student("Dwayne Johnson", "dwayne_johnson@yandex.com")

    math_teacher = Teacher("Mr. Loris", "loris@gmail.com", "Math")
    english_teacher = Teacher("Ms. Scott", "scott@gmail.com", "English")

    math_course = MathCourse("Mathematics 101", math_teacher)
    english_course = EnglishCourse("English Literature", english_teacher)

    math_course.enroll_student(student1)
    math_course.enroll_student(student2)

    english_course.enroll_student(student1)

    math_course.view_student_progress()
    english_course.view_student_progress()
