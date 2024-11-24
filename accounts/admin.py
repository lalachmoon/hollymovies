from django.contrib import admin
from django.contrib.admin import ModelAdmin

from accounts.models import AdminRequestMessage
from viewer.models import Movie


# Register your models here.
#Acest cod îmbunătățește gestionarea modelului AdminRequestMessage în interfața de administrare:
#Când accesezi modelul AdminRequestMessage în admin:
#Vezi o listă de mesaje, fiecare afișând utilizatorul, mesajul și data creării (definite prin list_display).
#Poți căuta rapid utilizând numele utilizatorului sau textul mesajului (search_fields).
#Poți filtra mesajele după data creării folosind filtrele din partea laterală (list_filter).

# @admin.register: Înregistrează modelul și aplică personalizările.
@admin.register(AdminRequestMessage)
class AdminRequestMessageAdmin(admin.ModelAdmin):
    #list_display: Definește coloanele afișate în tabel.
    list_display = ('user', 'message', 'created_at')

    #search_fields: Permite căutarea în câmpuri specifice.
    search_fields = ('user__username', 'message')

    #list_filter: Adaugă filtre laterale pentru filtrarea ușoară a datelor.
    list_filter = ('created_at', 'approved')

    # Adăugăm acțiune personalizată pentru aprobare sau respingere
    actions = ['approve_messages', 'reject_messages']

    def approve_messages(self, request, queryset):
        """Aprobă toate mesajele selectate."""
        queryset.update(approved=True)
        self.message_user(request, "Mesajele selectate au fost aprobate.")  # Mesaj de succes

    approve_messages.short_description = "Aprobă mesajele selectate"  # Descrierea acțiunii

    def reject_messages(self, request, queryset):
        """Aprobă toate mesajele selectate."""
        queryset.update(approved=False)
        self.message_user(request, "Mesajele selectate au fost respinse.")  # Mesaj de insucces

    reject_messages.short_description = "Respinge mesajele selectate"  # Descrierea acțiunii


class MovieAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description='ceva descriere default')

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 10
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description']

    fieldsets = [
        ('MyMovie', {'fields': ['title', 'created']}),
        (
            'External Information',
            {
                'fields': ['genre', 'released', 'actors'],
                'description': 'Fielduri de editat custom'
            }
        ),
        (
            'Movie info',
            {
                'fields': ['rating', 'description'],
                'description': 'Pareri despre film'
            }
        )
    ]

    readonly_fields = ['created']


admin.site.register(Movie, MovieAdmin)