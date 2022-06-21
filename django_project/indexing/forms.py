from dataclasses import fields
from django import forms
from django.contrib.auth.models import User

from .models import (
    CheckPoint,
    GradeServiceSet,
    StudentGroup,
    Students,
    Lecture,
    List_Of_Control_Activities,
    List_Of_Control_Activities_Value,
    Grade
)


class AddGroupStudent(forms.ModelForm):
    """ Форма создания группы учеников """

    class Meta:
        model = StudentGroup
        fields = "__all__"


class UpdateGroupStudent(forms.ModelForm):
    class Meta:
        model = StudentGroup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UpdateGroupStudent, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"


class AddStudent(forms.ModelForm):
    """ Форма создания cтудентов """

    class Meta:
        model = Students
        fields = "__all__"


class AddLecture(forms.ModelForm):
    """ Форма создания Занятий """

    class Meta:
        model = Lecture
        fields = "__all__"


class AddGrade(forms.ModelForm):
    """ Форма создания оценок студентам """

    class Meta:
        model = Grade
        fields = "__all__"


class AddList(forms.ModelForm):
    """ Форма создания листа контрольных мероприятий """

    class Meta:
        model = List_Of_Control_Activities
        fields = "__all__"
        date_input = forms.DateInput(
            format=('%Y/%m/%d'),
            attrs={
                'class': 'form-control', 
                'type': 'date',
                'value': '2022-06-03'
            }
        )
        widgets = {
            'date_of_approval': date_input,
            'check_point_date_start': date_input,
            'check_point_date_end': date_input
        }

    def __init__(self, *args, **kwargs):
        super(AddList, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ['group', 'teacher']:
                visible.field.widget.attrs['class'] = "form-select"
            else:
                visible.field.widget.attrs['class'] = "form-control"


date_input = forms.DateInput(
        format=('%Y/%m/%d'),
        attrs={
            'class': 'form-control', 
            'type': 'date',
            'value': '2022-06-03'
        }
    )


class LCAForm(forms.ModelForm):
    """ Форма создания листа контрольных мероприятий """
    class Meta:
        model = List_Of_Control_Activities
        fields = "__all__"
        widgets = {
            'date_of_approval': date_input,
        }

    def __init__(self, request, *args, **kwargs):
        super(LCAForm, self).__init__(*args, **kwargs)

        self.fields['teacher'].queryset = User.objects.filter(
            id__in=[request.user.id]
        )
        self.fields['group'].queryset = StudentGroup.objects.filter(
            teacher__in=[request.user]
        )

        for visible in self.visible_fields():
            if visible.name in ['group', 'teacher']:
                visible.field.widget.attrs['class'] = "form-select"
            else:
                visible.field.widget.attrs['class'] = "form-control"


class GSSForm(forms.ModelForm):
    class Meta:
        model = GradeServiceSet
        fields = '__all__'

    def __init__(self, pk, *args, **kwargs):
        super(GSSForm, self).__init__(*args, **kwargs)
        self.fields['check_point'].queryset = CheckPoint.objects.filter(
            lca_id=pk
        )
        fields_with_select = [
            'check_point',
            'grade_service',
            'form_holding',
            'order_holding'
        ]
        for visible in self.visible_fields():
            if visible.name in fields_with_select:
                visible.field.widget.attrs['class'] = "form-select"
            else:
                visible.field.widget.attrs['class'] = "form-control"


class CheckPointForm(forms.ModelForm):
    class Meta:
        model = CheckPoint
        fields = ('number', 'date')
        widgets = {
            'date': date_input,
        }

    def __init__(self, *args, **kwargs):
        super(CheckPointForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"


CheckPointFormSet = forms.inlineformset_factory(
    List_Of_Control_Activities,
    CheckPoint,
    form=CheckPointForm,
    fields = ('number', 'date'),
    extra=2,
    can_delete=False
)


class AddValue(forms.ModelForm):
    """ Форма создания содержимого в листе контрольных мероприятий """

    class Meta:
        model = List_Of_Control_Activities_Value
        fields = "__all__"
