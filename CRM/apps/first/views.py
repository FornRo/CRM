from django.shortcuts import render, redirect
# Create your views here.
from .models import Record, Project, Interaction, Communication
from django.views.generic import View, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class Base(View): # Для вывода базового Base.html
    template_name = r'first\Base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class RecordListView(ListView): # LoginRequiredMixin
    # login_url = '/accounts/login/'
    model = Record
    paginate_by = 5
    template_name = r'first\RecordList.html'
    context_object_name = 'id'
    queryset = model.objects.all()

    def get_ordering(self):
        ordering = self.request.GET.get('ordering')
        return ordering

class RecordDetailView(DetailView):
    model = Record
    template_name = r'first\RecordDetal.html'

    def get(self, pk, *args, **kwargs):
        content = {'record': self.model.objects.get(id=pk)}
        return render(self.request, self.template_name, content)

# ______________________________
from .forms import RecordForm

def PostRecordAdd(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=form.pk)
    else:
        form = RecordForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def PostRecordEdit(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=form.pk)
    else:
        form = RecordForm()
    return render(request, 'blog/post_edit.html', {'form': form})




class ProjectListView(ListView):
    model = Project
    paginate_by = 5
    template_name = r'first\ProjectList.html'
    queryset = model.objects.all()
    context_object_name = 'projects'

    def get_queryset(self):
        filter_val = self.request.GET.get('status')
        new_context = self.queryset
        if filter_val != '' and filter_val is not None:
            new_context = self.model.objects.filter(status=filter_val,)
        return new_context

class InteractionListView(ListView): # List
    model = Interaction
    paginate_by = 5
    # template_name = r'first\InteractionList.html'
    template_name = r'first\InteractionFilter.html'
    queryset = model.objects.all()
    context_object_name = 'interactions'

    def is_valid_context(self, filter_val):
        return filter_val != '' and filter_val is not None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.distinct()
        context['records'] = Record.objects.distinct()
        context['communications'] = Communication.objects.distinct()
        return context

    def get_queryset(self):
        filter_project = self.request.GET.get('project')
        filter_record = self.request.GET.get('record')
        filter_communication = self.request.GET.get('communication')
        new_context = self.queryset

        if self.is_valid_context(filter_project):
            new_context = new_context.filter(project_id=filter_project,)
        if self.is_valid_context(filter_record):
            new_context = new_context.filter(company_id=filter_record,)
        if self.is_valid_context(filter_communication):
            new_context = new_context.filter(communication_id=filter_communication,)

        return new_context

class InteractionDetailView(DetailView): # Detail
    model = Interaction
    template_name = r'first\InteractionDetai.html'

    def get(self, request, pk, *args, **kwargs):
        content = {'interaction': self.model.objects.get(id=pk)}
        return render(request, self.template_name, content)

