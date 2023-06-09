from django.db import models

# Create your models here.
YEARLEVEL = [
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
]

PAYMENT_MODES = [
    ('Cash', 'Cash'),
    ('Credit_card', 'Credit Card'),
    ('Debit_card', 'Debit Card'),
    ('G-cash', 'Gcash'),
    ('Paymaya', 'PayMaya'),
]

TRANSACTION_STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('PAID', 'Paid'),
    ('UNPAID', 'Unpaid'),
]


SEMESTER_TERM = [
    ('1st Semester', '1st Semester'),
    ('2nd Semester', '2nd Semester'),
]

CLEARANCE_STATUS = [
    ('PENDING', 'Pending'),
    ('CLEARED', 'Cleared'),
]

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=50)
    course_name = models.CharField(max_length=100, null=True)
    link = models.URLField(max_length=150, null=True)
    link2 = models.URLField(max_length=150, null=True)

    def __str__(self):
        return f'{self.course_id}'

class SchoolYear(models.Model):
    sy_id = models.CharField(max_length=100, null=True)
    semester = models.CharField(max_length=30, choices=SEMESTER_TERM, null=True)
    schoolyear = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.semester} - {self.schoolyear}'


class Student(models.Model):
    student_id = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=15, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_constraint=False)
    year_level = models.CharField(max_length=10, choices=YEARLEVEL)

    def __str__(self):
        return f'{self.student_id} - {self.last_name}, {self.first_name}'


class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=TRANSACTION_STATUS_CHOICES, default='PENDING')
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES, null=True)
    description = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.student.student_id} - {self.student.last_name}, {self.student.first_name} - {self.status}'


class Event(models.Model):
    event_id = models.CharField(max_length=50, null=True)
    event_name = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    description = models.CharField(max_length=100, null=True)
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.event_id} - {self.event_name} - {self.date}'


class Sanction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    merit = models.IntegerField(null=True)
    demerit = models.IntegerField(null=True)
    sanction = models.IntegerField(null=True)
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.student.student_id} - {self.student.last_name}, {self.student.first_name} - {self.sanction} - {self.schoolyear}'


class StudentClearance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, choices=CLEARANCE_STATUS, default='PENDING')
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return f'{self.student.student_id} - {self.student.last_name}, {self.student.first_name} - {self.status} - {self.schoolyear.semester} {self.schoolyear.schoolyear}'