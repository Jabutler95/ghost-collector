from django.shortcuts import render
from django.http import HttpResponse


class Ghost:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, city, state):
    self.name = name
    self.description = description
    self.city = city
    self.state = state
    
    

ghosts = [
  Ghost('Lolo', 'Kinda rude.', 'Gainesville', 'Florida'),
  Ghost('Sachi', 'Looks like a turtle.', 'Saint Petersburg', 'Florida'),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>BOOOOOO!!!</h1>')

def about(request):
  return render(request, 'about.html')

def ghost_index(request):
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })