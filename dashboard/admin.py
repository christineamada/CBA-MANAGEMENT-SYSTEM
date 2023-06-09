from django.contrib import admin
from .models import Course, Student, Transaction, Event, Sanction, SchoolYear, StudentClearance
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.models import User

admin.site.site_header = 'CBA Management System'


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name')


class StudentResource(resources.ModelResource):
    student_id = fields.Field(attribute='student_id', column_name='student_id')
    first_name = fields.Field(attribute='first_name', column_name='first_name')
    last_name = fields.Field(attribute='last_name', column_name='last_name')
    middle_initial = fields.Field(attribute='middle_initial', column_name='middle_initial')
    course = fields.Field(
        column_name='course',
        attribute='course',
        widget=widgets.ForeignKeyWidget(Course, 'course_id')
    )

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        if not dry_run:
            for row in dataset.dict:
                print(row)
                # Create a user account for each imported student
                username = row['student_id']
                password = 'cbastudent'
                first_name = row['first_name']
                last_name = row['last_name']

                # Check if a user with the same username already exists
                if not User.objects.filter(username=username).exists():
                    # Create a new user account
                    user = User.objects.create_user(username=username, password=password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()

    class Meta:
        model = Student
        fields = ('student_id', 'last_name', 'first_name', 'middle_initial', 'course', 'year_level')
        export_order = ('student_id', 'last_name', 'first_name', 'middle_initial', 'course', 'year_level')
        import_id_fields = ('student_id',)
        skip_unchanged = True
        report_skipped = False


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('student_id', 'last_name', 'first_name', 'middle_initial', 'course', 'year_level')
    list_filter = ('course', 'year_level')
    resource_class = StudentResource

    def export_data(self, request, queryset):
        data = serialize('json', queryset)

        data_list = []
        for entry in data:
            obj = entry['fields']
            obj['course'] = str(obj['course'])
            data_list.append(obj)

        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=data.json'
        return response

    actions = [export_data]


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('student', 'status', 'date', 'amount', 'status', 'payment_mode', 'description', 'schoolyear')


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'date')


class SanctionAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'sanction', 'schoolyear')
    list_filter = ('student', 'schoolyear')


class SchoolYearAdmin(admin.ModelAdmin):
    list_display = ('sy_id', 'semester', 'schoolyear')
    list_filter = ('sy_id', 'schoolyear')


class StudentClearanceAdmin(admin.ModelAdmin):
    lisit_display = ('student', 'status', 'schoolyear')


admin.site.register(Course, CourseAdmin)
admin.site.unregister(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sanction, SanctionAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(StudentClearance, StudentClearanceAdmin)
