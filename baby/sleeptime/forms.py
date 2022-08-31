from django import forms


from .models import SLeepTime


class SleepTimeForm(forms.ModelForm):
    class Meta:
        model = SLeepTime
        fields = ("pub_date_start", "pub_date_end")
        # labels = {
        #     "amount": "Вес",
        #     "pub_date": "Время",
        # }
        # help_texts = {
        #     "amount": "Введите граммы",
        #     "pub_date": "Введите время",
        # }
        # verbose_name = "Форма записи"
