from django import forms
from enroll.models import Enrollment, Program
from django.core.validators import FileExtensionValidator

class EnrollmentForm(forms.ModelForm):
    program = forms.ModelChoiceField(
        queryset=Program.objects.filter(is_active=True),
        empty_label="Choose a program"
    )
    
    transcript = forms.FileField(
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])]
    )
    
    id_proof = forms.FileField(
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])]
    )

    class Meta:
        model = Enrollment
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'enrollment_type': forms.RadioSelect()
        }