from rest_framework import serializers
from .models import Profile,Link,Notification


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','name','image','get_absolute_url']      

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields=['id','title','url','row_number']      

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=['id','title','link','get_absolute_url','icon','body','seen','date_added','color']