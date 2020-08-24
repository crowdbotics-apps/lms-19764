from django.contrib import admin
from .models import (
    Recording,
    Event,
    Subscription,
    Course,
    Group,
    Module,
    SubscriptionType,
    Enrollment,
    Category,
)

admin.site.register(Recording)
admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Subscription)
admin.site.register(Category)
admin.site.register(SubscriptionType)
admin.site.register(Enrollment)
admin.site.register(Group)
admin.site.register(Module)

# Register your models here.
