from django import forms
from .validators import validate_file_size

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField(validators=[validate_file_size])
    private = forms.BooleanField(required=False)
    date_expired = forms.DateTimeField(required=False)
