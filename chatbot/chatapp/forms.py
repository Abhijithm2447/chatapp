from django import forms
from chatapp.models import QueryDB, IntentDB

class QueryForm(forms.ModelForm):
    class Meta:
        model = QueryDB
        fields = '__all__'

class IntentForm(forms.ModelForm):
    class Meta:
        model = IntentDB
        fields = '__all__'
