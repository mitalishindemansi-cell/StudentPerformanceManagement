from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(SubjectCombination)
admin.site.register(Student)
admin.site.register(Notices)
admin.site.register(Result)