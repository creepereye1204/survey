# views.py
import joblib
import numpy as np
from django.shortcuts import render

logistic_model = joblib.load('logistic_model.pkl')

questions = [
    "도박에 많은 시간을 보내고 있습니까?", "도박으로 인해 가족이나 친구들과 갈등이 있습니까?",
    "도박으로 인해 직장이나 학업에 어려움이 있습니까?", "도박으로 인해 재정적 문제가 있습니까?",
    "도박을 하지 않을 때 불안감이나 초조함을 느낍니까?", "도박을 하다가 돈을 잃으면 다시 도박을 하여 잃은 돈을 만회하려 합니까?",
    "도박으로 인해 건강에 문제가 있습니까?", "도박으로 인해 법적 문제가 있습니까?", "도박으로 인해 대인관계에 어려움이 있습니까?"
]

choices = {
    "해당사항 없음": 0,
    "조금 그렇다": 1,
    "그렇다": 2,
    "매우 그렇다": 3,
}


def gamble_survey_result(y) -> str:
    z: str = ''
    if y == 0:
        z = '비문제'
    elif y == 1:
        z = '저위험도박'
    elif y == 2:
        z = '중위험도박'
    elif y == 3:
        z = '문제도박'
    return z


def home_page(request):
    return render(request, 'home.html')


def gamble_page(request):
    if request.method == 'POST':
        answers = []
        for i in range(len(questions)):
            answer = request.POST.get(f'question{i + 1}', None)
            if answer:
                answers.append(answer)
        x = np.array([answers])
        y = logistic_model.predict(x)

        return render(request, 'result.html',
                      {'result': gamble_survey_result(y)})

    return render(request, 'gamble.html', {
        'choices': choices,
        'questions': questions
    })


def diabetes_page(request):
    if request.method == 'POST':
        return render(request, 'result.html')
    return render(request, 'diabetes.html')
