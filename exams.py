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
    print("{:<6}    {:<10}    {:<5}    {:<8}    {:<5}".format(date, day, t, grade, ch))

print()
print_table("Date", "Day", "Class", "Subject", "Chapter")
print_table("----", "---", "-----", "-------", "-------")
for exam in exams:
    if datetime.now() < (exam.time + timedelta(hours=2)):
        time = exam.time.strftime
        print_table(time("%d/%m"), time("%A"), exam.grade, exam.subject, exam.lessons)
