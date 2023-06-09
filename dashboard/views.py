from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Course, Student, Transaction, Event, SchoolYear, Sanction, StudentClearance
from .forms import CourseForm, StudentForm, TransactionForm, EventForm, SchoolYearForm, SanctionForm, \
    StudentClearanceForm


# Create your views here.

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def about(request):
    return render(request, 'dashboard/about.html')

@login_required
def studentview(request):
    return render(request, 'dashboard/studentview.html')


# ----------COURSE MODULE----------
@login_required
def course(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-course')
    else:
        form = CourseForm()

    context = {
        'courses': courses,
        'form': form,
    }

    return render(request, 'dashboard/course.html', context)


@login_required
def course_delete(request, pk):
    courses = Course.objects.get(id=pk)
    if request.method == 'POST':
        courses.delete()
        return redirect('dashboard-course')
    return render(request, 'dashboard/course_delete.html')


@login_required
def course_update(request, pk):
    courses = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('dashboard-course')
    else:
        form = CourseForm(instance=courses)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/course_update.html', context)


# ----------END OF COURSE MODULE----------

# ----------STUDENT MODULE----------

@login_required
def student(request):
    student = Student.objects.all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-student')
    else:
        form = StudentForm()

    context = {
        'student': student,
        'form': form,
        'user': request.user
    }
    return render(request, 'dashboard/student.html', context)


@login_required
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('dashboard-student')
    return render(request, 'dashboard/student_delete.html')


@login_required
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard-student')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/student_update.html', context)


# ----------END OF STUDENT MODULE----------


# ----------TRANSACTION MODULE----------

@login_required
def transaction(request):
    if (request.user.is_superuser):
        transactions = Transaction.objects.all()
    else:
        transactions = Transaction.objects.all().filter(student__student_id=request.user.username)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-transaction')
    else:
        form = TransactionForm()

    context = {
        'transactions': transactions,
        'form': form,
        'user': request.user
    }

    return render(request, 'dashboard/transaction.html', context)


@login_required
def transaction_delete(request, pk):
    transactions = Transaction.objects.get(id=pk)
    if request.method == 'POST':
        transactions.delete()
        return redirect('dashboard-transaction')
    return render(request, 'dashboard/transaction_delete.html')


@login_required
def transaction_update(request, pk):
    transactions = Transaction.objects.get(id=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transactions)
        if form.is_valid():
            form.save()
            return redirect('dashboard-transaction')
    else:
        form = TransactionForm(instance=transactions)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/transaction_update.html', context)


# ----------END OF TRANSACTION MODULE----------


# ----------EVENT MODULE----------

def event(request):
    events = Event.objects.all()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-event')
    else:
        form = EventForm()

    context = {
        'events': events,
        'form': form,
        'user': request.user
    }

    return render(request, 'dashboard/event.html', context)


@login_required
def event_delete(request, pk):
    events = Event.objects.get(id=pk)
    if request.method == 'POST':
        events.delete()
        return redirect('dashboard-event')
    return render(request, 'dashboard/event_delete.html')


@login_required
def event_update(request, pk):
    events = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=events)
        if form.is_valid():
            form.save()
            return redirect('dashboard-event')
    else:
        form = EventForm(instance=events)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/event_update.html', context)


# ----------END OF EVENT MODULE----------


# ----------SANCTION POINTS MODULE----------

def sanction(request):
    if (request.user.is_superuser):
        sanctions = Sanction.objects.all()
    else:
        sanctions = Sanction.objects.all().filter(student__student_id=request.user.username)

    if request.method == 'POST':
        form = SanctionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-sanction')
    else:
        form = SanctionForm()

    context = {
        'sanctions': sanctions,
        'form': form,
        'user': request.user
    }

    return render(request, 'dashboard/sanction.html', context)


@login_required
def sanction_delete(request, pk):
    sanctions = Event.objects.get(id=pk)
    if request.method == 'POST':
        sanctions.delete()
        return redirect('dashboard-sanction')
    return render(request, 'dashboard/sanction_delete.html')


@login_required
def sanction_update(request, pk):
    sanctions = Sanction.objects.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=sanctions)
        if form.is_valid():
            form.save()
            return redirect('dashboard-sanction')
    else:
        form = SanctionForm(instance=sanctions)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/sanction_update.html', context)


# ----------END OF SANCTIONS MODULE----------


# ----------SCHOOL YEAR MODULE----------

@login_required
def schoolyear(request):
    schoolyears = SchoolYear.objects.all()

    if request.method == 'POST':
        form = SchoolYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-schoolyear')
    else:
        form = SchoolYearForm()

    context = {
        'schoolyears': schoolyears,
        'form': form,
        'user': request.user
    }

    return render(request, 'dashboard/schoolyear.html', context)


@login_required
def schoolyear_delete(request, pk):
    schoolyear = SchoolYear.objects.get(id=pk)
    if request.method == 'POST':
        schoolyear.delete()
        return redirect('dashboard-schoolyear')
    return render(request, 'dashboard/schoolyear_delete.html')


@login_required
def schoolyear_update(request, pk):
    schoolyear = SchoolYear.objects.get(id=pk)
    if request.method == 'POST':
        form = SchoolYearForm(request.POST, instance=schoolyear)
        if form.is_valid():
            form.save()
            return redirect('dashboard-schoolyear')
    else:
        form = SchoolYearForm(instance=schoolyear)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/schoolyear_update.html', context)


# ----------END OF SCHOOL YEAR MODULE----------


# ------------START OF CLEARANCE MODULE --------------

@login_required
def studentclearance(request):
    studentclearances = StudentClearance.objects.all()

    if request.method == 'POST':
        form = StudentClearanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-clearance')
    else:
        form = StudentClearanceForm()

    context = {
        'studentclearances': studentclearances,
        'form': form,
    }

    return render(request, 'dashboard/studentclearance.html', context)


@login_required
def studentclearance_delete(request, pk):
    studentclearances = StudentClearance.objects.get(id=pk)
    if request.method == 'POST':
        studentclearances.delete()
        return redirect('dashboard-clearance')
    return render(request, 'dashboard/studentclearance_delete.html')


@login_required
def studentclearance_update(request, pk):
    studentclearances = StudentClearance.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentClearanceForm(request.POST, instance=studentclearances)
        if form.is_valid():
            form.save()
            return redirect('dashboard-clearance')
    else:
        form = StudentClearanceForm(instance=studentclearances)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/studentclearance_update.html', context)

# ------------END OF CLEARANCE MODULE--------------
