class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)
     
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

def input_students(tracker):
    while True:
        name = input("Enter student name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        try:
            scores = [int(input(f"Enter score for subject {i+1}: ")) for i in range(3)]
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")
            continue
        tracker.add_student(name, scores)

def main():
    tracker = PerformanceTracker()
    input_students(tracker)
    print("\nStudent Performance:")
    tracker.display_student_performance()
    print(f"\nClass Average: {tracker.calculate_class_average():.2f}")

if __name__ == "__main__":
    main()
