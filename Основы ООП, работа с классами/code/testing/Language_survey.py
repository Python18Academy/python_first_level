from survey import AnonymousSurvey

# Определяет вопрос, и сохраняет все вопросы
question = "Какой язык вы хотите изучить первым?"
my_survey = AnonymousSurvey(question)

# показывает вопрос и сохраняет ответ
my_survey.show_question()
print("Введите 'q' для окончания работы программы\n")
while True:
    response = input("Язык: \n")
    if response == 'q':
        break
    my_survey.store_response(response)

# Показывает результаты опроса
print("\n Спасибо за участие в этом опросе")
my_survey.show_results()
