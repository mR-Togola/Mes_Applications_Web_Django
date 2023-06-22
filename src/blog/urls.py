from django.urls import path
from form import settings
from django.conf.urls.static import static
from blog.views import BlogHome, BlogPostCreate,BloPostUpdate, BlogPostDetail,BlosPostDelete


app_name = "posts"

urlpatterns = [

    path('', BlogHome.as_view(), name='home'),
     path('create_article/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='post'),
    path('editer_article/<str:slug>/', BloPostUpdate.as_view(), name='edit'),
    path('delete_article/<str:slug>/', BlosPostDelete.as_view(), name='delete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)