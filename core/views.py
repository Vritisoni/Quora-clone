from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.contrib.auth.decorators import login_required

def home(request):
    questions = Question.objects.all().prefetch_related('answer_set')
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})


def ask_question(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Question.objects.create(title=title, description=description, posted_by=request.user)
        return redirect('home')
    return render(request, 'ask_question.html')

@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        answer_text = request.POST['answer']
        Answer.objects.create(question=question, answer_text=answer_text, answered_by=request.user)
        return redirect('home')
    return render(request, 'answer_form.html', {'question': question})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user not in answer.likes.all():
        answer.likes.add(request.user)
    return redirect('home')

def question_list(request):
    questions = Question.objects.all().prefetch_related('answer_set')
    return render(request, 'home.html', {'questions': questions})
