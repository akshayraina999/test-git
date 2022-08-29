from django import forms  
from .models import Employee, Posts


class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['blog_id', 'title', 'body', 'category']
        # fields = "__all__"