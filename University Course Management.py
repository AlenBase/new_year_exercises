from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name, instructor, content):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.students = []

    @abstractmethod
    def display_course_details(self):
        pass

class UndergraduateCourse(Course):
    def display_course_details(self):
        print(f"Undergraduate Course: {self.name}, Instructor: {self.instructor}, Content: {self.content}")

class GraduateCourse(Course):
    def display_course_details(self):
        print(f"Graduate Course: {self.name}, Instructor: {self.instructor}, Content: {self.content}")

class Assignment(ABC):
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    @abstractmethod
    def display_assignment_details(self):
        pass

class BasicAssignment(Assignment):
    def display_assignment_details(self):
        print(f"Basic Assignment: {self.title}, Max Score: {self.max_score}")

class Student:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

    def complete_assignment(self, assignment, score):
        print(f"{self.name} completed the assignment - {assignment.title}, Score: {score}/{assignment.max_score}")

    def view_progress(self):
        print(f"{self.name}'s Enrolled Courses:")
        for course in self.enrolled_courses:
            print(f"- {course.name}")

class Professor:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def create_course(self, course):
        print(f"{self.name} created the course - {course.name}")

    def manage_course(self, course):
        print(f"{self.name} is managing the course - {course.name}")

# Example Usage
if __name__ == "__main__":
    undergrad_course = UndergraduateCourse("Introduction to Python", "Dr. Smith", "Basic Python concepts")
    grad_course = GraduateCourse("Advanced Machine Learning", "Prof. Johnson", "Deep learning and advanced ML techniques")

    basic_assignment = BasicAssignment("Python Basics Assignment", 100)

    student1 = Student("Vazgen", "vazgen@example.com")
    student2 = Student("Gor", "Gor@example.com")

    professor = Professor("Dr. Brown", "brown@example.com")

    professor.create_course(undergrad_course)
    professor.create_course(grad_course)

    student1.enroll_course(undergrad_course)
    student2.enroll_course(grad_course)

    professor.manage_course(undergrad_course)
    professor.manage_course(grad_course)

    student1.complete_assignment(basic_assignment, 90)
    student2.complete_assignment(basic_assignment, 85)

    student1.view_progress()
    student2.view_progress()
