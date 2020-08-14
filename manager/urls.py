from django.urls import path,include
from . import views
app_name="manager"
urlpatterns = [
    path('',views.BasicView().home,name='home'),
    path('project/<int:project_id>/',views.BasicView().home,name='project'),
    path('contract/<int:contract_id>/',views.BasicView().home,name='contract'),
]