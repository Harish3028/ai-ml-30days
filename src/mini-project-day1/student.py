class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def letter_grade(self):
        avg = self.average_score()
        if avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'F'

    def __str__(self):
        return f"Student Name: {self.name}, Average Score: {self.average_score():.2f}, Letter Grade: {self.letter_grade()}"

if __name__ == "__main__":
    s = Student("Aisha", [85, 92, 78])
    print(s)
    print(Student("Bob", [70, 65, 80]))
    print(Student("Eli", [55, 62, 48]))