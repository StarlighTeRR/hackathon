from django.shortcuts import render
from .models import Question, Answer, Result
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def answer_detail(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    return render(request, 'question_detail.html', {'question': answer.question})

def submit_answers(request):
    if request.method == 'POST':
        # Получаем данные из POST запроса
        answers = {}
        for key, value in request.POST.items():
            if key.startswith('answer'):
                question_id = int(key.replace('answer', ''))
                choice_id = int(value)
                answers[question_id] = choice_id
        # Сохраняем ответы в базе данных или выполняем другие нужные действия
        # Здесь вы можете использовать полученные ответы для сохранения их в базе данных или для выполнения другой логики
        
        # После обработки ответов, перенаправляем пользователя на другую страницу, например, на страницу "спасибо"
        return HttpResponseRedirect('/thank-you/')  # Замените '/thank-you/' на URL страницы "спасибо" 

    # Если запрос не является POST запросом, возвращаем ошибку
    return HttpResponse("Method Not Allowed", status=405)