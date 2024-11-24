from django.contrib import admin
from viewer.models import Genre, Movie, Actor

# Register your models here.
admin.site.register(Genre)
# admin.site.register(Movie)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name','birth_date', 'eye_color')
    search_fields = ('name', 'eye_color')
    list_filter = ('name',)

admin.site.register(Actor, ActorAdmin)
