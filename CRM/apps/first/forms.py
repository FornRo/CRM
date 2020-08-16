from django.core.exceptions import ValidationError

from django import forms

# from .models import Record, Project, Interaction
from .models import CompanyAddress, Descriptin, Record, Project, \
    Communication, Interaction


class CompanyAddressForm(forms.ModelForm):
    class Meta:
        model = CompanyAddress
        fields = ('address', 'phone_number', 'e_mail')
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон format "097 1593 367"',
                'type': 'tel',
                'pattern': "[0-9]{3} [0-9]{4} [0-9]{3}"
            }),
            'e_mail': forms.EmailInput(attrs={

                'class': 'form-control',
                'placeholder': 'Введите e-mail'
            })
        }


class DescriptinForm(forms.ModelForm):
    class Meta:
        model = Descriptin
        fields = ('description', )
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Описание'
            })
        }


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('name_company', 'name_manager', 'description_id', 'address')
        widgets = {
            'description_id': forms.Select(attrs={
                'id': 'description_id',
                'name': 'description_id',
                'class': 'form-control m-2'
            }),
            'address': forms.Select(attrs={
                'id': 'address_id',
                'name': 'address_id',
                'class': 'form-control m-2',
            }),
            'name_company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название компании'
            }),
            'name_manager': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО руководителя'
            })
        }


class ProjectForm(forms.ModelForm):
    CHOICES = [('1', 'True'), ('2', 'False')]
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Project
        fields = ('name_project', 'description_id', 'start_date', 'deadline', 'cost', 'status')
        widgets = {
            'name_project': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название компании'
            }),
            'description_id': forms.Select(attrs={
                'id': 'description_id',
                'name': 'description_id',
                'class': 'form-control m-2'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'step': 'any',
                'placeholder': 'Введите стоймость проекта Format: 1 < n'
            }),
            'status': forms.RadioSelect(attrs={
                'class': 'form-control',
                'type': 'radio'
            })
        }


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ('__all__' )
        widgets = {
            'communication': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите взаимодействия'
            })
        }

class InteractionForm(forms.ModelForm):
    appraisal = forms.IntegerField(min_value=0, max_value=10)  # оценки от 0 до 10
    class Meta:
        model = Interaction
        fields = ('project_id', 'company_id', 'communication_id', 'name_manager', 'description_id', 'appraisal')
        widgets = {
            'project_id': forms.Select(attrs={
                'id': 'project_id',
                'name': 'project_id',
                'class': 'form-control m-2'
            }),
            'company_id': forms.Select(attrs={
                'id': 'company_id',
                'name': 'company_id',
                'class': 'form-control m-2'
            }),
            'communication_id': forms.Select(attrs={
                'id': 'communication_id',
                'name': 'communication_id',
                'class': 'form-control m-2'
            }),
            'name_manager': forms.TextInput(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Введите ФИО менеджера'
            }),
            'description_id': forms.Select(attrs={
                'id': 'description_id',
                'name': 'description_id',
                'class': 'form-control m-2'
            })
        }

# 'appraisal': forms.NumberInput(attrs={
#                 'class': 'form-control m-2',
#                 'type': 'number',
#                 'min': '1',
#                 'max': '10',
#                 'placeholder': 'Введите оценку'
#             })
# class DogRequestForm(f eld(queryset=Speed.objects.all())
        # labels = {}
