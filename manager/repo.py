from .models import Contract,Project
from dashboard.repo import ProfileRepo
class ContractRepo():
    def __init__(self,user=None):
        self.user=user
        self.objects=Contract.objects
    def list(self):
        profile=ProfileRepo(user=self.user).me
        if profile is not None:
            return self.objects.filter(contractor=profile)

class ProjectRepo():
    def __init__(self,user=None):
        self.user=user
        self.objects=Project.objects
    def list(self):
        profile=ProfileRepo(user=self.user).me
        if profile is not None:
            return self.objects.filter(employer=profile)
    