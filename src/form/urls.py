from django.contrib import admin
from django.urls import path, include
from form import settings
from django.conf.urls.static import static



urlpatterns = [
    #path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('', include("inscription.urls")),
    path('blog/', include('blog.urls')),
    #path('portfolio/', include('portfolio.urls')),
    path('password_generator/', include('password_generator.urls')),
    path('find_birth_day/', include('jour_de_naissance.urls')),
    path('taches-a-faire/', include('todo.urls')),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
