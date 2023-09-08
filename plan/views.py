from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import WorkoutPlans

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLogin(LoginView):
    template_name = 'plan/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('plan_list')


class Register(FormView):
    template_name = 'plan/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('plan_list')

    def form_valid(self, form):
        user = form.save()
        if user is None:
            login(self.request, user)
        return super(self, Register).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('plan_list')
        return super(self, Register).get(*args, **kwargs)


class PlanList(LoginRequiredMixin, ListView):
    model = WorkoutPlans
    context_object_name = 'plan_list'


class PlanCreate(LoginRequiredMixin, CreateView):
    model = WorkoutPlans
    fields = ['title', 'arm_day', 'shoulder_day', 'back_day', 'chest_day', 'leg_day']
    success_url = reverse_lazy('plan_list')


class PlanEdit(LoginRequiredMixin, UpdateView):
    model = WorkoutPlans
    fields = ['title', 'arm_day', 'shoulder_day', 'back_day', 'chest_day', 'leg_day']
    success_url = reverse_lazy('plan_list')


class PlanDelete(LoginRequiredMixin, DeleteView):
    model = WorkoutPlans
    success_url = reverse_lazy('plan_list')






