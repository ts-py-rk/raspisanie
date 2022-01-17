from .models import Month
from django.forms import ModelForm, TextInput, Select
class MonthForm(ModelForm):
    class Meta:
        model = Month
        fields = ['id']
        # fields = ['person', 'day']
        widgets = {
            'id': Select(
                attrs={
                    'class': 'familia_calss',
                    'placeholder': '12346'
                }),
            # 'day': TextInput(
            #     attrs={
            #         'class': 'day',
            #         'placeholder': '12346',
            #         'value': 'qwewq'
            #     })
        }