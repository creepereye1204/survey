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


def get_color(value: int, cnt: int) -> str:
    red = int((value / cnt) * 255)
    green = 255 - red
    return f'rgb({red}, {green}, 0)'


def gamble_survey_result(y) -> dict:
    if y < 1e-10:
        return {
            '증상': '비문제',
            '설명': '도박증 상이 없어 보입니다!',
            '처방전': '지금 이상태를 유지하세요.',
            '레벨': get_color(y, 3)
        }
    elif y == 1:
        return {
            '증상': '저위험도박',
            '설명': '도박을 즐기고 있으나 큰 문제가 없습니다.',
            '처방전': '도박 시간을 제한하고, 예산을 설정하세요.',
            '레벨': get_color(y, 3)
        }
    elif y == 2:
        return {
            '증상': '중위험도박',
            '설명': '도박이 일상에 약간의 영향을 미치고 있습니다.',
            '처방전': '도박 시간을 조절하고, 전문 상담을 고려하세요.',
            '레벨': get_color(y, 3)
        }
    else:
        return {
            '증상': '문제도박',
            '설명': '도박이 생활에 심각한 영향을 미치고 있습니다.',
            '처방전': '전문 상담을 받으세요. 도박을 완전히 중단하는 것이 필요합니다.',
            '레벨': get_color(y, 3)
        }


def home_page(request):
    return render(request, 'home.html')


def gamble_page(request):
    if request.method == 'POST':
        answers = []
        for i in range(len(questions)):
            answer = request.POST.get(f'question{i + 1}', None)
            if answer:
                answers.append(int(answer))

        x = np.array([answers])
        y = logistic_model.predict(x)

        result = gamble_survey_result(y)

        return render(request, 'result.html', {'result': result})

    return render(request, 'gamble.html', {
        'choices': choices,
        'questions': questions
    })


def diabetes_page(request):
    if request.method == 'POST':
        return render(request, 'result.html')
    return render(request, 'diabetes.html')
