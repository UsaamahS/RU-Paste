from django.core.exceptions import ValidationError
import os

#checking to see if the file is valid and under 10 mb
def validate_file_size(value):
    filesize= value.size
    file_extension = os.path.splitext(value.name)[1]

    if filesize > 10485760 or file_extension != '.txt':
        raise ValidationError("invalid file")
    else:
        return value
