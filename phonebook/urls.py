from django.urls import path
from . import views
app_name='phonebook'
urlpatterns = [
    path('',views.IndexView().home,name='home'),
    path('entry/<int:entry_id>/',views.IndexView().entry,name='entry'),
]
