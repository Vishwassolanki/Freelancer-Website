from django.contrib import admin

from .models import user_profile

# Register your models here.

admin.site.register(user_profile)
from .models import extendeduser

admin.site.register(extendeduser)
from .models import reviews_user

admin.site.register(reviews_user)
