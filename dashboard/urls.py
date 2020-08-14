
from django.contrib import admin
from django.urls import path,include
from . import views
app_name="dashboard"
urlpatterns = [
    path('',views.BasicView().home,name='home'),
    path('api/',include('dashboard.api')),
    path('profile/<int:profile_id>/',views.ProfileView().profile,name='profile'),
    path('transactions/<int:profile_id>/',views.TransactionView().transactions,name='transactions'),    
    path('login/',views.AuthView().login,name='login'),
    path('reset_password/',views.AuthView().reset_password,name='reset_password'),
    path('auth/',views.AuthView().auth,name='auth'),
    path('register/',views.AuthView().register,name='register'),
    path('logout/',views.AuthView().logout,name='logout'),
    path('about/',views.BasicView().about,name='about'),
    path('terms/',views.BasicView().terms,name='terms'),
    path('change_profile_image/',views.ProfileView().change_profile_image,name='change_profile_image'),
    path('edit_profile/',views.ProfileView().edit_profile,name='edit_profile'),
    path('change_profile/',views.ProfileView().change_profile,name='change_profile'),
    path('search/',views.BasicView().search,name='search'),
    path('manager/',views.ManagerView().manager,name='manager'),
    path('notifications/',views.BasicView().notifications,name='notifications'),
    path('notification/<int:notification_id>/',views.BasicView().notifications,name='notification'),
    path('download/<int:document_id>/',views.BasicView().download,name='download'),
]
