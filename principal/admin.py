from django.contrib import admin
from .models import Annotation, Task, Liker


admin.site.register(Task)
admin.site.register(Liker)
admin.site.register(Annotation)
