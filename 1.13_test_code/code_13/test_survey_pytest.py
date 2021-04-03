import pytest
from survey import AnonymousSurvey


question = "На каком языке вы захотите заговорить"
my_survey = AnonymousSurvey(question)
responses = ['English', 'Spanish', 'Mandarin']

def test_store_single_response():
    """Проверяет что одиночный ответ был сохранен правильно"""
    my_survey.store_response(responses[0])
    assert responses[0] in my_survey.responses


def test_store_three_responses():
    """ Проверяет что каждый отдельный ответ был сохранен правильно"""
    for response in responses:
            my_survey.store_response(response)
    for response in responses:
           assert response in my_survey.responses

