from student import Student

def parse_line(line):
    parts = line.strip().split(",")
    name = parts[0].strip()

    if not name:
        raise ValueError("Name cannot be empty!")

    if len(parts) != 4: 
        raise ValueError("Line must contain 4 parts: name, score1, score2, score3")


    try:
        scores = [int(score) for score in parts[1:]]
    except ValueError:
        raise ValueError("Cannot parse scores!")

    for score in scores:
        if not (0 <= score <= 100):
            raise ValueError(f"Score {score} is out of range! Must be between 0 and 100.")

    return Student(name, scores)

def load_students(filename):
    students = []
    skipped = []
    with open(filename) as f:
        for line in f:
            clean = line.strip()

            if not clean:
                continue

            try:
                student_obj = parse_line(clean)
                students.append(student_obj)
            except ValueError as e:
                skipped.append((clean, str(e)))
    return students, skipped

def class_average(students):
    if not students:
        return 0.0

    total = [s.average_score() for s in students]
    return sum(total) / len(total)

def top_student(students):
    if not students:
        return None

    return max(students, key=lambda s: s.average_score())
    
def grade_counts(students):
    counts = {"A": 0, "B": 0, "C": 0, "F": 0}
    for s in students:
        g = s.letter_grade()
        counts[g] = counts.get(g, 0) + 1
    return counts

def build_report(students, skipped):
    lines = []
    lines.append("=== GRADE REPORT ===")
    lines.append(f"Valid students: {len(students)} | Skipped lines: {len(skipped)}")
    lines.append("")
    lines.append("--- Students ---")
    for s in students:
        lines.append(str(s))
    lines.append("")
    lines.append(f"Class average: {class_average(students):.2f}")
    lines.append(f"Top student: {top_student(students)}")
    lines.append(f"Grade counts: {grade_counts(students)}")
    lines.append("")
    lines.append("--- Skipped lines ---")
    
    for line, reason in skipped:
        lines.append(f"Skipped: {line}, Because: {reason}")
    return lines

def save_report(lines, filename):
    with open(filename, "w") as file:
        file.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    students, skipped = load_students("src/mini-projects/Day01/student-grade-tracker/students_raw.txt")
    report = build_report(students, skipped)
    print("\n".join(report))
    save_report(report, "src/mini-projects/Day01/student-grade-tracker/report.txt")
    print("\nReport saved to src/mini-projects/Day01/student-grade-tracker/report.txt")