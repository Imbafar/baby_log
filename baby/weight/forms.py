from django import forms


from .models import Weight


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ("amount", "pub_date")
        labels = {
            "amount": "Вес",
            "pub_date": "Время",
        }
        help_texts = {
            "amount": "Введите граммы",
            "pub_date": "Введите время",
        }
        verbose_name = "Форма записи"
