from django import forms
from app20.models import courseModel,studentModel

class courseForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = courseModel

class studentForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = studentModel