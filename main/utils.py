from .models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Categories.objects.all()
        context['categories'] = categories
        return context