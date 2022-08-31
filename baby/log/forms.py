from django import forms


from .models import Record


class RecordForm(forms.ModelForm):
    
    kasha = forms.BooleanField(initial=False, required=False, help_text="Кашу?", label='Каша')
    
    class Meta:
        model = Record
        fields = ("text", "pub_date", 'kasha')
        labels = {
            "text": "Количество",
            "pub_date": "Время",
            'kahsa': 'Каша?',
        }
        help_texts = {
            "text": "Введите мл",
            "pub_date": "Введите время",
            'kasha':'Отметьте каша ли это',
        }
        verbose_name = "Форма записи"
