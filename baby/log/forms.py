from django import forms


from .models import Record


class RecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ('text', 'pub_date')
        labels = {
            'text': 'Колиичество',
            'pub_date': 'Время',
        }
        help_texts = {
            'text': 'Введите мл',
            'pub_date': 'Введите время',
        }
        verbose_name = 'Форма сообщения'