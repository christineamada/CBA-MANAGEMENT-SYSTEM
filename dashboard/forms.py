from django import forms
from django.forms import DateInput
from .models import Student, Course, Transaction, Event, SchoolYear, Sanction, StudentClearance


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'last_name', 'first_name', 'middle_initial', 'course', 'year_level']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'link', 'link2']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['student', 'date', 'status', 'payment_mode', 'description', 'amount', 'schoolyear']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_id', 'event_name', 'date', 'description', 'schoolyear']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }


class SanctionForm(forms.ModelForm):
    class Meta:
        model = Sanction
        fields = ['student', 'event', 'merit', 'demerit', 'sanction', 'schoolyear']


class SchoolYearForm(forms.ModelForm):
    class Meta:
        model = SchoolYear
        fields = ['sy_id', 'semester', 'schoolyear']


class StudentClearanceForm(forms.ModelForm):
    class Meta:
        model = StudentClearance
        fields = ['student', 'status', 'schoolyear']
