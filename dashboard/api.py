from rest_framework.views import APIView
from .repo import ProfileRepo,NotificationRepo
from django.http import JsonResponse
from django.urls import path
from .constants import SUCCEED,FAILED
from .forms import *
class NotificationApi(APIView):
    def add_notification(self,request):
        if not request.method=='POST':
            return JsonResponse({'result':FAILED})
        add_notification_form = AddNotificationForm(request.POST)
        if add_notification_form.is_valid():
             
            title = add_notification_form.cleaned_data['title']
            body = add_notification_form.cleaned_data['body']
            icon = add_notification_form.cleaned_data['icon']
            color = add_notification_form.cleaned_data['color']
            link = add_notification_form.cleaned_data['link']
            profile_id = add_notification_form.cleaned_data['profile_id']
            priority = add_notification_form.cleaned_data['priority']
         
            # print(new_profile['bio'])
            NotificationRepo(user=request.user).add(priority=priority,profile_id=profile_id,title=title,body=body,color=color,icon=icon,link=link) 
            return JsonResponse({'result':SUCCEED})
class AuthApi(APIView):
    def check_available_username(self,request):
        username=request.POST['username']
        # csrfmiddlewaretoken=request.POST['csrfmiddlewaretoken']
        available=ProfileRepo(user=request.user).check_availabe_username(username=username)
        return JsonResponse({'available':available})

urlpatterns=[
    path('check_available_username/',AuthApi().check_available_username,name='check_available_username'),
    path('add_notification/',NotificationApi().add_notification,name='add_notification'),
]


