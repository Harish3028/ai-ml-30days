import numpy as np
from pathlib import Path

BASE = Path(__file__).parent

names = np.array(["Aisha", "Bob", "Cy", "Dana", "Eli", "Farah", "Gus", "Hana"])
exams = np.array(["Quiz", "Midterm", "Project", "Final"])

scores = np.array([
    [85, 92, 78, 88],
    [70, 65, 80, 72],
    [90, 55, 88, 91],
    [100, 95, 98, 97],
    [55, 62, 48, 60],
    [88, 91, 94, 85],
    [45, 70, 60, 52],
    [76, 80, 82, 79],
])

def exam_stats(scores):
    means = scores.mean(axis=0)
    maxes = scores.max(axis=0)
    mins = scores.min(axis=0)
    return means, maxes, mins

def student_averages(scores):
    return scores.mean(axis=1)

def best_student(scores, names):
     avg = student_averages(scores)
     i = avg.argmax()
     return names[i], avg[i]

def worst_student(scores, names):
    avg = student_averages(scores)
    i = avg.argmin()
    return names[i], avg[i]

def top_three(scores, names):
    avg = student_averages(scores)
    position = np.argsort(avg)[::-1][:3]
    return names[position]

def hardest_exam(scores, exams):
    avg = scores.mean(axis=0)
    hardest = avg.argmin()
    return exams[hardest], avg[hardest]

def easiest_exam(scores, exams):
    avg = scores.mean(axis=0)
    easy = avg.argmax()
    return exams[easy], avg[easy]

def pass_summary(scores):
    avg = student_averages(scores)
    passed_mask = avg >= 60
    passed_count = int(passed_mask.sum())
    pass_rate = passed_mask.mean() * 100
    return passed_mask, passed_count, pass_rate

def failed_any(scores, names):
    failed = scores < 60
    mask = failed.any(axis=1)
    return names[mask]

def failing_score_count(scores):
    failed = scores < 60
    return int(failed.sum())

def curve(scores, bonus=5):
    return np.minimum(scores + bonus, 100)

def letter_grades(avg):
    return np.where(avg >= 80, "A", np.where(avg >= 70, "B",
                          np.where(avg >= 60, "C", "F")))

def grade_counts(letters):
    counts = {}
    for g in "ABCF":
        counts[g] = int((letters == g).sum())
    return counts

def z_scores(scores):
    return ((scores - scores.mean(axis=0)) / scores.std(axis=0))

def most_improved(scores, names):
    final_score = (scores[:, 3] - scores[:, 0])
    i = final_score.argmax()
    return names[i], final_score[i]

def build_report(scores, names, exams):
    lines = []
    lines.append("=== EXAM ANALYSIS ===")
    lines.append(f"Students: {len(names)} | Exams: {len(exams)}")
    lines.append(f"Overall mean: {scores.mean():.2f} | Std: {scores.std():.2f}")
    lines.append("")
    lines.append("--- Per exam ---")
    means, maxes, mins = exam_stats(scores)
    for e, m, mx, mn in zip(exams, means, maxes, mins):
        lines.append(f"{e}: mean {m:.2f}, max {mx}, min {mn}")
    lines.append("")
    lines.append("--- Per student ---")
    avg = student_averages(scores)
    letters = letter_grades(avg)
    for n, a, l in zip(names, avg, letters):
        lines.append(f"{n}: {a:.2f}, ({l})")
    lines.append("")
    lines.append("--- Highlights ---")
    best_name, best_avg = best_student(scores, names)
    worst_name, worst_avg = worst_student(scores, names)
    lines.append(f"Best student: {best_name} ({best_avg:.2f})")
    lines.append(f"Worst student: {worst_name} ({worst_avg:.2f})")
    lines.append(f"Top 3: {', '.join(top_three(scores, names))}")
    hard_name, hard_mean = hardest_exam(scores, exams)
    easy_name, easy_mean = easiest_exam(scores, exams)
    lines.append(f"Hardest exam: {hard_name} (mean {hard_mean:.2f})")
    lines.append(f"Easiest exam: {easy_name} (mean {easy_mean:.2f})")
    mask, count, rate = pass_summary(scores)
    lines.append(f"Passed: {count} of {len(names)} ({rate:.1f} percent)")
    lines.append(f"Below 60 in any exam: {', '.join(failed_any(scores, names))}")
    lines.append(f"Grade counts: {grade_counts(letters)}")
    imp_name, imp_change = most_improved(scores, names)
    lines.append(f"Most improved: {imp_name} (+{imp_change})")
    return lines


def save_report(lines, filename):
    with open(filename, "w") as file:
        file.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    report = build_report(scores, names, exams)
    print("\n".join(report))
    save_report(report, BASE / "report.txt")
    print(f"\nReport saved to {BASE / 'report.txt'}")





