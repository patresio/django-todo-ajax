from django import forms
from .models import Status, TodoList

class TodoListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ('titulo',)
        exclude = ('status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'