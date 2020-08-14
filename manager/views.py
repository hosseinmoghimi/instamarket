from dashboard import settings
from .apps import APP_NAME
from dashboard.enums import IconsEnum, ParametersEnum
from .forms import *
from .repo import ContractRepo,ProjectRepo
from dashboard.constants import CURRENCY
from dashboard.repo import DocumentRepo,ProfileTransactionRepo,ProfileRepo,NotificationRepo, RegionRepo
from dashboard.serializers import NotificationSerializer
from django.shortcuts import render,redirect,reverse
from django.views import View
from django.http import Http404
from dashboard.settings import PUSHER_IS_ENABLE
from dashboard.views import getContext as dashboard_context

import json
TEMPLATE_ROOT='manager/'
def getContext(request):
    context=dashboard_context(request=request)
    return context
class BasicView(View):
    def home(self,request,*args, **kwargs):
        user=request.user
        context=getContext(request)
        context['projects']=ProjectRepo(user=user).list()
        context['contracts']=ContractRepo(user=user).list()
        return render(request,TEMPLATE_ROOT+'index.html',context)