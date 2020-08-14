from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from trivia_app.models import Quiz

# Create your views here.
def index(request):
        return render(request, 'index.html')

#Function to save data into db
def user_Data(request):
        if request.method == "POST":
                user_name = request.POST.get('user_name')
                best_player = request.POST.get('best_player')
                flag_color = request.POST.getlist('flag_color')
        
                quiz = Quiz(user_name=user_name, best_player=best_player, flag_color=flag_color)
                quiz.save()

                recent_data = Quiz.objects.last()
                return render(request, "summary.html", {'recent_data': recent_data})

#Function to view summary
def summary(request):
        recent_data = Quiz.objects.last()
        return render(request, "summary.html", {'recent_data': recent_data})

#Function to show entire history
def history(request):
        data = Quiz.objects.all()
        return render(request, "history.html", {'data': data})
