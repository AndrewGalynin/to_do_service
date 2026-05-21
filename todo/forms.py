from django import forms

from todo.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'deadline': forms.DateTimeInput(
                # Вказуємо формат для правильного відображення дати при редагуванні
                format='%Y-%m-%dT%H:%M',
                # Змінюємо тип інпуту на HTML5 віджет календаря
                attrs={'type': 'datetime-local'}
            ),
        }