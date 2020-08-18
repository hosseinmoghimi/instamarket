from django.http import HttpResponse,Http404
import uuid 
from .apps import APP_NAME
from .enums import ResumeCategoryEnum,IconsEnum, TransactionDirectionEnum, ColorEnum, ParametersEnum, PicEnum, ProfileStatusEnum, RegionEnum, TransactionTypeEnum
from .constants import FORCE_RESIZE_IMAGE,SHIPPER_IMAGE_WIDTH,SHIPPER_IMAGE_HEIGHT,SUPPLIER_IMAGE_WIDTH,SUPPLIER_IMAGE_HEIGHT,PRODUCT_IMAGE_WIDTH,PRODUCT_IMAGE_HEIGHT,PRODUCT_IMAGE_HEIGHT,PRODUCT_THUMBNAIL_WIDTH,PRODUCT_THUMBNAIL_HEIGHT,CATEGORY_IMAGE_WIDTH,CATEGORY_IMAGE_HEIGHT,PROFILE_IMAGE_WIDTH,PROFILE_IMAGE_HEIGHT
from .persian import PersianCalendar
from .settings import *
from .utils import get_qrcode
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models import Avg, Max, Min,F,Q,Sum
from django.shortcuts import reverse
from django.utils.translation import gettext as _
from io import BytesIO
from datetime import datetime
from PIL import Image
import sys
import os
IMAGE_FOLDER=APP_NAME+'/images/'



class Link(models.Model):
    priority=models.IntegerField(_("priority"),default=100)
    title=models.CharField(_("title"), max_length=50)
    url=models.CharField(_("url"), max_length=1100)
    color=models.CharField(_("color"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    icon=models.CharField(_("icon"),choices=IconsEnum.choices,default=IconsEnum.link, max_length=50)
    image_origin=models.ImageField(_("image"), upload_to=IMAGE_FOLDER+'Link/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    
    
    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.url

class HomeSlider(models.Model):
    title=models.CharField(_("عنوان"), max_length=500,blank=True,null=True)
    body=models.CharField(_("پیام"), max_length=500,blank=True,null=True)
    image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'HomeSlider/', height_field=None, width_field=None, max_length=None)
    action_link=models.CharField(_("لینک"), max_length=1100,blank=True,null=True)
    action_text=models.CharField(_("متن دکمه"), max_length=50,blank=True,null=True)
    priority=models.IntegerField(_("ترتیب"),default=100)
    class Meta:
        verbose_name = _("HomeSlider")
        verbose_name_plural = _("HomeSliders")
    def image(self):
        return MEDIA_URL+str(self.image_origin)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("HomeSlider_detail", kwargs={"pk": self.pk})

class Profile(models.Model):
    region = models.ForeignKey("Region", verbose_name=_("region"), on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,null=True,blank=True
    )
    status = models.CharField(_("وضعیت"), max_length=50,choices=ProfileStatusEnum.choices,default=ProfileStatusEnum.ENABLED)
    first_name = models.CharField(_("نام"), max_length=200)
    last_name = models.CharField(_("نام خانوادگی"), max_length=200)
    mobile = models.CharField(_("موبایل"), max_length=50,null=True,blank=True)
    bio = models.CharField(_("درباره"), max_length=500,null=True,blank=True)
    image_origin = models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'Profile/', height_field=None, width_field=None, max_length=1200,blank=True,null=True)
    
    def name(self):
        return self.first_name+' '+self.last_name
    def get_my_qrcode(self):
        self.save_qrcode()
        return f'{APP_NAME}/images/Profile/{self.pk}.svg'

    def save_qrcode(self):
        try:
            data={
                'profile_id':self.pk,
                'name':self.name,
                'image':SITE_DOMAIN+self.image(),
            }
            img=get_qrcode(data=data)
            file_name=os.path.join(os.path.join(os.path.join(os.path.join(MEDIA_ROOT,APP_NAME),'images'),'Profile'),str(self.pk)+".svg")
            img.save(file_name)
        except :
            pass
        

    def image(self):
        if self.image_origin:
            return MEDIA_URL+str(self.image_origin)
        else:
            return STATIC_URL+'dashboard/img/default_avatar.png'
    def save(self):  
        
        old_image=None      
        try:
            old_image=Profile.objects.get(pk=self.pk).image_origin
        except:
            pass
        if not self.image_origin :
             super(Profile,self).save()
        elif old_image is not None and str(self.image_origin)==str(Profile.objects.get(pk=self.pk).image_origin):
            super(Profile,self).save()
        elif self.image_origin and FORCE_RESIZE_IMAGE:
            #Opening the uploaded image
            image = Image.open(self.image_origin)       
            output = BytesIO()     
            #Resize/modify the image
            image = image.resize( (PROFILE_IMAGE_WIDTH, PROFILE_IMAGE_HEIGHT), Image.ANTIALIAS )
            
            #after modifications, save it to the output
            image.save(output, format='JPEG', quality=95)
           
            output.seek(0)  
            #change the imagefield value to be the newley modifed image value
            self.image_origin = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image_origin.name.split('.')[0], IMAGE_FOLDER+'Profile/image/jpeg', sys.getsizeof(output), None)
            
        super(Profile,self).save()
        

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f'{self.name()} : {self.user.username}'

    def get_absolute_url(self):
        return reverse("dashboard:profile", kwargs={"profile_id": self.pk})
    def get_transactions_url(self):
        return reverse("dashboard:transactions", kwargs={"profile_id": self.pk})
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/profile/{self.pk}/change/'

class Region(models.Model):
    name=models.CharField(_("name"), max_length=50,choices=RegionEnum.choices,default=RegionEnum.KHAF)
    

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Region_detail", kwargs={"pk": self.pk})

class Notification(models.Model):
    profile=models.ForeignKey("Profile", verbose_name=_("پروفایل"), on_delete=models.CASCADE)
    title=models.CharField(_("عنوان"), max_length=50)
    body=models.CharField(_("توضیحات"), max_length=500,null=True,blank=True)
    link=models.CharField(_("link"), max_length=1100,blank=True,null=True)
    seen=models.BooleanField(_('دیده شد'),default=False)
    priority=models.IntegerField(_("اولویت"),default=1000)
    date_added=models.DateTimeField(_('تاریخ ایجاد'),auto_now_add=True,auto_now=False)
    date_seen=models.DateTimeField(_('تاریخ دیده شده'),auto_now_add=False,auto_now=False,null=True,blank=True)
    icon=models.CharField(_("آیکون"), max_length=50,default='notification_important')
    color=models.CharField(_("رنگ"), choices=ColorEnum.choices,default=ColorEnum.INFO, max_length=500,null=True,blank=True)
    # def send(self,user,channel_name,event_name):
    #     try:
    #           PusherChannelEventRepo(user=user).get(channel_name,event_name).send_message(
            
    #         {
    #             'body':self.body,
    #             'title':self.title,
    #             'color':self.color,
    #             'icon':self.icon,
    #             'link':self.link,
    #             'get_absolute_url':self.get_absolute_url(),
    #         }
            
    #         )
    #     except expression as identifier:
    #         pass
      


    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("dashboard:notification", kwargs={"notification_id": self.pk})

class MetaData(models.Model):
    key=models.CharField(_("key name"), max_length=50,default='name')
    value=models.CharField(_("key value"), max_length=50)
    content=models.CharField(_("content"), max_length=2000)
    class Meta:
        verbose_name = _("MetaData")
        verbose_name_plural = _("MetaDatas")

    def __str__(self):
        return f'{self.key} : {self.value}'

    def get_absolute_url(self):
        return reverse("MetaData_detail", kwargs={"pk": self.pk})

class MainPic(models.Model):
    name=models.CharField(_("جای تصویر"), max_length=50,choices=PicEnum.choices)    
    image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'MainPic/', height_field=None, width_field=None, max_length=None,null=True,blank=True)

    class Meta:
        verbose_name = _("MainPic")
        verbose_name_plural = _("MainPics")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MainPic_detail", kwargs={"pk": self.pk})

class ContactMessage(models.Model):
    fname=models.CharField(_("نام"), max_length=50)
    lname=models.CharField(_("نام خانوادگی"), max_length=50)
    email=models.EmailField(_("ایمیل"), max_length=254)
    subject=models.CharField(_("عنوان پیام"), max_length=50)
    message=models.CharField(_("متن پیام"), max_length=50)
    date_added=models.DateTimeField(_("افزوده شده در"), auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = _("ContactMessage")
        verbose_name_plural = _("ContactMessages")

    def __str__(self):
        return self.email+"     "+str(self.date_added)

    def get_absolute_url(self):
        return reverse("ContactMessage_detail", kwargs={"pk": self.pk})

class Parameter(models.Model):
    name=models.CharField(_("نام"), max_length=50,choices=ParametersEnum.choices)
    value=models.CharField(_("مقدار"), max_length=10000)
    

    class Meta:
        verbose_name = _("Parameter")
        verbose_name_plural = _("Parameters")

    def __str__(self):
        return f'{self.name} : {self.value}'

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/parameter/{self.pk}/change/'

class FAQ(models.Model):

    number=models.IntegerField(_("شماره"))
    question=models.CharField(_("سوال"), max_length=200)
    answer=models.CharField(_("پاسخ"), max_length=5000)
    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("FAQ_detail", kwargs={"pk": self.pk})

class Blog(models.Model):

    title=models.CharField(_("عنوان"), max_length=50)
    short_desc=models.CharField(_("شرح کوتاه"), max_length=1000)
    description=models.CharField(_("شرح کامل"), max_length=10000)
    thumb_image_origin=models.ImageField(_("تصویر کوچک"), upload_to=IMAGE_FOLDER+'Blog/', height_field=None, width_field=None, max_length=None)
    big_image_origin=models.ImageField(_("تصویر بزرگ"), upload_to=IMAGE_FOLDER+'Blog/big/', height_field=None, width_field=None, max_length=None)
    priority=models.IntegerField(_("ترتیب"))
    author=models.CharField(_("توسط"), max_length=50)
    date_added=models.CharField(_("تاریخ"), max_length=50)
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})

class Testimonial(models.Model):
    image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'Testimonial/', height_field=None, width_field=None, max_length=None)
    title=models.CharField(_("عنوان"), max_length=2000)
    body=models.CharField(_("متن"), max_length=2000)
    footer=models.CharField(_("پانوشت"), max_length=200)
    priority=models.IntegerField(_("ترتیب"))
    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})

class OurService(models.Model):
    title=models.CharField(_("عنوان"), max_length=50)
    icon=models.CharField(_("آیکون"), max_length=50,choices=IconsEnum.choices,default=IconsEnum.settings)
    description=models.CharField(_("توضیحات"), max_length=500)
    priority=models.IntegerField(_("ترتیب"))
    class Meta:
        verbose_name = _("OurService")
        verbose_name_plural = _("OurServices")

    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse("OurService_detail", kwargs={"pk": self.pk})

class GalleryPhoto(models.Model):
    title=models.CharField(_("عنوان"), max_length=50)
    thumb_image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'GalleryPhoto/', height_field=None, width_field=None, max_length=None)
    image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'GalleryPhoto/', height_field=None, width_field=None, max_length=None)
    
    priority=models.IntegerField(_("ترتیب"))
    class Meta:
        verbose_name = _("GalleryPhoto")
        verbose_name_plural = _("GalleryPhotoes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("GalleryPhoto_detail", kwargs={"pk": self.pk})

class SocialLink(models.Model):
    name=models.CharField(_("نام"), max_length=50)
    icon=models.CharField(_("آیکون"),choices=IconsEnum.choices,default=IconsEnum.settings, max_length=50)
    color=models.CharField(_("رنگ"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    link=models.CharField(_("لینک"), max_length=50)
    priority=models.IntegerField(_("ترتیب"))

    class Meta:
        verbose_name = _("شبکه اجتماعی")
        verbose_name_plural = _("SocialLinks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.link

class OurTeam(models.Model):
    name=models.CharField(_("نام"), max_length=100)
    job=models.CharField(_("سمت"), max_length=100)
    description=models.CharField(_("توضیحات"), max_length=500)
    priority=models.IntegerField(_("ترتیب"))
    image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'OurTeam/', height_field=None, width_field=None, max_length=None)
    social_links=models.ManyToManyField("SocialLink", verbose_name=_("social_links"),blank=True)
    resume_categories=models.ManyToManyField("ResumeCategory", verbose_name=_("ResumeCategories"))
    def __str__(self):
        return self.name
    def get_resume_url(self):
        return reverse('dashboard:resume',kwargs={'our_team_id':self.pk})
    def image(self):
        if self.image_origin:
            return MEDIA_URL+str(self.image_origin)
        else:
            return STATIC_URL+'dashboard/img/default_avatar.png'
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'OurTeam'
        managed = True
        verbose_name = 'OurTeam'
        verbose_name_plural = 'OurTeams'

class ProfileTransaction(models.Model):
    from_profile_id=models.IntegerField(_('از'))
    to_profile_id=models.IntegerField(_('به'))
    title=models.CharField(_("عنوان"), max_length=50)
    amount=models.IntegerField(_("مبلغ"))
    cash_type=models.CharField(_("نوع پرداخت"),choices=TransactionTypeEnum.choices,default=TransactionTypeEnum.CASH, max_length=50)
    description=models.CharField(_("شرح"), max_length=50,null=True,blank=True)
    date_added=models.DateTimeField(_("ایجاد شده در "), auto_now=False, auto_now_add=True)
    def from_profile(self):
        try:
            return Profile.objects.get(pk=self.from_profile_id)
        except:
            return None
    def to_profile(self):
        try:
            return Profile.objects.get(pk=self.to_profile_id)
        except:
            return None
    class Meta:
        verbose_name = _("ProfileTransaction")
        verbose_name_plural = _("ProfileTransactions")
    def get_balanced_amount(self,profile_id=None):
        if profile_id is None:
            return None
        if self.to_profile_id==profile_id:
            return 0-self.amount
        if self.from_profile_id==profile_id:
            return self.amount
        return None 
    def direction(self,profile_id):
        if self.to_profile_id==profile_id:
            return TransactionDirectionEnum.TO_PROFILE
        
        if self.from_profile_id==profile_id:
            return TransactionDirectionEnum.FROM_PROFILE
        
    def rest(self,profile_id):
        rest=0
        transactions=ProfileTransaction.objects.filter(id__lte=self.pk) 
        transactions_to=transactions.filter(to_profile_id=profile_id)
        transactions_from=transactions.filter(from_profile_id=profile_id)
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
    def __str__(self):
        return f'{self.title} {self.amount}'

    def get_absolute_url(self):
        return reverse("Transaction_detail", kwargs={"pk": self.pk})

class Document(models.Model):
    profile=models.ForeignKey("Profile", verbose_name=_("پروفایل"), on_delete=models.CASCADE)
    title=models.CharField(_("title"), max_length=50)
    file=models.FileField(_("فایل ضمیمه"), upload_to=IMAGE_FOLDER+'Document', max_length=100)
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    row_number=models.IntegerField(_("row_number"),default=10000)
    icon=models.CharField(_("آیکون"),choices=IconsEnum.choices,default=IconsEnum.get_app, max_length=50)
    color=models.CharField(_("رنگ"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    
    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
    def get_download_url(self):
        return reverse('dashboard:download',kwargs={'document_id':self.pk})
    def download(self):
        
    #STATIC_ROOT2 = os.path.join(BASE_DIR, STATIC_ROOT)
        file_path = str(self.file.path)
        #print(file_path)
        #return JsonResponse({'download:':str(file_path)})
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/force-download")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("dashboard:document", kwargs={"document_id": self.pk})

class ResumeCategory(models.Model):
    our_team=models.ForeignKey("OurTeam", verbose_name=_("our_team"), on_delete=models.CASCADE)
    resumes=models.ManyToManyField("Resume", verbose_name=_("resume"))
    title=models.CharField(_("title"),choices=ResumeCategoryEnum.choices,default=ResumeCategoryEnum.EDUCATION, max_length=50)
    priority=models.IntegerField(_("priority"))

    class Meta:
        verbose_name = _("ResumeCategory")
        verbose_name_plural = _("ResumeCategorys")

    def __str__(self):
        return f'{self.our_team.name} -> {self.title}'

    def get_absolute_url(self):
        return reverse("ResumeCategory_detail", kwargs={"pk": self.pk})


class Resume(models.Model):
    priority=models.IntegerField(_("priority"))
    title=models.CharField(_("title"), max_length=50)
    subtitle=models.CharField(_("subtitle"), max_length=50)
    description=models.CharField(_("description"), max_length=500)
    date=models.DateTimeField(_("date"), auto_now=False, auto_now_add=False)
    links=models.ManyToManyField("Link", verbose_name=_("links"),blank=True)
    documents=models.ManyToManyField("Document", verbose_name=_("documents"),blank=True)
    

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Resume_detail", kwargs={"pk": self.pk})



