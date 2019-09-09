from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello<h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', {'dogs': dogs})

class Dog:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed 
    self.description = description
    self.age = age

dogs = [
  Dog('Ace', 'Pit/Lab', 'Tan', 4),
  Dog('Chloe', 'Boxer', 'Nub tail', 13),
  Dog('Diesel', 'Brindel', 'Dosile', 8)
]