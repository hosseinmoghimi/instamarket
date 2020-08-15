from django.contrib.auth import login, logout, authenticate
from .models import Document,Profile,ProfileTransaction,HomeSlider, Region, Link, MetaData, Notification, SocialLink, OurTeam, OurService, GalleryPhoto, Testimonial, Blog, Parameter, FAQ, MainPic
from .enums import ParametersEnum, PicEnum, ProfileStatusEnum
from django.contrib.auth.models import User
from .apps import APP_NAME
from .settings import SITE_URL
from django.db.models import Avg, Max, Min,F,Q,Sum
from .constants import NOTIFICATION_UNSEEN_COUNT,NOTIFICATION_SEEN_COUNT,NOTIFICATION_ALL_COUNT
 
class RegionRepo():
    def __init__(self,user=None):
        self.objects=Region.objects
        self.user=user
    def list(self):
        return self.objects.all()

class TestimonialRepo:
    def __init__( self, user=None):
        self.objects=Testimonial.objects
        self.user=user   
    def list(self):
        return self.objects.order_by('priority')
  
class MainPicRepo:
    mainPic=MainPic.objects  
    def faq(self):
        try:
            faq=self.mainPic.get(name=PicEnum.faq).image
        except:
            Parameter(name=PicEnum.faq).save()
            faq=self.mainPic.get(name=PicEnum.faq).image
        return faq
    
    def video(self):
        try:
            video=self.mainPic.get(name=PicEnum.video).image
        except:
            Parameter(name=PicEnum.video).save()
            video=self.mainPic.get(name=PicEnum.video).image
        return video
    
    def about(self):
        try:
            about=self.mainPic.get(name=PicEnum.about).image
        except:
            Parameter(name=PicEnum.about).save()
            about=self.mainPic.get(name=PicEnum.about).image
        return about
    def carousel(self):
        try:
            carousel=self.mainPic.get(name=PicEnum.carousel).image
        except:
            Parameter(name=PicEnum.carousel).save()
            carousel=self.mainPic.get(name=PicEnum.carousel).image
        return carousel
  
class MetaDataRepo:
    def __init__(self,user=None):
        self.objects=MetaData.objects
        self.user=user
    def list(self):
        return self.objects.all()

class FAQRepo:
    def __init__(self,user):
        self.user=user
        self.objects=FAQ.objects
        self.profile=ProfileRepo(user=user).me
      
    def list(self):
        return self.objects.order_by('number')
  
class ParameterRepo:
    
    def __init__(self,user=None):
        self.objects=Parameter.objects
    
    def set(self,name,value='--'):
        if value is None:
            value='--'
        self.objects.filter(name=name).delete()
        Parameter(name=name,value=value).save()
    
    def init(self,name,value=None):
        if value is None:
            value='...'
        try:
            param=self.objects.get(name=name)
        except :
            self.set(name=name,value=value)

    def get(self,name):
        try:
            parameter=self.objects.get(name=name)
        except:
            self.set(name=name)            
            parameter=self.objects.get(name=name)
        return parameter

class BlogRepo:
    def __init__(self,user=None):
        self.user=user
        self.objects=Blog.objects  
    def list(self):
        return Blog.objects.order_by('priority')
  
class NotificationRepo:

    def __init__(self,user):
        self.user=user
        self.objects=Notification.objects.order_by('-date_added')
        self.profile=ProfileRepo(user=user).me
        self.count=len(Notification.objects.filter(profile=self.profile).filter(seen=False))
    def add(self,profile_id,title,body,color,icon,link,priority=1,send_pusher=True):  
        if self.user.has_perm('leopusher.change_pusherchannelevent'):      
            notification=Notification(title=title,priority=priority,link=link,body=body,color=color,icon=icon,profile_id=profile_id)
            notification.save()
            if notification is not None:
                # PUSHER_IS_ENABLE=ParameterRepo(user=self.user).get(ParametersEnum.PUSHER_IS_ENABLE).value
                # if PUSHER_IS_ENABLE=='True':
                #     PUSHER_IS_ENABLE=True
                # else:
                #     PUSHER_IS_ENABLE=False
                # if send_pusher and PUSHER_IS_ENABLE:    
                #     channel_name=PusherChannelNameEnum.NOTIFICATION
                #     event_name=str(profile_id)
                #     if PUSHER_IS_ENABLE:
                #         notification.send(user=self.user,channel_name=channel_name,event_name=event_name)
                return notification
    def get(self,notification_id):
        profile=self.profile
        if profile is not None:
            notification=self.objects.get(pk=notification_id)
            if notification.profile==profile:
                notification.seen=True
                notification.save()
                if notification is not None:
                    return notification
    def list_seen(self):
        profile=self.profile
        if profile is not None:
            return self.objects.filter(profile=profile).filter(seen=True)[:NOTIFICATION_SEEN_COUNT]
    def list_all(self):
        profile=self.profile
        if profile is not None:
            return self.objects.filter(profile=profile)[:NOTIFICATION_ALL_COUNT]
    def list_unseen(self):
        profile=self.profile
        if profile is not None:
            return self.objects.filter(profile=profile).filter(seen=False)[:NOTIFICATION_UNSEEN_COUNT]

class SocialLinkRepo:
    def __init__(self,user):
        self.user=user
        self.objects=SocialLink.objects
        self.profile=ProfileRepo(user=user).me
    
    def list(self):
        return SocialLink.objects.order_by('priority')

class OurServiceRepo:
    def list(self):
        return OurService.objects.order_by('priority')

class HomeSliderRepo:
    def __init__(self,user=None):
        self.user=user
        self.objects=HomeSlider.objects
    def list(self):
        return self.objects.order_by('priority')

class GalleryPhotoRepo:    
    def __init__(self,user=None):
        self.user=user
        self.objects=GalleryPhoto.objects
    def list(self):
        return self.objects.order_by('priority')

class OurTeamRepo:
    def __init__(self,user=None):
        self.user=user
        self.objects=OurTeam.objects
    def get_link(self):
        return ParameterRepo(user=self.user).get(ParametersEnum.OUR_TEAM_LINK)  
    def get_title(self):
        if ParameterRepo(user=self.user).get(ParametersEnum.OUR_TEAM_TITLE).value=='--':
            ParameterRepo(user=self.user).set(ParametersEnum.OUR_TEAM_TITLE,'تیم خلاق برای وب بهتر')
        return ParameterRepo(user=self.user).get(ParametersEnum.OUR_TEAM_TITLE)    
    def list(self):
        return self.objects.order_by('priority')
    
class LinkRepo:
    def __init__(self,user=None):
        self.user=user
        self.profile=ProfileRepo(user=user).me
        self.objects=Link.objects.order_by('priority')
    def add(self,title,url,priority):
        link=Link(title=title,url=url,priority=priority)
        link.save()
        return link
    def delete(self,link_id,class_session_id):
        link=self.get(link_id=link_id)
        link.delete()
    def search(self,search_for):
        return self.objects.filter(Q(name__contains=search_for) | Q(link__contains=search_for))
    def get(self,link_id):
        try:
            return self.objects.get(pk=link_id)            
        except:
            return None
    def list(self):
        return self.objects.order_by('priority')

class DocumentRepo:
    def __init__(self,user=None):
        self.objects=Document.objects
        self.user=user
    def list(self):
        return self.objects.all()
    def get(self,document_id):
        try:
            return self.objects.get(pk=document_id)
        except :
            return None

class ProfileRepo:
    
    
    def __init__(self,user=None):
        if user is not None and user.is_authenticated:

            self.user = user
            self.objects = Profile.objects.filter(status=ProfileStatusEnum.ENABLED)
            try:
                self.me = self.objects.filter(user=user).filter(selected=True)[0]          
            except :
                profiles = self.objects.filter(user=user)
                if len(profiles)>0:
                    for profile in profiles:
                        profile.selected=False
                        profile.save()
                    profiles[0].selected=True
                    profiles[0].save()
                    self.me= profiles[0]
                else:
                    self.me=None
                    
        else:
            self.me=None
            self.objects=None
            self.user=None          
        
    def list_all(self):
        if self.user is not None and self.user.is_authenticated:
            return self.objects.all()
    
    def reset_selected_profile(self,user):
        profiles=self.objects.filter(user=user)
        if len(profiles)>0:
            for profile in profiles:
                profile.selected=False
                profile.save()
            profiles[0].selected=True
            profiles[0].save()
            return profiles[0]
        return None
  
    def get_by_user(self,user):
        if user is None or not user.is_authenticated:
            return None
        try:
            profile = self.objects.filter(user=user).filter(selected=True)[0]           
            return profile
        except :
            return self.reset_selected_profile(user=user)
    
    def list_by_user(self,user):
        profiles=self.objects.filter(user=user)
        return profiles
    
    def change_profile(self,user,actived):
        try:
            profile1=self.objects.filter(user=user).get(pk=actived)
            
            profiles=self.objects.filter(user=user)
            for profile in profiles:
                profile.selected=False
                profile.save()
            profile1.selected=True
            profile1.save()
            return profile1
        except:
            pass
        return None
    
    def change_profile_image(self,profile_id,image):
        profile=ProfileRepo(user=self.user).get(profile_id=profile_id)
        if profile is not None:
            profile.image_origin = image
            profile.save()
            return True
        return False
    
    def edit_profile(self,profile_id,first_name,last_name,mobile,region_id,address,bio):
        user=self.user
        if user.is_authenticated:
            profile=self.get_by_user(user)
            if profile.id==profile_id or user.has_perm(APP_NAME+'.change_profile'):
                edited_profile=self.objects.get(pk=profile_id)
                
                if edited_profile is not None:
                    edited_profile.first_name=first_name
                    edited_profile.last_name=last_name
                    edited_profile.mobile=mobile
                    edited_profile.region_id=region_id
                    edited_profile.address=address
                    edited_profile.bio=bio
                    
                    edited_profile.save()
                    return edited_profile
        return None
    
    def reset_password(self,request,username,new_password,old_password=None):
        user=self.user
        try:
            selected_user=User.objects.get(username=username)
        except:
            selected_user=None
        
        if selected_user is not None :            
            if self.user.has_perm(APP_NAME+'.change_profile'):                                    
                selected_user.set_password(new_password)
                selected_user.save()
                if selected_user is not None:
                    return True
            selected_user=authenticate(request=request,username=username,password=old_password)                                    
            if selected_user is not None:
                    selected_user.set_password(new_password)
                    selected_user.save()
                    if selected_user is not None:
                        request=self.login(request=request,username=username,password=new_password)
                        return request
                               
    def get(self,profile_id):
        user=self.user
        profile=self.objects.get(pk=profile_id)
        return profile
        
        
        current_profile=self.get_by_user(user)
        if current_profile is None:
            return None
        if user.has_perm('dashboard.view_profile'):
            profile=self.objects.filter(pk=profile_id)
            if len(profile)==1:
                return profile[0]
        if current_profile.id==profile_id:
            return current_profile
    
    def check_availabe_username(self,username):

        return False if len(User.objects.filter(username=username))>0 else True
    
    def register(self,username,password,first_name,last_name,region_id):
        if not self.check_availabe_username(username):
            return None
        user = User.objects.create_user(username=username,email= 'new_user@khafonline.com', password=password)

        # Update fields and then save again
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profile=Profile(user=user,first_name=first_name,last_name=last_name,region_id=region_id)
        profile.save()
        return profile

    def login(self,request,username,password):
        user=authenticate(request=request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_authenticated:                
                return request  
        return None
    
    def logout(self,request):
        logout(request=request)

class ProfileTransactionRepo:
    def __init__(self,user=None):
        self.objects=ProfileTransaction.objects.order_by('-date_added')
        self.user=user        
        self.profile=ProfileRepo(user=self.user).me
    
    def rest(self,profile_id=None,until_date=None,transaction_id=None):  
      
        if self.profile is not None and profile_id is None:
            profile_id=ProfileRepo(user=self.user).me.id
        transactions=ProfileTransaction.objects         
        transactions_to=transactions.filter(to_profile_id=profile_id)#.aggregate(Sum('amount'))
        transactions_from=transactions.filter(from_profile_id=profile_id)#.aggregate(Sum('amount'))
        if transaction_id is not None:
                transactions=transactions.filter(id__lte=transaction_id)      
            
        if until_date is not None:
                transactions=transactions.filter(date_added__lte=until_date)
        
        
        if len(transactions_to)==0:
            transactions_to={'sum':0}
        else:
            transactions_to=transactions_to.aggregate(sum=Sum('amount'))
        
        if len(transactions_from)==0:
            transactions_from={'sum':0}
        else:
            transactions_from=transactions_from.aggregate(sum=Sum('amount'))
        
        rest=transactions_from['sum']-transactions_to['sum']
        return rest

    def add(self,from_profile_id,to_profile_id,title,amount,cash_type,description):
        transaction=ProfileTransaction(
            from_profile_id=from_profile_id,
            to_profile_id=to_profile_id,
            title=title,
            amount=amount,
            cash_type=cash_type,
            description=description
        )

        transaction.save()
        return transaction
    

    def list(self,profile_id=None,until_date=None,transaction_id=None):
        transactions=self.objects
        if self.profile is not None and profile_id is None:
            profile_id=self.profile.id
        if self.profile is not None:
            transactions=transactions.filter(Q(from_profile_id=profile_id) | Q(to_profile_id=profile_id))
            if transaction_id is not None:
                transactions=transactions.filter(id__lte=transaction_id)      
            
            if until_date is not None:
                transactions=transactions.filter(date_added__lte=until_date)
            
            for transaction in transactions:
                transaction.rest=transaction.rest(profile_id=profile_id)
                transaction.direction=transaction.direction(profile_id)
            return transactions      
    