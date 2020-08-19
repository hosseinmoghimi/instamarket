from django.shortcuts import render
from dashboard.views import getContext as dashboardContext
from django.views import View
from .repo import EntryRepo
TEMPLATE_ROOT='phonebook/'
def getContext(request):
    context=dashboardContext(request=request)
    return context

class IndexView(View):
    def home(self,request,*args, **kwargs):
        user=request.user
        context=getContext(request=request)
        context['entries']=EntryRepo(user=user).list()
        return render(request,TEMPLATE_ROOT+'index.html',context)
    def entry(self,request,entry_id,*args, **kwargs):
        user=request.user
        context=getContext(request=request)
        entry=EntryRepo(user=user).get(entry_id=entry_id)
        # print(entry)
        context['entry']=entry
        return render(request,TEMPLATE_ROOT+'entry.html',context)