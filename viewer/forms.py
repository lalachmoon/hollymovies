import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import (
    CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, DateInput, ModelForm
)

from viewer.models import Genre, Movie


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')

class DateInput(DateInput):
    input_type = 'date'



class MyModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'my_date': DateInput()
        }

class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=result.day)

class MovieForm(ModelForm):

    #If I add this class Django is creating the rest of the fields by himself
    class Meta:
        model = Movie
        fields = '__all__'
    # So I can comment the fields where i didn't inserted unique specifications
    title = CharField(max_length=128)
    # genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField(widget=DateInput)
    # description = CharField(widget=Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'commedy' and result['rating'] > 5:
            self.add_error('genre' '')
            self.add_error('rating' '')
            raise ValidationError(
                "Commedies aren't so good to be rated over 5."
            )
        return result