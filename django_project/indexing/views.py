from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    DeleteView,
)
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import (
    AddStudent,
    AddGroupStudent,
    AddLecture,
    AddGrade,
    AddValue,
    AddList,
    CheckPointFormSet,
    GSSForm,
    LCAForm,
    UpdateGroupStudent,
)
from .models import *
from .serialisers import (
    GradeItemSerializer,
    GradeResultSerializer,
    ResultSerializer
)


def index(request):
    lecture = Lecture.objects.filter(teacher__username=request.user)
    context = {
        'lecture': lecture,
    }
    if request.user.is_authenticated:
        temp = 'profile/index.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


def profile(request):
    lecture = Lecture.objects.filter(teacher__username=request.user)
    context = {
        'lecture': lecture,
    }
    if request.user.is_authenticated:
        temp = 'profile/index.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


# -------------------------------------------------------------------


class CreateGroup(CreateView):
    """ Форма создания группы студентов """
    template_name = 'profile/create_group.html'
    form_class = AddGroupStudent
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class GroupListView(ListView):
    model = StudentGroup
    template_name = 'profile/student_groups.html'


class GroupUpdateView(UpdateView):
    model = StudentGroup
    form_class = UpdateGroupStudent
    success_url = '/'
    template_name = 'profile/update_group.html'


class CreateStudent(CreateView):
    """ Форма создания студентов """
    template_name = 'profile/create_student.html'
    form_class = AddStudent
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateLecture(CreateView):
    """ Форма создания Занятий """
    template_name = 'profile/create_lecture.html'
    form_class = AddLecture
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateGrade(CreateView):
    """ Форма создания оценок для студентов """
    template_name = 'profile/create_grade.html'
    form_class = AddGrade
    success_url = '/accounts/profile/table'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateList(CreateView):
    """ Форма создания ЛКМ """
    template_name = 'profile/create_list.html'
    form_class = AddList
    success_url = '/accounts/profile/table-list'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


class CreateValue(CreateView):
    """ Форма создания значений """
    template_name = 'profile/create_value.html'
    form_class = AddValue
    success_url = '/accounts/profile/table-list'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            # Try to dispatch to the right method; if a method doesn't exist,
            # defer to the error handler. Also defer to the error handler if the
            # request method isn't on the approved list.
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("login")


# -------------------------------------------------------------------
def table(request):
    tables = Grade.objects.filter(teacher__username=request.user)
    context = {
        'table': tables,
    }
    if request.user.is_authenticated:
        temp = 'profile/table-data.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)


def table_list(request):
    tables = List_Of_Control_Activities.objects.all().filter(teacher__username=request.user)
    context = {
        'rows': tables
    }
    if request.user.is_authenticated:
        temp = 'profile/table-data-list.html'
    else:
        temp = 'account/login.html'
    return render(request, temp, context)

def table_delate(request, pk):
    tables = Grade.objects.get(id=pk)
    tables.delete()
    return redirect('/accounts/profile/table')


class Update_Table_View(UpdateView):
    model = Grade
    template_name = 'profile/create_grade.html'
    form_class = AddGrade
    success_url = '/accounts/profile/table'



class LCACreateView(CreateView):
    template_name = 'profile/create_lca.html'
    form_class = LCAForm
    
    def get_success_url(self):
        return reverse('Index:lca-detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checkpoint_formset'] = CheckPointFormSet()
        return context

    def get_form_kwargs(self):
        kwargs = super(LCACreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        checkpoint_formset = CheckPointFormSet(self.request.POST or None)
        if form.is_valid() and checkpoint_formset.is_valid():
            return self.form_valid(form, checkpoint_formset)
        else:
            return self.form_invalid(form, checkpoint_formset)

    def form_valid(self, form, checkpoint_formset):
        self.object = form.save(commit=False)
        self.object.save()
        checkpoints = checkpoint_formset.save(commit=False)
        for checkpoint in checkpoints:
            checkpoint.lca = self.object
            checkpoint.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, checkpoint_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                checkpoint_formset=checkpoint_formset
            )
        )


class LCADetailView(DetailView):
    model = List_Of_Control_Activities
    template_name = 'profile/lca_detail.html'


class LCAPrintView(DetailView):
    model = List_Of_Control_Activities
    template_name = 'pdf/lca_detail.html'


class PerformancePrintView(DetailView):
    model = List_Of_Control_Activities
    template_name = 'pdf/performance.html'

    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs['pk']
    #     context = super().get_context_data(**kwargs)
    #     context['results'] = GradeResult.objects.filter(
    #         grade_item__grade_service_set__check_point__lca=pk
    #     ).values(
    #         'student',
    #         'grade_item__grade_service_set__check_point'
    #     ).annotate(result=Sum('score'))
    #     return context



class LCADeleteView(DeleteView):
    model = List_Of_Control_Activities
    success_url = reverse_lazy('Index:table-list')


class GradeServiceCreateView(CreateView):
    model = GradeService
    fields = '__all__'
    template_name = 'profile/create_grade_service.html'
    success_url = reverse_lazy('Index:profile')


class FormHoldingCreateView(CreateView):
    model = FormHolding
    fields = '__all__'
    template_name = 'profile/create_form_holding.html'
    success_url = reverse_lazy('Index:profile')


class OrderHoldingCreateView(CreateView):
    model = OrderHolding
    fields = '__all__'
    template_name = 'profile/create_order_holding.html'
    success_url = reverse_lazy('Index:profile')


class GradeServiceSetCreateView(CreateView):
    form_class = GSSForm
    template_name = 'profile/create_gss.html'

    def get_form_kwargs(self):
        kwargs = super(GradeServiceSetCreateView, self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        n = int(form['evaluation_quantity'].value())
        objs = [GradeItem(grade_service_set=self.object) for i in range(n)]
        GradeItem.objects.bulk_create(objs)

        return redirect(reverse(
            'Index:lca-detail',
            kwargs={'pk': self.object.check_point.lca.pk}
            )
        )


class GradeItemUpdateAPIView(UpdateAPIView):
    serializer_class = GradeItemSerializer
    queryset = GradeItem.objects.all()


class GradeResultViewSet(viewsets.ModelViewSet):
    serializer_class = GradeResultSerializer
    
    def get_queryset(self):
        pk = self.kwargs['lca_id']
        queryset = GradeResult.objects.filter(
            grade_item__grade_service_set__check_point__lca=pk
        )
        return queryset


class ResultAPIView(APIView):
    def get(self, request, lca_id,format=None):
        rates = GradeResult.objects.filter(
            grade_item__grade_service_set__check_point__lca=lca_id
        ).values('student_id', 'grade_item__grade_service_set__check_point').annotate(result=Sum('score'))
        serializer = ResultSerializer(rates, many=True)
        return Response(serializer.data)
