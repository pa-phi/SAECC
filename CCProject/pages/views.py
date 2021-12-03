from django.shortcuts import render

# Create your views here.
def mainPage(request):
  return render(request, 'index.html')

# Create your views here.
def testPage(request):
  return render(request, 'test.html')
