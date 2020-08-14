from django.contrib import admin
from .models import Document,ProfileTransaction, Region,Link,MetaData,Notification,Profile,SocialLink,OurTeam,OurService,GalleryPhoto,Testimonial,Blog,Parameter,ContactMessage,FAQ,MainPic


admin.site.register(Document)
admin.site.register(ProfileTransaction)
admin.site.register(Link)
admin.site.register(MetaData)
admin.site.register(Notification)
admin.site.register(Profile)
admin.site.register(FAQ)
admin.site.register(SocialLink)
admin.site.register(Blog)
admin.site.register(OurTeam)
admin.site.register(MainPic)
admin.site.register(Parameter)
admin.site.register(OurService)
admin.site.register(Testimonial)
admin.site.register(GalleryPhoto)
admin.site.register(ContactMessage)
admin.site.register(Region)
# Register your models here.
