from . import settings
from .apps import APP_NAME
from .enums import IconsEnum, ParametersEnum
from .forms import *
from .constants import CURRENCY
from .repo import DocumentRepo, ParameterRepo, ProfileTransactionRepo, LinkRepo, ProfileTransactionRepo, ProfileRepo, MetaDataRepo, OurTeamRepo, RegionRepo, NotificationRepo
from .serializers import NotificationSerializer
from django.shortcuts import render,redirect,reverse
from django.views import View
from django.http import Http404
from .settings import PUSHER_IS_ENABLE
import json

if PUSHER_IS_ENABLE:
    from leopusher.repo import PusherChannelEventRepo
    from leopusher.serializers import PusherChannelEventSerializer
    PusherChannelEventRepo



TEMPLATE_ROOT='dashboard/'
def getContext(request):
    user=request.user
    context={}
    context['TEMPLATE_ROOT']=TEMPLATE_ROOT
    context['CURRENCY']=CURRENCY 
    if user.is_authenticated:
        profile=ProfileRepo(user=user).me    
        context['profile']=profile 
        context['notifications_s']=json.dumps(NotificationSerializer(NotificationRepo(user=request.user).list_unseen(),many=True).data)
        context['notifications_count']=NotificationRepo(user=user).count
        profiles=ProfileRepo(user=user).list_by_user(user=user)
        context['profiles']=profiles.exclude(pk=profile.pk)
        if PUSHER_IS_ENABLE:            
            my_channel_events=PusherChannelEventRepo(user=user).my_channel_events()
            my_channel_events_s=PusherChannelEventSerializer(my_channel_events,many=True).data
            context['my_channel_events_s']=json.dumps(my_channel_events_s)
    else:
        context['profile']=None                
        context['profiles']=None            
        context['my_channel_events_s']='[]'
        context['notifications_s']='[]'

    parameter_repo=ParameterRepo(user=user)
    context['PUSHER_IS_ENABLE']=PUSHER_IS_ENABLE
    context['dashboard']={
        'title':parameter_repo.get(ParametersEnum.TITLE),
        'subtitle':parameter_repo.get(ParametersEnum.SUBTITLE),
        'address':parameter_repo.get(ParametersEnum.ADDRESS),
        'about_us':parameter_repo.get(ParametersEnum.ABOUT_US),
        'email':parameter_repo.get(ParametersEnum.EMAIL),
        'url':parameter_repo.get(ParametersEnum.URL),
        'meta_data_items':MetaDataRepo().list(),
        'our_team_title':OurTeamRepo(user=user).get_title(),
        'our_team_link':OurTeamRepo(user=user).get_link(),
    }
    context['SITE_URL']=settings.SITE_URL
    context['MEDIA_URL']=settings.MEDIA_URL
    context['ADMIN_URL']=settings.ADMIN_URL
    context['DEBUG']=settings.DEBUG
    
    # context['current_profile']=ProfileRepo.get_by_user()

    #leoData
    context['search_form']=SearchForm()
    return context

def csrf_failure(request, reason=""):
        context=getContext(request=request)
        context['message']=ParameterRepo(user=request.user).get(ParametersEnum.CSRF_FAILURE_MESSAGE).value        
        context['login_form']=LoginForm()
        context['register_form']=RegisterForm()
        return render(request,TEMPLATE_ROOT+'login.html',context)

class BasicView(View):
    def download(self,request,document_id):
        download=DocumentRepo(user=request.user).get(document_id=document_id).download()
        return download
    def notifications(self,request,notification_id=None):
        user=request.user
        context=getContext(request=request)
        if notification_id is None:
            
            notifications_seen=NotificationRepo(user=user).list_seen()
            notifications_unseen=NotificationRepo(user=user).list_unseen()
            # for notification in notifications_seen:
            #     if notification.seen:
            #         notification.color='scecondary'
            context['notifications_seen']=notifications_seen
            context['notifications_unseen']=notifications_unseen
        else:
            context['notification']=NotificationRepo(user=user).get(notification_id=notification_id)
        context['notifications_s']=json.dumps(NotificationSerializer(NotificationRepo(user=request.user).list_unseen(),many=True).data)
        return render(request,TEMPLATE_ROOT+'notifications.html',context)
    def about(self,request):        
        context=getContext(request=request)
        context['about_us']=ParameterRepo(user=request.user).get(ParametersEnum.ABOUT_US)
        return render(request,TEMPLATE_ROOT+'about.html',context)
    def terms(self,request):        
        context=getContext(request=request)
        context['terms']=ParameterRepo(user=request.user).get(ParametersEnum.TERMS)
        return render(request,TEMPLATE_ROOT+'terms.html',context)
    def search(self,request):
        if request.method=='POST':
            search_form=SearchForm(request.POST)
            if search_form.is_valid():
                search_for=search_form.cleaned_data['search_for']                     
                return redirect('/')

    def home(self,request):
        user=request.user
        context=getContext(request=request)
        context['links']=LinkRepo(user=user).list()
        return render(request,TEMPLATE_ROOT+'index.html',context)

class AuthView(View):
    def reset_password(self,request):
        user=request.user
        if request.method=='POST':
            reset_password_form=ResetPasswordForm(request.POST)
            if reset_password_form.is_valid():
                username=reset_password_form.cleaned_data['username']
                old_password=reset_password_form.cleaned_data['old_password']
                new_password=reset_password_form.cleaned_data['new_password']
                request1=ProfileRepo(user=request.user).reset_password(request=request,username=username,old_password=old_password,new_password=new_password)                
                if request1 is not None:
                    if request1.user.is_authenticated:                    
                        return redirect(reverse('dashboard:home'))
            
            context=getContext(request)
            context['message']='نام کاربری و کلمه عبور صحیح نمی باشد'            
            
            context['login_form']=LoginForm()
            context['register_form']=RegisterForm()
            context['reset_password_form']=ResetPasswordForm()
            context['regions']=RegionRepo(user=request.user).list()  
            
            return render(request,TEMPLATE_ROOT+'login.html',context=context)
        else:            
            return redirect(reverse('dashboard:login'))
    def logout(self,request):
        ProfileRepo().logout(request)
        return redirect(reverse('dashboard:login'))
    def auth(self,request,back_url=None):
        if back_url is None:
            back_url=reverse('dashboard:home')
        
        if request.method=='POST':
            login_form=LoginForm(request.POST)
            if login_form.is_valid():
                username=login_form.cleaned_data['username']
                password=login_form.cleaned_data['password']                
                request1=ProfileRepo().login(request=request,username=username,password=password)
                if request1 is not None and request1.user is not None and request1.user.is_authenticated:
                    return redirect(back_url)
                else:   
                    context=getContext(request=request)         
                    context['message']='نام کاربری و کلمه عبور صحیح نمی باشد'
                    context['login_form']=LoginForm()
                    context['register_form']=RegisterForm()
                    context['reset_password_form']=ResetPasswordForm()
                    return render(request,TEMPLATE_ROOT+'login.html',context)
        else:      
            return redirect(reverse('dashboard:login'))
                
    def login(self,request,back_url='/'):
            context={}
            context['back_url']=back_url
            context['login_form']=LoginForm()
            context['register_form']=RegisterForm()
            context['reset_password_form']=ResetPasswordForm()
            context['regions']=RegionRepo(user=request.user).list()               
            return render(request,TEMPLATE_ROOT+'login.html',context)
    def register(self,request):
        if request.method=='POST':
            register_form=RegisterForm(request.POST)
            if register_form.is_valid():
                region_id=register_form.cleaned_data['region_id']
                username=register_form.cleaned_data['username']
                password=register_form.cleaned_data['password']
                first_name=register_form.cleaned_data['first_name']
                last_name=register_form.cleaned_data['last_name']
                profile=ProfileRepo(user=request.user).register(username=username,password=password,first_name=first_name,last_name=last_name,region_id=region_id)                
                if profile is not None:
                    user=profile.user
                    if user is not None:
                        request1=ProfileRepo(user=request.user).login(request=request,username=user.username,password=password)
                        if request1 is not None and request1.user.is_authenticated:
                            return redirect(reverse('dashboard:home'))
            context=getContext(request)
            context['login_form']=LoginForm()
            context['register_form']=RegisterForm()
            context['reset_password_form']=ResetPasswordForm()
            context['regions']=RegionRepo(user=request.user).list()  
            return render(request,TEMPLATE_ROOT+'login.html',context=context)
        else:            
            return redirect(reverse('dashboard:login'))

class ProfileView(View):
    
    def change_profile_image(self,request):
        upload_profile_image_form=UploadProfileImageForm(request.POST,request.FILES)
        if upload_profile_image_form.is_valid():
            image=request.FILES['image']
            profile_id=upload_profile_image_form.cleaned_data['profile_id']
            ProfileRepo(user=request.user).change_profile_image(profile_id=profile_id,image=image)                    
            return redirect(reverse('dashboard:profile',kwargs={'profile_id':profile_id}))
    def edit_profile(self,request):
        if not request.method=='POST':
            return redirect('dashboard:home')
        edit_profile_form=EditProfileForm(request.POST)
        if edit_profile_form.is_valid():
            
            profile_id=edit_profile_form.cleaned_data['profile_id']
            first_name=edit_profile_form.cleaned_data['first_name']
            last_name=edit_profile_form.cleaned_data['last_name']
            region_id=edit_profile_form.cleaned_data['region_id']
            mobile=edit_profile_form.cleaned_data['mobile']
            address=edit_profile_form.cleaned_data['address']
            bio=edit_profile_form.cleaned_data['bio']
            # print(new_profile['bio'])
            profile=ProfileRepo(user=request.user).edit_profile(profile_id=profile_id,first_name=first_name,last_name=last_name,mobile=mobile,region_id=region_id,address=address,bio=bio) 
        return redirect(reverse('dashboard:profile',kwargs={'profile_id':profile.pk}))
    def change_profile(self,request):
        if not request.method=='POST':
            return redirect('dashboard:home')
        change_profile_form=ChangeProfileForm(request.POST)
        if change_profile_form.is_valid():
            actived=change_profile_form.cleaned_data['actived']
            profile=ProfileRepo(user=request.user).change_profile(user=request.user,actived=actived) 
        return redirect(reverse('dashboard:home'))
        

    def profile(self,request,profile_id=0):
        user=request.user
        context=getContext(request=request)
        if not user.is_authenticated:
            return AuthView().login(request=request,back_url=reverse('dashboard:profile',kwargs={'profile_id':profile_id}))
    
        active_profile=ProfileRepo(user=user).me
    
        selected_profile=ProfileRepo(user=user).get(profile_id=profile_id)
        if selected_profile is None:                
            raise Http404
        context['selected_profile']=selected_profile
        if (selected_profile is not None and selected_profile.user==request.user) or request.user.has_perm(f'{APP_NAME}.change_profile'):
            context['regions']=RegionRepo(user=user).list().exclude(pk=selected_profile.region_id)
            context['edit_profile_form']=EditProfileForm()
            context['upload_profile_image_form']=UploadProfileImageForm() 
            

        if selected_profile.user==request.user or request.user.has_perm(f'{APP_NAME}.view_profiletransaction'):
            transaction_repo=ProfileTransactionRepo(user=user)
            transactions=transaction_repo.list(profile_id=profile_id)[:20]                
            context['transactions']=transactions
            context['rest']=transaction_repo.rest(profile_id=profile_id)
        
        return render(request,TEMPLATE_ROOT+'profile.html',context)


class TransactionView(View):
    def transactions(self,request,profile_id,*args, **kwargs):
        user=request.user
        profile=ProfileRepo(user=user).get(profile_id=profile_id)
        context=getContext(request=request)
        transaction_repo=ProfileTransactionRepo(user=user)
        transactions=transaction_repo.list(profile_id=profile_id)
        context['transactions']=transactions
        context['transaction_title']=profile.name
        context['rest_all']=transaction_repo.rest(profile_id=profile_id)
        return render(request,TEMPLATE_ROOT+'transactions.html',context)


class ManagerView(View):
    
    def manager(self,request):
        user=request.user
        if user is not None and user.is_authenticated:
            return BasicView().home(request)
        context=getContext(request=request)
        priority_range=range(6)
        context['priority_range']=priority_range
        site_profiles=ProfileRepo(user=user).list_all()
        icons=list(IconsEnum)
        context['icons_s']=json.dumps(icons)
        context['site_profiles']=site_profiles
        if user.has_perm('leodashboard.add_notification'):
            add_notification_form=AddNotificationForm()
            context['add_notification_form']=add_notification_form
        return render(request,TEMPLATE_ROOT+'manager.html',context)
