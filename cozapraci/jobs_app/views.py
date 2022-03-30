from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, CreateView,DetailView, FormView,ListView,UpdateView,DeleteView
from jobs_app.models import Job

# Create your views here.
class HomeView(TemplateView):
    template_name = 'jobs_app/home.html'

class ThankYouView(TemplateView):
    template_name = 'jobs_app/thank_you.html'

class JobCreateView(CreateView):
    model = Job
    fields = "__all__"
    success_url = reverse_lazy("jobs_app:thank_you")

class JobListView(ListView):
    model = Job
    query_set = Job.objects.order_by("job_name")
    context_object_name = 'jobs_list'

class JobDetailView(DetailView):
    model = Job