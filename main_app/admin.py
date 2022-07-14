from django.contrib import admin
from .models import Card, Format, Set
# Register your models here.
admin.site.register(Card)
admin.site.register(Set)
admin.site.register(Format)