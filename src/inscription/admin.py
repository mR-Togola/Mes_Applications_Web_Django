from django.contrib import admin



# Register your models here.
from inscription.models import ParticipantForm



#admin.site.register(BlogPost)

@admin.register(ParticipantForm)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'prenom',
        'telephone',
        'email',
    )

    


