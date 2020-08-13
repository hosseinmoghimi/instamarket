from django.shortcuts import render,reverse,redirect
from django.http import JsonResponse,Http404,HttpResponse
from django.views import View
TEMPLATE_ROOT='dashboard/'

def getContext(request):
    context={}
    context['title']='instamarket'
    return context
class IndexView(View):
    def home(self,request,*args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+'index.html',context)