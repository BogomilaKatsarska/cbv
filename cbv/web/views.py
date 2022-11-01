import random

from django.http import HttpResponse
from django.shortcuts import render


def index():
    pass


class IndexView:
    # The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach.
    # The __init__  function is called every time an object is created from a class.
    # The __init__ method lets the class initialize the object’s attributes and serves no other purpose.
    # It is only used within classes.
    def __init__(self):
        self.values = [
            random.randint(1, 15),
            ]

    @classmethod
    def get_view(cls):
        return cls().view

    def view(self, request):
        return HttpResponse(f'It works: {self.values}')


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