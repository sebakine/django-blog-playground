from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from .forms import PageForm

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Page.objects.filter(title__icontains=query)
        return Page.objects.all()

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')
