from abc import ABC, abstractmethod

class Exercise(ABC):
    def __init__(self, name, muscle_group):
        self.name = name
        self.muscle_group = muscle_group

    @abstractmethod
    def perform(self):
        pass

class CardioExercise(Exercise):
    def __init__(self, name, duration, intensity, muscle_group):
        super().__init__(name, muscle_group)
        self.duration = duration
        self.intensity = intensity

    def perform(self):
        print(f"Cardio Exercise: {self.name}, Duration: {self.duration}, Intensity: {self.intensity}")

class StrengthExercise(Exercise):
    def __init__(self, name, sets, repetitions, muscle_group):
        super().__init__(name, muscle_group)
        self.sets = sets
        self.repetitions = repetitions

    def perform(self):
        print(f"Strength Exercise: {self.name}, Sets: {self.sets}, Repetitions: {self.repetitions}")

class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.favorite_exercises = []

    def add_favorite_exercise(self, exercise):
        self.favorite_exercises.append(exercise)

class WorkoutPlan:
    def __init__(self, user, exercises, duration):
        self.user = user
        self.exercises = exercises
        self.duration = duration

    def display_plan(self):
        print(f"Workout Plan for {self.user.name}:")
        for exercise in self.exercises:
            exercise.perform()
        print(f"Plan Duration: {self.duration} minutes")

user1 = User("Irina", "irina@yandex.com")
cardio_exercise = CardioExercise("Running", 30, "High", "Legs")
strength_exercise = StrengthExercise("Bench Press", 3, 10, "Chest")

user1.add_favorite_exercise(cardio_exercise)
user1.add_favorite_exercise(strength_exercise)

favorite_exercises = user1.favorite_exercises

workout_plan = WorkoutPlan(user1, favorite_exercises, 60)
workout_plan.display_plan()
