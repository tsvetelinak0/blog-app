from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include 
from blog.views import (
    blog_post_create_view,
)

from searches.views import search_view
from users import views as user_views
from . import views
# from .views import (
#     home_page,
#     about_page,
#     contact_page,
# )


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog-new/', blog_post_create_view),
    path('blog/', include('blog.urls')),
    path('search/', search_view, name= 'search'),
    path('about/', views.about, name='blog-about'),
    # path('pages/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)