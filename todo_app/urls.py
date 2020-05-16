# tempat manage semua url aplikasi, yg selanjutnya terhubung dengan url project
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'), #list_id = id database
    path('cross_off/<list_id>', views.cross_off, name='cross_off'), #list_id = id database
    path('uncross/<list_id>', views.uncross, name='uncross'), #list_id = id database
    path('edit/<list_id>', views.edit, name='edit'), #list_id = id database
]
