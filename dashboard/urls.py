from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('about/', views.about, name='dashboard-about'),
    path('studentview/', views.studentview, name='dashboard-studentview'),
    path('student/', views.student, name='dashboard-student'),
    path('student/delete/<int:pk>/', views.student_delete, name='dashboard-student-delete'),
    path('student/update/<int:pk>/', views.student_update, name='dashboard-student-update'),
    path('course/', views.course, name='dashboard-course'),
    path('course/delete/<int:pk>/', views.student_delete, name='dashboard-course-delete'),
    path('course/update/<int:pk>/', views.student_update, name='dashboard-course-update'),
    path('transaction/', views.transaction, name='dashboard-transaction'),
    path('transaction/delete/<int:pk>/', views.transaction_delete, name='dashboard-transaction-delete'),
    path('transaction/update/<int:pk>/', views.transaction_update, name='dashboard-transaction-update'),
    path('event/', views.event, name='dashboard-event'),
    path('event/delete/<int:pk>/', views.event_delete, name='dashboard-event-delete'),
    path('event/update/<int:pk>/', views.event_update, name='dashboard-event-update'),
    path('sanction/', views.sanction, name='dashboard-sanction'),
    path('sanction/delete/<int:pk>/', views.sanction_delete, name='dashboard-sanction-delete'),
    path('sanction/update/<int:pk>/', views.sanction_update, name='dashboard-sanction-update'),
    path('schoolyear/', views.schoolyear, name='dashboard-schoolyear'),
    path('schoolyear/delete/<int:pk>/', views.schoolyear_delete, name='dashboard-schoolyear-delete'),
    path('schoolyear/update/<int:pk>/', views.schoolyear_update, name='dashboard-schoolyear-update'),
    path('clearance/', views.studentclearance, name='dashboard-clearance'),
    path('clearance/delete/<int:pk>/', views.studentclearance_delete, name='dashboard-clearance-delete'),
    path('clearance/update/<int:pk>/', views.studentclearance_update, name='dashboard-clearance-update'),
]