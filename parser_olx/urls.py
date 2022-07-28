from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.main, name = 'main'),
    path('login/', views.login, name = "login"),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),
    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

