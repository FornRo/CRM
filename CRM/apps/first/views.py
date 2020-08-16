from django.shortcuts import render, redirect
# Create your views here.
from . import models # Record, Project, Interaction, Communication
from django.views.generic import View, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class Base(View):  # Для вывода базового Base.html
    template_name = r'first\Base.html'

    def get(self, request):
        return render(request, self.template_name)

# _____________________________________| List View |_____________________________________


class RecordListView(ListView):
    # login_url = '/accounts/login/'
    model = models.Record
    paginate_by = 5
    template_name = r'first\RecordList.html'
    context_object_name = 'id'
    queryset = model.objects.all()

    def get_ordering(self):
        ordering = self.request.GET.get('ordering')
        return ordering


class ProjectListView(ListView):
    model = models.Project
    paginate_by = 5
    template_name = r'first\ProjectList.html'
    queryset = model.objects.all()
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.queryset.count()
        context['count_all'] = self.model.objects.count()
        return context

    def get_queryset(self):
        filter_val = self.request.GET.get('status')
        if filter_val != '' and filter_val is not None:
            self.queryset = self.queryset.filter(status=filter_val,)
        return self.queryset


class InteractionFilterView(ListView):  # List
    model = models.Interaction
    paginate_by = 5
    # template_name = r'first\InteractionList.html'
    template_name = r'first\InteractionFilter.html'
    queryset = model.objects.all()
    context_object_name = 'interactions'

    @staticmethod
    def is_valid_context(filter_val):
        return filter_val != '' and filter_val is not None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = models.Project.objects.distinct()
        context['records'] = models.Record.objects.distinct()
        context['communications'] = models.Communication.objects.distinct()
        return context

    def get_queryset(self):
        filter_project = self.request.GET.get('project')
        filter_record = self.request.GET.get('record')
        filter_communication = self.request.GET.get('communication')
        new_context = self.queryset

        if self.is_valid_context(filter_project):
            new_context = new_context.filter(project_id=filter_project, )
        if self.is_valid_context(filter_record):
            new_context = new_context.filter(company_id=filter_record, )
        if self.is_valid_context(filter_communication):
            new_context = new_context.filter(communication_id=filter_communication, )

        return new_context
# _____________________________________| NEXT Detail View |_____________________________________


class RecordDetailView(DetailView):
    model = models.Record
    template_name = r'first\RecordDetal.html'

    def get(self, pk, *args, **kwargs):
        content = {'record': self.model.objects.get(id=pk)}
        return render(self.request, self.template_name, content)


class InteractionDetailView(DetailView):  # Detail
    model = models.Interaction
    template_name = r'first\InteractionDetai.html'

    def get(self, pk, *args, **kwargs):
        content = {'interaction': self.model.objects.get(id=pk)}
        return render(self.request, self.template_name, content)
# _____________________________________| NEXT Forms |_____________________________________


from .forms import CompanyAddressForm, DescriptinForm, RecordForm,\
    ProjectForm, CommunicationForm, InteractionForm


class CompanyAddressCreate(LoginRequiredMixin, View):
    form_class = CompanyAddressForm
    initial = {'key': 'value'}
    template_name = r'first\Create\CompanyAddressCreate.html'

    def get(self, request):
        form = self.form_class(self.initial)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        error = ''
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BaseView')
        else:
            error = 'Форма была Неверной'
        context = {
            'form': form,
            'error': error
        }
        return render(request, self.template_name, context)


class DescriptinCreate(LoginRequiredMixin, View):
    form_class = DescriptinForm
    initial = {'key': 'value'}
    template_name = r'first\Create\DescriptinCreate.html'

    def get(self, request):
        form = self.form_class(self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BaseView')

        return render(request, self.template_name, {'form': form})


class RecordCreate(LoginRequiredMixin, View):
    form_class = RecordForm
    initial = {'key': 'value'}
    template_name = r'first\Create\RecordCreate.html'

    def get(self, request):
        form = self.form_class(self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BaseView')

        return render(request, self.template_name, {'form': form})


class ProjectCreate(LoginRequiredMixin, View):
    form_class = ProjectForm
    initial = {'key': 'value'}
    template_name = r'first\Create\ProjectCreate.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BaseView')

        return render(request, self.template_name, {'form': form})


class CommunicationCreate(LoginRequiredMixin, View):
    form_class = CommunicationForm
    initial = {'key': 'value'}
    template_name = r'first\Create\CommunicationCreate.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BaseView')

        return render(request, self.template_name, {'form': form})


class InteractionCreate(LoginRequiredMixin, View):
    form_class = InteractionForm
    initial = {'key': 'value'}
    template_name = r'first\Create\InteractionCreate.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BaseView')

        return render(request, self.template_name, {'form': form})
# _____________________________________| END |_____________________________________
