class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores.values()) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores.values())

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        student = Student(name, scores)
        self.students[name] = student

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"{student.name}: Average Score = {average:.2f}, Status = {status}")
            for subject, score in student.scores.items():
                print(f"   {subject}: {score}")

def input_students(tracker):
    while True:
        name = input("Enter student name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        scores = {}
        for subject in ["English", "Math", "Science"]:
            try:
                score = int(input(f"Enter score for {subject}: "))
                scores[subject] = score
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                break
        else:  # Only adds the student if all scores are valid
            tracker.add_student(name, scores)

def main():
    tracker = PerformanceTracker()
    input_students(tracker)
    print("\nStudent Performance:")
    tracker.display_student_performance()
    print(f"\nClass Average: {tracker.calculate_class_average():.2f}")

if __name__ == "__main__":
    main()
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores.values()) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores.values())

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        student = Student(name, scores)
        self.students[name] = student

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"{student.name}: Average Score = {average:.2f}, Status = {status}")
            for subject, score in student.scores.items():
                print(f"   {subject}: {score}")

def input_students(tracker):
    while True:
        name = input("Enter student name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        scores = {}
        for subject in ["English", "Math", "Science"]:
            try:
                score = int(input(f"Enter score for {subject}: "))
                scores[subject] = score
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                break
        else:  # Only adds the student if all scores are valid
            tracker.add_student(name, scores)

def main():
    tracker = PerformanceTracker()
    input_students(tracker)
    print("\nStudent Performance:")
    tracker.display_student_performance()
    print(f"\nClass Average: {tracker.calculate_class_average():.2f}")

if __name__ == "__main__":
    main()
