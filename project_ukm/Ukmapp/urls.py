from django.urls import path, include
from . import views

urlpatterns =[
    #path('', views.home, name = 'home'),
    path('addUser', views.addUser, name = 'addUser'),
   # path('addItem', views.addItem, name = 'add'),
    path('Laporan', views.Laporan, name = 'laporan'),
    path('register/', views.register, name = 'add'),
    path('dashboard/', views.dashboard, name = 'as'),
    path('stokbarang/', views.StokBarang, name = 'stokbarang'),
    path('karyawan/', views.karyawan, name = 'karyawan'),
    path('Penentuan', views.Penentuan, name = 'penentuan'),
    path('outlet/', views.outlet, name = 'outlet'),

]