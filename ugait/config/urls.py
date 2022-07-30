from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),

    #django form을 이용하여 사용자 입력값 받아오기 
    #path('formcreate/',views.formcreate, name = 'formcreate'),


    #이미지 파일 

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
