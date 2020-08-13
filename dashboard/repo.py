from .models import Link
class LinkRepo:
    def __init__(self):
        self.objects=Link.objects
    def list(self):
        return self.objects.all()