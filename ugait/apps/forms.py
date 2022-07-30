from dataclasses import field, fields
from django import forms
from .models import Guide, Member

#입력받고자 하는 값 
class MemberNameForm(forms.ModelForm):
    class Meta: 
        model = Member
        fields = ['mb_nm']

class GuideImageForm(form,ModelForm):
    class Meta:
        model = Guide
        fields =[' guide_profile']