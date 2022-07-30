from django.contrib import admin
from .models import Member
from .models import Guide
from .models import Guide_Lang
from .models import GuideMatching



# Register your models here.
admin.site.register(Member)
admin.site.register(Guide)
admin.site.register(Guide_Lang)
admin.site.register(GuideMatching)