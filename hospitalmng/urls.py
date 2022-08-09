from django.urls import path
from .views import about, home, contact, login, logout_admin, index

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin_login/', login, name='admin_login'),
    path('admin_logout/', logout_admin, name='logout_admin'),
    path('index/', index, name='dashboard'),

]
