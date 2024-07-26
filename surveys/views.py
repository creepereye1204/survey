# views.py

from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def gamble_page(request):
    if request.method == 'POST':
        return render(request, 'result.html')

    questions = [
        "도박에 많은 시간을 보내고 있습니까?", "도박으로 인해 가족이나 친구들과 갈등이 있습니까?",
        "도박으로 인해 직장이나 학업에 어려움이 있습니까?", "도박으로 인해 재정적 문제가 있습니까?",
        "도박을 하지 않을 때 불안감이나 초조함을 느낍니까?",
        "도박을 하다가 돈을 잃으면 다시 도박을 하여 잃은 돈을 만회하려 합니까?", "도박으로 인해 건강에 문제가 있습니까?",
        "도박으로 인해 법적 문제가 있습니까?", "도박으로 인해 대인관계에 어려움이 있습니까?"
    ]

    choices = {
        "해당사항 없음": 0,
        "조금 그렇다": 1,
        "그렇다": 2,
        "매우 그렇다": 3,
    }

    return render(request, 'gamble.html', {
        'choices': choices,
        'questions': questions
    })


def diabetes_page(request):
    if request.method == 'POST':
        return render(request, 'result.html')
    return render(request, 'diabetes.html')
