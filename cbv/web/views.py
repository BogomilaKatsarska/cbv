import random
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic as views

from cbv.web.models import Employee


def index(request):
    context = {
        'title': 'FBV',
    }

    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Bare view',
        }

        return render(request, 'index.html', context)

    def post(self, request):
        pass


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {
        # static context
        'title': 'Template view',
    }
    # Dynamic context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class IndexViewWithListView(views.ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employees'
    extra_context = {
        'title': 'List view',
    }

# def my_view(request):
#     handler = None
#     if request.method == 'GET':
#         handler = self.get
#     else:
#         handler = self.post
#     return handler

# class IndexView:
#     # The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach.
#     # The __init__  function is called every time an object is created from a class.
#     # The __init__ method lets the class initialize the object’s attributes and serves no other purpose.
#     # It is only used within classes.
#     def __init__(self):
#         self.values = [
#             random.randint(1, 15),
#             ]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It works: {self.values}')


class Index2View(IndexView):
    def __init__(self):
        # The super() function is used to give access to methods and properties of a parent or sibling class.
        # The super() function returns an object that represents the parent class.
        super().__init__()
        self.values.append(random.randint(15, 30))


def view(request):
    return HttpResponse('It works')


class IndexViewWithProfile(IndexView):
    pass