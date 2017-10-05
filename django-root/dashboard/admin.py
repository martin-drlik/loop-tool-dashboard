from django.contrib import admin

from dashboard.models import CourseOffering
from dashboard.models import CourseRepeatingEvent
from dashboard.models import CourseSingleEvent
from dashboard.models import CourseSubmissionEvent


@admin.register(CourseOffering)
class CourseOfferingAdmin(admin.ModelAdmin):
    readonly_fields = ('last_activity_at',)


admin.site.register(CourseSubmissionEvent)
admin.site.register(CourseSingleEvent)
admin.site.register(CourseRepeatingEvent)
