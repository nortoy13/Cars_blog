from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from cars.forms import *

from .models import *


# Create your views here.
class CarsHome(ListView):
    model = CarsModel
    template_name = 'cars/home.html'
    context_object_name = "cars"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        
        return context
    
    def get_queryset(self):
        return CarsModel.objects.all().order_by('-time_created')
    

def show_about(request):
    return render(request, 'cars/about.html')


class ShowCar(DetailView):
    model = CarsModel
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'
    slug_url_kwarg = 'car_slug'

class CarCategory(ListView):
    model = CarsModel
    template_name = 'cars/home.html'
    context_object_name='cars'
    # allow_empty = False

    def get_queryset(self):
        return CarsModel.objects.filter(cat__slug=self.kwargs['cat_slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        context['category'] = Category.objects.get(slug=self.kwargs['cat_slug'])
        
        return context
    
class CreateBlog(CreateView):
    model = CarsModel
    template_name = 'cars/add_blog.html'
    success_url = reverse_lazy('home')
    fields = ['brand', 'model', 'slug', 'year', 'description', 'photo', 'cat']

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'cars/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    class_form = LoginUserForm
    template_name = 'cars/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
def logout_user(request):
    logout(request)
    return redirect('login')