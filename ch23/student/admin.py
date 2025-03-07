from django.contrib import admin
from student.models import Profile, Result
# Register your models here.

# admin.site.register(Profile)
# admin.site.register(Result)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll','city','email')

admin.site.register(Profile,ProfileAdmin)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','stu_class')

# admin.site.register(Result,ResultAdmin)