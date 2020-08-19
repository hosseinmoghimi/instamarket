from .models import Entry,EntryDetail
from dashboard.repo import ProfileRepo
class EntryRepo:
    def __init__(self,user):
        self.user=user
        self.profile=ProfileRepo(user=user).me
        self.objects=Entry.objects
    def list(self):
        if self.profile is not None:
            return self.objects.filter(profile=self.profile)
    def get(self,entry_id):
        if self.profile is not None:
            try:
                entry=self.objects.get(pk=entry_id)
                if entry.profile==self.profile:
                    return entry
            except:
                pass
        return None
        

class EntryDetailRepo:
    def __init__(self,user):
        self.user=user
        self.profile=ProfileRepo(user=user).me
        self.objects=EntryDetail.objects
    def search(self,entry_id):
        if self.profile is not None:
            return self.objects.filter(profile=self.profile)