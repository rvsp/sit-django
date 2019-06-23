from django import forms
from catalog.models import Book,Author,Genre


class BookForms(forms.Form):
    name = forms.CharField(label='Book Name',
        widget = forms.TextInput(attrs={'maxlength':'30', 'placeholder':'Book Name','class':'form-control'}))
    author = forms.ModelChoiceField(
                    queryset=Author.objects.all(),
                    empty_label='', widget= forms.Select(attrs={'name':'author','id':'author','class':'custom-select'}))
    pur_date = forms.DateField(label='',
                            widget = forms.DateInput(attrs={'placeholder':'Purchase Date','name':'pur_date','id':'pur_date','class':'form-control'}))
    # genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
    #                         widget=forms.CheckboxSelectMultiple)





class ModelBookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','genre','purchase_date','author')
        # fields = '__all__'


class SearchForm(forms.Form):
    q = forms.CharField(label='',
        widget = forms.TextInput(attrs={'maxlength':'30', 'placeholder':'Search','class':'form-control', 'minlength':'2'}))