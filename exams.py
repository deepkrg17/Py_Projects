from datetime import datetime, timedelta


class Exam:
    def __init__(self, subject, lessons, grade, time):
        self.subject = subject
        self.lessons = lessons
        self.grade = grade
        self.time = time

exams = [
    Exam("Sub", "Ch", 5, datetime(2023, 7, 28, 16)),
]

def print_table(date, day, t, grade, ch):
    print(f"{date:<6}    {day:<10}    {t:<5}    {grade:<8}    {ch:<5}")

print()
print_table("Date", "Day", "Class", "Subject", "Chapter")
print_table("----", "---", "-----", "-------", "-------")
for exam in exams:
    if datetime.now() < (exam.time + timedelta(hours=2)):
        strftime = exam.time.strftime
        print_table(strftime("%d/%m"), strftime("%A"), exam.grade, exam.subject, exam.lessons)
